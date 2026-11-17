# Loading Flight Data

With no flight loaded, the **Flight** menu offers four items.

## Create

Choose **Create**, then pick a log file. FCScore works out whether it is an ArduPilot BIN file or an AcroWRX file from the file name and contents. If it can read it as neither, it tells you why each attempt failed.

For a BIN file:

- FCScore checks whether the file is already loaded and reads it, showing progress.
- A summary shows the boot time, duration, logging frequency and the position of the flight. The flight is cropped to the airborne part of the log.
- You can optionally add a Flight Coach JSON file (`.json`, `.f3a`). It supplies your recorded box position and manoeuvre splits. If its pilot position is far from the position in the BIN file you are asked whether to use it anyway.
- A warning is shown if the logging rate is 18 Hz or below. FCScore expects about 20 Hz and asks you to confirm before continuing at a lower rate.
- Click **Continue to box setup** to go to the [box](box_definition.md).

For an AcroWRX file, FCScore looks the sequence up in the database. If the sequence is not there yet you are asked to choose the judging rules (**Judging rules** list, then **Continue**) to create its schedule with.

## Import

**Import** opens "Import BIN or AJSON File". Select a saved analysis (`.ajson` or `.json` file), choose whether the matching flight file is **Ardupilot** or **AcroWrx**, select that file, then click **Load**. This restores a previous analysis, including its splits.

## Load Template and Example

**Load Template** opens the results view without a recorded flight. **Example** loads a built-in example flight so you can look around without a log of your own.

## Sending flights directly

The client also accepts flights sent from AcroWRX or the Flight Coach Plotter by the external upload route. These arrive already loaded.

Next: [Set up the box](box_definition.md).
