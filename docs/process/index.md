# Analysis Process

These pages explain how FCScore turns a flight log into a score, in the order that the analysis works. They supplement the instructions for using the client in the [instructions](../instructions/index.md), and the help on each page of the client.

[Modelling Aerobatic Sequences](sequence_definition.md) describes how a schedule is turned into a model of the manoeuvres, their elements, and the parameters that link them, which is the template that the flight is judged against.

[Element Splitting](segmentation.md) explains how the flown data of each manoeuvre is divided into its principal elements.

[Intra Element Assessment](intra.md) explains how errors within a single element are measured, selected and converted to downgrades, and how the downgrades make up the manoeuvre score.

[Inter Element Assessment](inter.md) explains how parameters that should be the same in different elements, such as loop radii and roll rates, are compared.

[Positioning Assessment](box.md) explains the box, the box downgrades and how the centre of a manoeuvre is found.

[Visibility](visibility.md) explains how the judge's position and the attitude of the aircraft change how much of a small error is charged.

The [downgrade reference](../downgrades/index.md) lists every downgrade for each discipline, with what it measures, where, how visibility affects it and the rulebook text it is based on.
