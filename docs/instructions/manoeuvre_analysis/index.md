# Understanding the Results

Click a manoeuvre in the [results table](../scoring/results.md) to open its detail view. This page explains how to read it. For how the scores are calculated see [How it works](../../process/index.md); for what each downgrade measures see the [downgrade reference](../../downgrades/index.md).

## The manoeuvre view

The flown manoeuvre is drawn in 3D. The **Manoeuvre Results** panel on the left contains:

- **Back to sequence** and the previous and next manoeuvre buttons.
- **Adjust segmentation**, which opens the [element segmentation](element_segmentation.md) tools.
- A gear menu with preferences: **Auto-advance to the next manoeuvre** (moves on when playback reaches the end), **Show active element downgrades**, **Show template** (the ideal manoeuvre drawn for comparison) and, when a comparison flight is loaded, **Show comparison flight**.
- Score buttons for **intra**, **inter** and **Box** (positioning), each with its score, and the manoeuvre **Total**.

While the analysis is running the panel shows its stage ("Analysis running: Aligning 3/6"), or "Waiting for analysis" if it is queued.

## The three score types

Click **intra**, **inter** or **Box** to list the downgrades that make up that score, with the points lost for each and a total.

- [Intra downgrades](intra.md): how well each element was flown.
- [Inter downgrades](inter.md): how well the manoeuvre compares with the schedule, for example sizes and angles between elements.
- [Positioning downgrades](positioning.md): where the manoeuvre was flown in the box.

## Inspecting a downgrade

Click a row in the table to select that downgrade. The 3D view marks where the loss occurred, and a panel at the bottom shows its description and the judging guide text for the rule set. Scrub the playback to follow the aircraft. With **Show active element downgrades** on, an overlay lists the downgrades that apply at the aircraft's current position; click one to select it.

## The analysis settings

Analysis version, difficulty and truncation are set from the **Analysis** menu on the sequence page, or from **Info**. See [Results](../scoring/results.md).
