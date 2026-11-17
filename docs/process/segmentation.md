# Element Splitting

A manoeuvre is flown as a series of principal elements: lines, loops, snaps, spins, stall turns and tail slides. Element splitting finds where each element starts and stops in your flight data. A human judge does this without thinking. For the software it is one of the hardest steps in scoring a flight.

It matters because almost every downgrade is measured on a particular element or on the join between two elements. If a split is in the wrong place, a line can pick up part of the loop before it, or a roll can be measured over the wrong stretch of flight. The score then changes even though your flying did not.

## Two levels of splitting

Splitting happens at two levels.

1. **Manoeuvre level.** The whole flight is cut into manoeuvres. The analysis server compares the flight with the characteristics of each manoeuvre in the schedule (looping, upright or inverted, horizontal or vertical, rolling, snapping, stalling) and finds the sequence of manoeuvres that fits best. The split between two manoeuvres sits on the line between them. You can check and adjust these splits on the flight's segmentation page. See [Manoeuvre Segmentation](../instructions/scoring/manoeuvre_segmentation.md).
2. **Element level.** Within one manoeuvre, the elements are found by element alignment. This page is mostly about that step.

## Element alignment

Element alignment uses a hidden Markov model (HMM). Earlier versions used dynamic time warping, which is no longer offered.

The model for a manoeuvre is built in advance from the schedule definition and stored in the database with the schedule. The analysis server does not build models on request. If a manoeuvre has no stored model that matches the current alignment settings, the analysis is refused (HTTP 412) with a message asking for the schedule's manoeuvres to be updated. This also happens for a schedule definition you have edited locally, because the stored model was built from the database definition.

### How it works

- **States.** Each element of the manoeuvre becomes a state in the model. When an element turns through a large angle, it can be split into ordered sub-states (about every 45 degrees of turn or roll) so that the decoder tracks progress through it.
- **Emissions.** At each sample, the model asks how well the measured flight matches each state. It uses body rotation rates, roll attitude and the direction of the velocity track, compared with what that element should look like.
- **Legal transitions.** A state can only be followed by the next element in the definition. Where a manoeuvre has options, or combinations such as roll direction choices, the model contains each alternative, and a path is only legal if it stays within one consistent choice.
- **Decoding.** The Viterbi algorithm finds the single most likely path through the states for the whole manoeuvre. The points where the path changes element are the splits.

The option you flew, and the roll directions and other combination choices, are taken from the best scoring legal path. You do not have to say which you flew.

## Split optimisation

The HMM gives a good first estimate of the splits. The split optimiser then refines it.

The optimiser moves each split to reduce the total downgrade. The total includes the intra element downgrades on either side of the split, the inter element downgrades that depend on the split, and positioning. It works first on a fast approximation of how each downgrade changes as the split moves. It then rescores the manoeuvre in full with the new splits.

To a pilot this means the optimiser may place a split wherever gives the best score, so long as the split stays between the elements either side and each element keeps enough data samples. A split cannot jump past a neighbouring element.

### Score guard

The server runs the optimiser with a score guard. The optimised result is kept only if its full score is better than the score before optimising. Otherwise the splits from the alignment stay as they were. The optimiser therefore cannot make a manoeuvre score worse than the starting splits.

## When each stage runs

- **First analysis of a flight.** Alignment and then split optimisation both run.
- **Re-analysis with new analysis version.** The splits already stored for the manoeuvre are kept. Only the split optimisation runs, starting from the stored splits.
- **Loading a flight from the database for the same analysis version.** The manoeuvre is rescored with the stored splits and the splits are not moved, so the score should be identical.
- **Stored splits that do not match the definition.** If the stored element names do not fit the schedule definition, the alignment is run again.

## What can go wrong

If the first estimate is a long way from the true splits, the optimiser cannot recover and the manoeuvre may score zero.

- **A poor manoeuvre-level split.** If the split between manoeuvres cuts into the loop or radius at the start or end of the manoeuvre, the alignment starts from bad data. Go back to the segmentation page and correct the manoeuvre splits.
- **A very short or missing element.** The decoder needs a minimum number of samples for each element. Very short elements, or an element that was barely flown, can fail or be placed badly.
- **Ambiguous rolls.** In roll combinations with a change of direction, the decoder can choose the wrong roll direction or place the reversal badly.
- **Stuck optimiser.** The optimiser can finish on a local minimum that is not the best position.

## How to fix it

Open the manoeuvre from the results page and press **Adjust segmentation**. In the **Element Segmentation** menu, drag the plane between two elements to move that split. Then either:

- press **Score current boundaries** to score with your splits exactly as placed, or
- press **Optimise from current boundaries** to run the optimiser starting from your splits.

**Reset boundary changes** restores the original splits. The two scoring buttons are enabled once you have moved a split.

Step by step instructions are in [Element Segmentation](../instructions/manoeuvre_analysis/element_segmentation.md).
