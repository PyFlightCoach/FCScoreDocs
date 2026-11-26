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
