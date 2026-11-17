# Set Up The Box

The box page shows your flight in a 3D view with a **Box** panel on the left. The box position and heading matter: positioning scores and the manoeuvre alignment depend on them.

## Choosing the box

Use **Input Mode** to describe the box in one of four ways:

| Input mode | What you provide |
|---|---|
| Flight Coach Sites | Pick a known flying site from the list. |
| Pilot, Centre | Latitude, longitude and altitude of the pilot position and of the centre of the box. |
| Pilot, Heading | Latitude, longitude and altitude of the pilot position and the box heading. |
| F3A Zone / FC JSON File | **Select Box File**: an F3A zone file or Flight Coach JSON file. |

Warnings appear if the box is more than 500 m from the position in the BIN file, or if the box elevation differs from the BIN landing elevation. When the second warning appears with a BIN file, **Reset elevation** sets the box elevation to the BIN value. The panel also shows the ground elevation looked up for the box.

Other controls:

- **Open map view** shows the flight on a map with the box, so you can drag it into place.
- **Reset box** returns to the box the flight was loaded with.

## Moving on

Click **Score**. The "Score flight" window offers two routes:

- Choose the schedule(s) you flew and click **Start segmentation and scoring**. FCScore finds the manoeuvres itself. See [Define The Manoeuvres](manoeuvre_segmentation.md) and [Scoring against several schedules](multiple_schedules.md).
- Click **Split manoeuvres manually** to mark each manoeuvre yourself.

For AcroWRX files that carry their own sequence, a **Split and score AcroWRX sequence** button is also offered, with a category choice (primary to unlimited).

You can come back to the box at any time from the Flight menu (**Box**).
