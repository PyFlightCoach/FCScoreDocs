# Intra Element Assessment

Downgrades that depend on the geometry of a single principal element are called *intra* element downgrades. Examples are the roundness of a loop, the heading drift along a line or the amount of rotation in a roll. Each one is listed, with its description and rulebook references, in the [downgrade reference](../downgrades/index.md).

Which downgrades apply to an element depends on the rules of the discipline (F3A, IMAC, IAC etc.), the type of element (line, loop, snap, spin, stall turn, roll), and the elements before and after it. For example, in F3A the heading drift on a line is not charged on the line before a spin or stall turn, where the pilot is allowed to drift with the wind, and a different set of downgrades applies instead. If a downgrade looks wrong, is missing, or is too harsh or too kind, let us know.

Every intra element downgrade is calculated in the same way. The steps below follow the order in which the analysis performs them.

## 1. Measure

A measurement is taken of the flown data, sometimes with reference to the template of the correct manoeuvre. The result is a value at every time sample. Examples are the angle between the flown track and the template track on a line, or the radius of the loop at each instant.

For example [Line Heading Drift](../downgrades/f3a.md#track_z) (`track_z` in the F3A rules) measures the sideways angle between the flight path and the template line. [Loop Roundness](../downgrades/f3a.md#radius) (`radius`) measures the radius of a circle fitted to the loop, and how much the aircraft's distance from its centre varies.

## 2. Estimate the visibility

Each measurement has one or more visibility models. They estimate, at every sample, how easy the error is to see from the judge's position, as a weighting between zero (hard to see) and one (easy to see). The weightings are multiplied together if there are several. For example a track error is harder to see when it is along the line of sight, and a roll error is harder to see when the judge is looking at the top or bottom of the aircraft. The models are described on the [visibility page](visibility.md).

## 3. Apply the visibility to the measurement

The measurement is reduced according to the visibility weighting. Only small errors are reduced. Errors beyond the limit of the downgrade curve (see step 6) are not reduced at all. See [visibility](visibility.md) for the function.

There is no separate smoothing step in the scoring of a downgrade. The measurement is used at the sample rate of the flight data. Criteria that look for increases in an error (such as track and roll) treat each separate rise as an error, and criteria such as loop roundness use the variation of the whole element.

## 4. Select the region

Some downgrades only apply to part of the element. A selector picks the samples to use. Examples in the F3A rules are the last sample of a line (entry heading and the exit track of loops, spins and snaps), the final few seconds before a spin entry, or the section of a snap or spin in which the aircraft is autorotating. Where there is no selector the whole element is used. The selector is applied to the measurement and its visibility, not to the raw flight data, so the measurement is made over the whole element and the selected samples are then scored.

## 5. Find the downgradable points

The criteria identify what is charged in the selected samples. Depending on the downgrade this is:

- every increase in the error away from zero, from each trough to the following peak (track and roll errors). A decrease is free, so correcting an error costs nothing but a drift that builds up does.
- one value for the whole selection, such as the variation of the radius around its average (loop roundness),
- the single largest value above or below a limit,
- one value for every sample or the last sample (end of roll angle, exit track),
- each stretch outside a boundary (positioning).

## 6. Look up the downgrade

Each error is converted to a downgrade by an error to downgrade curve defined for that downgrade in the discipline's rules. In the rules data a curve is given as an exponent, a reference error and the downgrade at that error. For example the F3A track and roll curves are linear and give 6 points at 90 degrees. The downgrade is the sum over all the points found in step 5.

## Manoeuvre size

Criteria that charge every separate increase, such as track and roll deviations, would charge a larger manoeuvre more simply because it takes longer to fly. For the downgrades marked as whole element `Continuous` downgrades with a duration exponent (in the F3A rules these are the line heading, line pitch and roll angle downgrades, with exponent 0.75) the downgrade is multiplied by (reference duration / flown duration) to the power of the exponent, and the factor is limited to between 0.7 and 1.4. The durations are those of the elements between the entry and exit lines. Downgrades that use a selector (such as the last sample of a line) are not scaled. The [downgrade reference](../downgrades/f3a.md#track_z) says which downgrades are scaled.

## From downgrades to the score

The downgrades from every element are added up, as are the inter element and positioning downgrades. The manoeuvre score is 10 minus the intra, inter and positioning totals, and it cannot go below zero.

Before they are added, each individual downgrade is passed through the difficulty setting. At difficulty 3, the default, the downgrade is unchanged. Difficulties 1 and 2 reduce downgrades below 6 points slightly (a 6 point downgrade stays at 6). 

Each of the three totals can optionally be truncated, which rounds it down to a multiple of half a point, as is done on judges' scores. The analysis server calculates both the truncated and untruncated scores, and the client displays the one selected. The analysis tools that compare scores use the untruncated version.

When a whole schedule is scored, the manoeuvre scores are weighted by the K factor of each manoeuvre in the schedule.
