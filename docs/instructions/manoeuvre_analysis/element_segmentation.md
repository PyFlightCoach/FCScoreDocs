# Element Segmentation

FCScore splits each manoeuvre into elements (lines, loops, rolls and so on) before scoring. [How it works](../../process/segmentation.md) describes how. Occasionally the boundary between two elements lands in the wrong place, or the optimiser settles on a poor solution. The element segmentation tools let you correct this.

## Opening the tools

In the manoeuvre view click **Adjust segmentation**. The **Element Segmentation** panel replaces the results panel and the boundaries between elements appear in the 3D view as planes, labelled with the elements either side (for example "line → loop").

## Moving a boundary

Drag a plane along the flight path to move the boundary between two elements. Dragging is disabled while an analysis is running.

The panel shows the **Current score** (total, intra, inter and positioning) and three buttons, enabled once you have moved a boundary:

- **Optimise from current boundaries**: runs the full alignment optimisation, starting from the boundaries you set.
- **Score current boundaries**: scores the manoeuvre with your boundaries exactly as placed, with no optimisation. This is the quick check.
- **Reset boundary changes**: restores the original boundaries and recalculates the score.

**Back to manoeuvre** returns to the results panel.

## When to use it

Use it only when the automatic segmentation has clearly gone wrong, for example when a plane sits well away from where the change of element happens. The panel notes that the tool is intended to be removed once automatic segmentation is robust enough. Boundaries you place yourself are scored as given when you use **Score current boundaries**, so place them as a judge would see the transition.
