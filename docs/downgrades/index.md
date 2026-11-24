# Downgrades

This is the reference for every downgrade FCScore can apply. There is one page per ruleset:

- [F3A](f3a.md)
- [IMAC](IMAC.md)
- [IAC Power](IAC.md)
- [IAC Glider](IACGlider.md)
- [CIVA](CIVA.md)
- [CIVA Glider](CIVAGlider.md)

The pages are generated from the Tuning data of FCScore, so they describe what the scoring code actually does. Each page opens with the rulebook edition its quotations come from.

## Kinds of downgrade

- **Intra-element**: how well a single element (line, loop, roll, and so on) is flown.
- **Positioning (box)**: where the manoeuvre sits relative to the judges and the box.
- **Inter-element**: how consistent elements are with each other within a manoeuvre, for example matching loop radii or roll rates.
- **Sequence-level score**: IAC, CIVA and IMAC judges give each sequence one extra mark for placing the figures in the box, weighted by its own K factor like an extra figure (Presentation in IAC, Positioning in CIVA, Airspace Control in IMAC). For these rulesets the positioning (box) downgrades of every figure are added up into this one score instead of being taken off each figure, and the ruleset's page describes it under *Sequence-level score*. F3A has no such score: its figures keep their box downgrades.

## Reading a description

Each downgrade has a short summary and, under *Details*, a longer explanation. Together they say:

- **What is measured**: the quantity FCScore extracts from the flight, such as a heading error or a radius.
- **Where**: the region of the element the measurement applies to, for example the whole element or only its end.
- **Visibility**: how much the measurement is discounted when the error is hard for a judge to see, for instance along the line of sight, or high or wide in the box.
- **Criteria**: how the (visibility scaled) measurement is turned into a downgrade in points.

Where a downgrade is an FCScore approximation rather than an explicit rule, the description says so or has no rulebook quotation. Quoted rulebook extracts are verbatim and are linked to the *Rulebook references* section at the end of each page.

Every downgrade can be linked to directly by its key, for example `f3a/#inter.loop_radius`.
