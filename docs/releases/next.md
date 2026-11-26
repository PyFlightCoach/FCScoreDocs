# Next release (draft)

!!! warning "Not released"
    This page collects the changes waiting for the next scoring release. It changes how
    flights are scored, so the release gets a new version number (not a `.post` release),
    which replaces the title of this page when it is released.

## Matching sizes in figures read from OLAN

**For IAC, IAC Glider, CIVA, CIVA Glider and IMAC schedules built from OLAN or OpenAero.**

The rules ask for some loops and lines within a figure to be the same size: the corners and
sides of the square, diamond and octagonal loops and the Family 3 figures, the two loops of an
S or an eight, the parts of a reversing loop, and so on. Until now a figure read from OLAN did
not link any of these sizes, so FCScore never compared them. From this release it does:

- **Loop Radius Matching** compares the part-loops the rules say must match. In general these
  are the part-loops OpenAero draws as round, not the corners; in Family 3 and the square,
  diamond and octagonal loops every corner matches too, and in the double humpty-bumps (8.8)
  none do. CIVA Glider pairs the corners of the square, diamond and octagonal loops by height
  (Figure 29: the top corners need not match the bottom ones).
- **Line Length Matching** compares the interior lines of Family 3 and of the square, diamond
  and octagonal loops, and the two 45° lines of the horizontal eights (7.8.1-7.8.8) for IAC,
  CIVA and IMAC power. The final horizontal line of a square or octagonal loop is not compared.
  For gliders, a line with a flick roll is left out.
- **Compared with the first.** Each radius or line is compared with the first one in the
  figure, as all four rulebooks say (IAC 27.9.5 and 27.13.5, CIVA B.8.1.5, CIVA-G B.8.1.12,
  IMAC 7.1 and 8.7.1 c). F3A keeps comparing each value with the previous one.
- **Non-Aresti figures are refused.** OpenAero's figures without an Aresti number (its Family
  0, such as the wingover and the quarter clover) cannot be analysed yet. A sequence holding
  one is refused with a message that lists them all. We are working on it.

**Effect on scores.** Only figures with linked sizes change, and only when the sizes the rules
compare differ: a figure flown with matching sizes scores the same as before, and figures with
nothing to link are not affected at all. We checked one OpenAero library sequence per rule set,
flown synthetically with every loop radius and line length varied by up to 30%. The linked
figures lost between 0.03 and 0.7 of a point each, and the average figure score of a sequence
fell by between 0.005 and 0.1:

| Rules | Sequence | Linked figures | Average figure score before | After |
| --- | --- | ---: | ---: | ---: |
| IAC | 2023 Intermediate Known | 2 of 12 | 8.79 | 8.75 |
| IAC Glider | 2021 Intermediate Known | 1 of 8 | 8.30 | 8.30 |
| CIVA | 2014 Advanced Known | 2 of 9 | 8.94 | 8.86 |
| CIVA Glider | 2018 Unlimited Free Known | 1 of 5 | 7.46 | 7.41 |
| IMAC | 2023 Intermediate Alt-Known | 2 of 10 | 9.06 | 9.03 |

Comparing with the first value instead of the previous one makes no difference when a figure
links two sizes, which is most of them. With more (the four corners of a square loop, the eight
of an octagonal loop) a size that grows a little at every corner costs more than before.

**Stored schedules** are not affected. A stored schedule keeps the definition it was saved
with, including its comparisons, so its flights score as before. To pick up the new
comparisons, read the sequence from OLAN again.
