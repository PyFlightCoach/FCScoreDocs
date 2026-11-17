# Positioning Assessment

Positioning downgrades are charged when a manoeuvre is not centred, or leaves the box in which it is supposed to be flown. They depend on the shape of the box, which is part of the rules of each discipline, and on the position of the judge.

## Box shape

- **F3A** uses a triangular box. The pilot stands at the origin and the box is defined by angles from the pilot: a width of 120 degrees (60 degrees either side of the centre), a height of 60 degrees and a floor of 15 degrees. Distance limits (150 m to 175 m in the rules data) are measured in metres. Limits are therefore measured as an angle, so the allowance grows with distance.
- **IMAC, IAC and IAC Glider** use a rectangular box, with limits in metres for width, depth, floor and height. The IAC box dimensions depend on the category, and for IAC Glider the floor and ceiling depend on the category.

The box that applies to a flight is the one chosen in the [box definition](../instructions/scoring/box_definition.md) and the schedule.

## Box downgrades

For each wall of the box, the measurement is how far the aircraft is outside it. Each stretch outside the box is charged by the average distance beyond the wall, weighted by the share of the manoeuvre's duration it lasts for, so a small or short excursion costs little. In each discipline some or all of these are defined. The F3A downgrades are:

- [Top](../downgrades/f3a.md#top): angle above the height limit.
- [Left](../downgrades/f3a.md#left) and [right](../downgrades/f3a.md#right): beyond the 60 degree lines.
- [Back](../downgrades/f3a.md#back): distance beyond the back limit, with backward drift of a spin during the manoeuvre allowed for. In F3A there is no front or bottom downgrade.
- IMAC, IAC and IAC Glider also define front and bottom walls; the keys are `top`, `right`, `left`, `back`, `front` and `btm` on [IMAC](../downgrades/IMAC.md#top), [IAC](../downgrades/IAC.md#top) and [IAC Glider](../downgrades/IACGlider.md#top).

Visibility reduces small errors in the same way as intra downgrades (see [visibility](visibility.md)). Large errors are charged in full. Which visibility applies depends on the wall: lateral limits are easier to judge when low in the box, top limits are always hard to judge and depth limits depend on the direction the aircraft is seen from.

## Centring

Where a manoeuvre is a centre manoeuvre, [Centre Position](../downgrades/f3a.md#centre) charges the angle, seen from the pilot, between the centre line and the aircraft at the centre point of the manoeuvre. The absolute angle is used, so left or right is the same. Manoeuvres with no centre point are not charged. The sequence definition says where the centre is: either a boundary between two elements, or a fraction of a centred element.

For a boundary the sample at the start of the element is used. For a centred element the centre is found geometrically wherever the element rotates, because the roll rate and rate of turn of a flown element are rarely constant:

- on a roll on a line or a snap, the centre is where the flown roll angle reaches the roll angle the template has at that fraction of the element (for example, inverted half way through a full roll),
- on a loop the centre is where the flown track angle reaches the template value (for example horizontal flight at the top of a half loop from vertical up to vertical down),
- a rolling loop has two centres, one for the loop and one for the roll, and each is charged,
- other centred elements use the same fraction of the path length flown.

The centre position is a fractional sample, so the downgrade changes smoothly if the splits move.
