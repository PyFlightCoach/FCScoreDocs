# Next release (draft)

!!! warning "Not released"
    This page collects the changes waiting for the next scoring release. It changes how
    flights are scored, so the release gets a new version number (not a `.post` release),
    which replaces the title of this page when it is released.

## Sizes compared with the first

**For IAC, IAC Glider, CIVA, CIVA Glider and IMAC.**

Loop Radius Matching and Line Length Matching now compare each radius or line with the first
one in the figure, as all four rulebooks say (IAC 27.9.5 and 27.13.5, CIVA B.8.1.5, CIVA-G
B.8.1.12, IMAC 7.1 and 8.7.1 c). Until now each was compared with the previous one. F3A keeps
comparing each value with the previous one. The hover label on these downgrades reads "Change
from first".

**Stored schedules** keep the comparisons they were saved with, so their flights score as
before. A schedule read from OLAN again, or a figure built again from the rule set, compares
with the first.

**Effect on scores.** A figure that links two sizes, which is most of them, scores the same
either way. With more (the four corners of a square loop, the eight of an octagonal loop) a
size that grows a little at every corner costs more than before, while one that wanders back
and forth costs less. In the sequences checked for the
[OLAN sizing update](1.0.0.md#matching-sizes-in-figures-read-from-olan), flown with every loop
radius and line length varied by up to 30%, two figures changed: a CIVA figure gained 0.19
and an IAC figure lost 0.04. The sequences' average figure scores moved by less than 0.03.

## Spin nose drop measured until the nose has dropped

**For F3A.**

[Spin Nose Drop](../downgrades/f3a.md#drop_pitch_rate) checks that the nose drops decisively
as the model stalls into the spin. It charges time spent with the nose dropping slower than
10° per second. Until now it looked at the spin from its start to the first 15° of rotation.
It now stops at 15° of rotation or when the nose has dropped 7.5°, whichever comes first.

In a clean stall break the nose drops first and then, for a moment as the wing drops, the
nose-down rate pauses. The old window took in that pause and charged it whenever the spin
was taken to start at the stall break, so the split was pushed later and the nose drop
was charged instead as a descent before the spin. A model that rotates without the nose
dropping is still checked over the whole 15° of rotation.

**Effect on scores.** Only F3A spins change, and only where the nose drops before the wing.
In a P27 spin flown that way, the spin scored 8.86 instead of 8.47 with the split at the
stall break. A spin entered with a climb and a late nose drop scored the same as before.
Stored schedules keep the definitions they were saved with until they are built again,
which the release does.

## Line track errors are easier to see around an attitude change

**For F3A.** The size of this change is still being tuned; the numbers below are for the
current setting.

A judge's eye is drawn by a visible change of pitch or yaw attitude on a line. A correction
shows up the error it corrects, and an attitude change can start a new error. The line track
downgrades ([Line Pitch Drift](../downgrades/f3a.md#track_y),
[Line Heading Drift](../downgrades/f3a.md#track_z), the entry line and the spin approach checks)
now count an error for more in the half second before and the second after such a change,
and for a little less where the aircraft is steady. F3A still judges the flight path only:
an attitude change with no track error costs nothing, and a steady crab into wind has no
attitude change.

The attitude change is measured against the template, on lines only, so the planned start of
the next loop or roll does not count. A small steady misalignment of the flight controller,
which would look like the nose circling on rolling lines, is taken out.

**Effect on scores.** Averaged over 230 F3A flights the line track downgrades are unchanged.
Flights with smooth lines gain and flights with many visible corrections lose, by about
2 points per flight either way (one standard deviation). Two P27 flights both gained, by 2.9
and 2.1 points. Stored schedules keep the definitions they were saved with until they are
built again, which the release does.
