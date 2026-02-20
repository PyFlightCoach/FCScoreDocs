
# Competition Options

| Option | Description |
|--------------------|-------------|
| Allow Pilots to Enter                  | Allows pilots to add themselves to the competition.  Otherwise, only CDs can add competitors.                             |
| Allow Pilots to Link Their Own Flights | Allows pilots to upload-and-link or link their own flights.  Otherwise, only CDs can link flights.                        |
| Start Date and End Date                | These are planning dates.  The actual dates and times in the database are calculated from when you open and close rounds. |

# Stage Options

| Option | Description |
|--------------------|-------------|
| Progress Top N |Only the best N competitors will be progressed from this stage to the next stage. |
| Use Top N | For each competitor, their best N round scores count (other scores are “dropped”). |
| Restart Scoring From this Stage | For competitors in this stage, all previous stage scores are dropped. An example is a FINAL stage where, for those making the FINAL, only the scores from the FINAL decide the result. |

## Round Options

| Option | Description |
|--------------------|-------------|
| Must Boot whilst Round is Open | Flights will only be accepted if their log file start time is from when the round is open. |
| Must upload whilst Round is Open | Flights will only be accepted if they are linked when the round is open. |
| Upload within (N hours) | Flight will only be accepted if it is uploaded and linked within N hours of the log file start  |time.
| Prevent Flight Overwrite | Competitors may only link one flight to a round. If they subsequently try to link another  |(probably better!) flight, it will be rejected.
| Score from Previous Stage | Takes the scores from a previous stage and uses them as the Raw Scores in this round. |

## Normalisation Options (Applies to Competition, Stages and Rounds)

| Option | Description |
|--------------------|-------------|
| Raw Score | No normalisation is applied; the raw flight scores are used. |
| Best Score N | Normalisation is applied such that the best score is normalised to N. |
| Average Score N | Normalisation is applied such that a raw score equal to the average of all scores would be normalised to  |N.

## Running Order Rotation Options

| Option | Description |
|--------------------|-------------|
| Continue from previous stage | The first round of this stage will be taken from the last round of the previous stage (with  |rotation applied).
| Randomise first round | The first round of this stage will have a random running order applied. |
| Rotate by N | The running order will be shifted down by N pilots between rounds. |