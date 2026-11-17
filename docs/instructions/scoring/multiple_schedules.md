# Scoring Against Several Schedules

One recording often holds more than one sequence: a warm-up and a competition flight, two different schedules, or the same schedule flown twice. FCScore can find and score all of them from a single log.

## Choosing the schedules

On the box page click **Score** to open the "Score flight" window.

1. In **Database schedules**, filter the table by category, type or owner and click **Select** on each schedule flown in this recording.
2. Each choice appears as a chip under **Selected (n/4)**. You can pick up to four schedules. Click the bin on a chip to remove it.
3. Click **Start segmentation and scoring**.

Repeats of a schedule are detected automatically, so select a schedule once even if you flew it several times.

## Reading the results

When the analysis has found more than one sequence, the Sequence Results panel shows a row of numbered buttons, one per sequence found, ordered by time in the flight. Each button shows the schedule name. The number of manoeuvres analysed so far (for example 7/16) is shown until the sequence is complete, and a pencil marks a sequence you have edited. Hover over a button to see its schedule, occurrence number, start and end times and whether it is the best match.

Click a button to switch the manoeuvre table, scores and 3D view to that sequence. Schedules that could not be found in the flight are listed in a warning under the buttons. If some manoeuvres of the selected sequence failed, **Retry failed** re-runs them.

### Overlapping matches

If two sequences found in the flight overlap in time, FCScore cannot tell which schedule the overlapping part belongs to. A warning lists the overlap and a tick box for each candidate. Tick the intervals that are genuine and click **Assign selected intervals** before scoring continues.

## Choosing between repetitions

When the same sequence was flown more than once, the results show "The sequence was flown N times" with a list of the repetitions. Each has a time range, a coloured marker and badges: **best match** is the one FCScore thinks matches the schedule best, and **scored** marks the one currently analysed. Select a different one to score that repetition instead. Changing it analyses the flight again and the earlier results for the previous repetition are discarded.

The **Show on flight** switch colours the repetitions on the 3D flight view (the scored one is green) so you can see which part of the flight each one covers.

When a recording is analysed with several schedules, repeats appear as separate numbered sequence buttons instead of this list.

## Uploading

Only one sequence from a recording can currently be uploaded to the database. If one has already been shared, the upload window says so. Select the sequence you want to share before clicking **Upload**.

## Progress while a sequence is analysed

An automatic analysis runs on the analysis server and reports its stage while it works.

- While the flight is being split into manoeuvres, a message over the 3D view reads "Splitting flight:" followed by the stage and its position out of three: **Loading** (1/3), **Measuring** (2/3) and **Matching** (3/3). Before that it may say "Preparing sequence…" or "Waiting to split flight…".
- Once split, each manoeuvre is analysed in turn. A running manoeuvre shows its stage out of six in the results table and in the manoeuvre view: **Loading**, **Starting**, **Aligning**, **Scoring**, **Optimising** and **Finishing** (for example "Aligning 3/6"). Manoeuvres waiting their turn show an hourglass and "Waiting for analysis".
- If the analysis server is older and does not report stages, the messages fall back to plain text such as "Preparing sequence…" or "Running".

The 3D view stays usable while the progress message is shown.

## Limits

The analysis server accepts at most four schedules per recording, at most 20 sequences found in total and at most five candidates per schedule.
