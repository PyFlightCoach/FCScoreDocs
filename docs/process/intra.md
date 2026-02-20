Downgrades applicable to a single principal element due to errors in the geometry of that element are denoted Intra element downgrades.

The downgrades are selected for each principal element based on the rules of the aerobatic discipline (F3A, IMAC, IAC etc.), the type of element, its driving geometric parameters, the elements that precede and follow it and measurements of the constructed template. This process, and the definition of the downgrades themselves is extremely configurable. If you find a downgrade that doesn't look right, you think one is missing, too harsh or too kind then let us know and we will fix it in a future release.

Every intra element downgrade is applied according to the following process.

1. **Take a Measurement** 

    A measurement is taken of the flight data, occasionally with reference to the corresponding template data. The result is an array of values. This array represents downgradable features such as the instantanious loop radius at every time instant for loop elements, or the difference between the flown track and the template track for line elements.

2. **Account for the Visibility** 

    The visibility of the error is estimated, taking into account the judges view vector. This produces a corresponding array of visibility values. These calculations depend on the type of measurement and the geometry of the flown data. For example track errors are harder to see when they are parallel to the view vector and roll angle errors are harder to see when you are looking at the top or bottom of the plane.

3. **Downselect the Sample** 

    The smoothed sample represents a measurement of the entire element, but in some cases only a portion of that data is relevant. One example is in F3A aerobatics on the line element before a spin, where the horisontal track criteria must be relaxed to allow some drift with the wind. Selectors such as this are used extensively in and around stalled manoeuvres such as snaps, spins and stallturns.

4. **Identify the Downgradable Points**

    Key downgradable points in the visible, smoothed, downselected sample are now identified. Depending on the downgrade this may be all peaks and troughs, just the absolute peaks, just the last point, some global measurement such as the standard deviation, excedences above or below a boundary or within a range.

4.  **Calculate the Downgrade**

    Finally, the downgrade for each downgradable point is calculated by looking up the value in a curve of error vs downgrade.
