# Visibility

A judge sees the manoeuvre from one position, and some errors are easy to see from there and others are not. A track error along the line of sight is almost invisible, a roll error is hard to see when looking at the underside of the aircraft, and small errors in a distant, high manoeuvre are harder to see than the same errors close and low. FCScore models this by weighting errors by how visible they are.

## The visibility weighting

For each measurement the visibility is a weighting between 0 (cannot be seen) and 1 (fully visible), calculated at each sample of the flight. Each downgrade specifies which visibility models apply to it, and if there are several they are multiplied together. The models are computed from the position of the aircraft relative to the judge (the view vector), its attitude, and the direction of the error. The main ones are:

- **Direction of the error.** A vector error (such as track) is easiest to see when it is perpendicular to the view vector, and hardest when along it. The weighting falls from 1 to 0.2 as the angle changes from perpendicular to parallel.
- **Attitude.** Roll and pitch angle errors are easiest to see when the body of the aircraft is edge on to the judge and hardest when the judge is looking at the top or bottom of it. Roll and pitch rates and the nose drop of a spin use similar models.
- **Loop shape.** Errors in the shape of a loop are most visible when the view vector is along the loop axis (the loop is seen face on), and least when it is seen edge on. For the rate of turn, the radial direction of the loop is used.
- **Position in the box.** The weighting falls for an aircraft that is high or wide in the box, away from straight in front of the judge.
- **Part elements.** Some downgrades are scaled by the amount of loop or roll flown, so a quarter loop is weighted at about a quarter of a full loop.
- **Awkward line angles.** Horizontal and vertical lines are easy to judge, 45 degree lines harder.

Positioning downgrades have their own models: the visibility of lateral position (easier low in the box), depth (easier at the edges of the box) and a constant, low value for the top of the box, which is always hard to judge.

Inter element comparisons are weighted by the size of the elements compared with the height of the box (see [inter element assessment](inter.md)).

## How it is applied

Visibility only reduces small errors. A visibility weighting `v` reduces an error `x`, expressed as a fraction of the limit of the downgrade curve (the error at which the downgrade reaches the largest value in the rules data, for example 90 degrees for the F3A track downgrade), as follows:

- if the error is greater than the limit it is unchanged,
- otherwise it becomes (1 - v) x^3 + v x, in units of the limit.

With v = 1 the error is unchanged. With a lower v a small error is reduced a lot, because the cubic term is tiny for small x, but the reduction fades smoothly to nothing as the error approaches the limit. So errors of a size that would be noticed whatever the view are charged in full, and only small errors in poor viewing conditions are discounted. The inter element weighting is different: it scales the downgrade of each comparison directly.

The same function is used for all intra and box downgrades. For the downgrades that measure variation, such as loop roundness, it is applied to the deviations from the average, and for the box downgrades it is applied to the distance outside each wall.

Each downgrade's visibility is described in the [downgrade reference](../downgrades/index.md).
