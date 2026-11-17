# Inter Element Assessment

As well as defining the elements themselves, the sequence definition defines the relationships between the controlling parameters of different elements within a manoeuvre. For example, all the loops in a manoeuvre must have the same radius, the lines before and after a roll must be the same length, or two rolls must be flown at the same rate. Downgrades for failing to meet these relationships are *inter* element downgrades. The ones for each discipline are in the *inter-element* section of the [downgrade reference](../downgrades/f3a.md#inter.loop_radius).

## Manoeuvre parameters

Each of these relationships is a manoeuvre parameter. It has a name (such as `loop_radius` or `full_roll_rate`), a unit, a criteria and a default value. The default value is replaced by the value the pilot actually flew, so the manoeuvre template is drawn at the size and speeds that the pilot chose. The defaults, and the criteria for each parameter, are part of the rules of each discipline.

## Collectors

A parameter has a list of collectors. Each collector names the element (or run of consecutive elements) of the manoeuvre whose value belongs to the parameter. The collector measures that value in the flown data. For example the loop radius parameter of a manoeuvre with two loops has one collector for each loop. If the manoeuvre was flown correctly all the values collected for a parameter are the same.

## Comparison

For most parameters the collected values are compared in order. Each value is compared with the one before it, the ratio of the larger to the smaller is found (a ratio of 1 is a perfect match) and the downgrade is looked up from the ratio error. The ratio means that the size of the loops or lines does not matter, only the proportional difference does: a 10% difference costs the same on a 50 m loop as on a 100 m loop. Very small ratio errors are smoothed slightly so that tiny differences are not charged. The first value is not compared with anything, so it sets the starting point rather than being judged.

## Visibility

The downgrade for each comparison is multiplied by a visibility weighting that is based on the size of the elements compared with the height of the box (larger elements are easier to compare). The more visible of the two elements in the comparison is used. A weighting of one is applied to elements that fill the box. This differs from the intra case: the weighting scales the downgrade rather than only reducing small errors. See [visibility](visibility.md).

## Parameters that are not downgraded

Some parameters are collected and used to define the template, but have no downgrade. In the F3A rules `speed` is a parameter with a comparison whose curve gives no downgrade, so a change of speed is not charged between elements. (Speed is judged within each element by the intra downgrade [Constant Speed](../downgrades/f3a.md#speed).) The same applies to the generic `free` comparison.

## Combinations and options

Not every parameter is a measurement. Some, such as the roll direction or the combination of rolls in a roll sequence, are a choice from a list of alternatives. This is called a combination. The pilot's flight is compared with each alternative and the nearest is taken as what was flown. Other options in the sequence definition, where a schedule allows more than one version of a manoeuvre, are handled in the same way: the version that best matches the flight is selected for scoring.
