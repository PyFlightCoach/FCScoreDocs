# Define The Manoeuvres

FCScore needs to know where each manoeuvre starts and ends. There are two ways to do this, both started from the **Score** button on the box page.

## Automatic

In the "Score flight" window, pick the schedule you flew from the **Database schedules** table (filter by category, type and owner, then click **Select**) and click **Start segmentation and scoring**. The analysis server finds the manoeuvres and you are taken to the results while the analysis runs. A stage indicator shows progress; see [Scoring against several schedules](multiple_schedules.md#progress-while-a-sequence-is-analysed).

If the automatic split is wrong for a manoeuvre, you can correct it from the results page: for AcroWRX flights the sequence menu offers **Edit splits**, and individual element boundaries can be corrected in the manoeuvre view ([Element segmentation](../manoeuvre_analysis/element_segmentation.md)). You can also go to **Manoeuvres** in the Flight menu to place the splits yourself.

## Manual

Choose **Split manoeuvres manually**, or **Manoeuvres** in the Flight menu. The **Manoeuvres** panel lists the manoeuvres with a status for each (current, accepted, waiting, queued, running, complete, failed).

For each manoeuvre in turn:

1. Click the ribbon (the flight trace) at the end of the manoeuvre. Click again to relocate it. You can also click and drag to preview the split and release to set it. The selected end point is shown in seconds.
2. If the manoeuvre is not the one expected, open the options arrow next to it and choose **Change manoeuvre** to pick another from the schedule library, or **Show template** to see what it should look like.
3. Click **Create next manoeuvre** (or press Enter). Double-clicking the ribbon sets the split and accepts it in one step.

Other things to know:

- Pressing `b` changes the current manoeuvre to a break between manoeuvres.
- Use the crop control below the plot to limit the visible range.
- **Delete this manoeuvre** (in the options menu) is available on the last manoeuvre only.
- **Segmentation tools** has **Read FC JSON** (take splits from a Flight Coach JSON file), **Restore loaded segmentation** and **Clear all splits**.
- When you reach Landing, the button changes to **View results**.

Each manoeuvre is analysed in the background as you accept it.
