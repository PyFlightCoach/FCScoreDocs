# Setting up your ArduPilot logger

Flight Coach Score works from the log your autopilot records. The attitude, position and velocity it scores come from that log, so how the logger is set up decides how well your flight can be analysed. A log recorded at a low rate, with dropped data, or with a noisy GPS, compass or accelerometer gives less reliable results.

When you load a BIN file, FCScore checks the log and, if it finds problems, shows a red warning card. Each section below matches one check in that warning, and the warning links straight to it. Most problems are fixed once, with a parameter change, and apply to every flight after that.

Things to know before you start:

- The parameter names and values below are for ArduPlane. Other vehicles use different logging bit numbers, so FCScore only gives bitmask advice for ArduPlane logs.
- A file that is not a DataFlash log at all (for example a JSON file saved with a `.bin` extension) cannot be checked. See [Not a DataFlash log](#not-a-bin).
- Checks that need a message the log does not contain (for example vibration, which needs the IMU bit) are not run for that log. A clean report does not prove those things are fine.
- The thresholds were chosen from a survey of 385 real ArduPlane logs (firmware 4.0 to 4.8), mostly from F3A pilots. They are starting points and may change.

## Recommended settings { #recommended }

| Parameter | Recommended | Why |
| --- | --- | --- |
| `LOG_BITMASK` | Fast attitude + GPS + IMU + compass at least | Attitude at a usable rate, GPS, measured accelerations, vibration data |
| `LOG_FILE_RATEMAX` | `0` | Removes the logging rate limit, which otherwise can halve the attitude rate |
| `GPS1_RATE_MS` (older firmware: `GPS_RATE_MS`) | `200` or lower | Five GPS updates per second or more |
| `AHRS_EKF_TYPE` | `3` | Use the EKF3 estimator that FCScore reads |
| `LOG_DISARMED` | `0` or `1` as you prefer | See [A7](#a7) |

### LOG_BITMASK

`LOG_BITMASK` is a sum of bit values. For ArduPlane (verified against the ArduPilot source and the [parameter page](https://ardupilot.org/plane/docs/parameters.html#log-bitmask)):

| Bit | Value | Logs |
| --- | --- | --- |
| 0 | 1 | Fast attitude |
| 1 | 2 | Medium attitude |
| 2 | 4 | GPS |
| 3 | 8 | Performance (PM) |
| 4 | 16 | Control tuning |
| 5 | 32 | Navigation tuning |
| 7 | 128 | IMU |
| 8 | 256 | Mission commands |
| 9 | 512 | Battery monitor (POWR) |
| 10 | 1024 | Compass |
| 11 | 2048 | TECS |
| 13 | 8192 | RC input and output |

(Other bits exist; see the parameter page.)

A common setting is **1029** = 1024 (compass) + 4 (GPS) + 1 (fast attitude). It has no IMU. Add the IMU bit, 128, to get **1157**. Worked example: 1029 + 128 = 1157. To add a bit to your own value, add its value if it is not already set (check by looking at the table: for example 65535 already has every bit up to 15 set).

Enabling the IMU bit also turns on vibration logging (the `VIBE` message), which lets FCScore run the vibration check ([B3](#b3)). Bit 3 (performance, 8) and bit 9 (battery monitor, 512) enable the CPU and power messages used by [B6](#b6) and [B7](#b7). Adding them is optional: 1157 + 8 + 512 = 1677. A value of 65535 sets everything, at the cost of larger log files.

### Setting parameters

Connect the autopilot, then in **Mission Planner**: *Config* (or *Setup*), *Full Parameter List* (or *Full Parameter Tree*), search for the name, edit the value, then *Write Params*. In **QGroundControl**: *Vehicle Setup*, *Parameters*, search for the name, click the value, enter the new one and save. In `LOG_BITMASK`, Mission Planner's *Full Parameter Tree* shows tick boxes for the bits. Reboot the autopilot afterwards; some logging parameters only apply at start-up.

These menu names are general guidance and have not been checked against current versions of either program; see the ArduPilot [Mission Planner](https://ardupilot.org/planner/) and [QGroundControl](https://qgroundcontrol.com/) documentation if the menus differ.

## Not a DataFlash log { #not-a-bin }

If FCScore finds no DataFlash messages in the file, it is not an ArduPilot BIN log. In the survey, 54 files named `recording.bin` were JSON text instead. Pick the actual `.BIN` file from the autopilot's SD card, or use **Import** for a saved analysis. Nothing in the log can be checked, so none of the sections below apply.

## Logger set-up checks

### A1: IMU data not logged { #a1 }

**What it means.** The log has no `IMU` messages, because the IMU bit (128) of `LOG_BITMASK` is not set. This was the case in 69% of the surveyed logs, most of them with `LOG_BITMASK` 1029.

**Why it matters.** Scoring still works without it. With IMU data FCScore uses measured rotation rates and accelerations; without it, it estimates them from attitude and velocity. The measured values matter most for snaps and fast rolls. The IMU bit also switches on vibration logging, so without it [B3](#b3) cannot run.

**How to fix.** Add 128 to `LOG_BITMASK`, for example 1029 becomes 1157. See [Recommended settings](#recommended).

ArduPilot: [LOG_BITMASK](https://ardupilot.org/plane/docs/parameters.html#log-bitmask), [Logs](https://ardupilot.org/plane/docs/common-logs.html).

### A2: Attitude logged at a low rate { #a2 }

**What it means.** In the airborne part of the log, `ATT` was recorded at 18 Hz or less. With Fast attitude at the default 50 Hz scheduler loop, ATT is normally about 25 Hz.

**Why it matters.** FCScore builds the flight path and attitude from these samples. A low rate gives coarse attitude, worse rate estimates and less precise element boundaries.

**How to fix.** Set the Fast attitude bit (1) in `LOG_BITMASK` and set `LOG_FILE_RATEMAX` to `0`. In the survey, 9 of the 10 logs at or below 18 Hz had `LOG_FILE_RATEMAX` 20, which gave ATT at 12.5 Hz; the tenth had no Fast attitude. Values of 30 and 40 did no harm in the survey. `LOG_FILE_RATEMAX` does not exist in firmware 4.0 and 4.1, so its absence is not a problem.

ArduPilot: [LOG_FILE_RATEMAX](https://ardupilot.org/plane/docs/parameters.html#log-file-ratemax), [LOG_BITMASK](https://ardupilot.org/plane/docs/parameters.html#log-bitmask).

### A3: Position or EKF logged at a low rate { #a3 }

**What it means.** `XKF1` (EKF state) or `POS` was recorded at less than 18 Hz in the airborne part of the log.

**Why it matters.** Same as [A2](#a2): position and velocity are less finely sampled. In the survey these streams followed the attitude rate, so the cause is nearly always the same.

**How to fix.** As for [A2](#a2). The EKF logging settings may also be involved; this has not been verified here.

ArduPilot: [LOG_FILE_RATEMAX](https://ardupilot.org/plane/docs/parameters.html#log-file-ratemax), [LOG_BITMASK](https://ardupilot.org/plane/docs/parameters.html#log-bitmask).

### A4: GPS updates too slowly { #a4 }

**What it means.** The median time between GPS updates (`GPA.Delta`) is more than 210 ms, below about 5 Hz.

**Why it matters.** Position and velocity are anchored to the GPS. Slower updates make the track coarser.

**How to fix.** Set `GPS1_RATE_MS` (older firmware: `GPS_RATE_MS`) to 200 or lower, if the receiver supports it. ArduPilot does not allow a rate slower than 5 Hz (range 50 to 200 ms), so this check should rarely if ever fire; it never did in the survey.

ArduPilot: [GPS1_RATE_MS](https://ardupilot.org/plane/docs/parameters.html#gps1-rate-ms), [How GPS works](https://ardupilot.org/plane/docs/common-gps-how-it-works.html).

### A5: Log data was dropped in flight { #a5 }

**What it means.** The logger's count of rejected writes (`DSF.Dp`) rose while the aircraft was airborne. The count is cumulative for the file and is often non-zero from start-up, so only an increase in flight is flagged (6% of surveyed logs).

**Why it matters.** Dropped writes mean missing samples, usually in bursts. FCScore may see gaps in attitude and position during a manoeuvre.

**How to fix.** Use a fast, good-quality SD card and reformat it in the autopilot or with the SD Association formatter. Replace a card that keeps failing. Reducing what is logged (a smaller `LOG_BITMASK`) also reduces the write load. These are practical suggestions rather than ArduPilot-verified procedures, apart from the meaning of `DSF.Dp` ("number of times we rejected a write to the backend").

ArduPilot: [Log messages (DSF)](https://ardupilot.org/plane/docs/logmessages.html), [Logs](https://ardupilot.org/plane/docs/common-logs.html).

### A6: Essential data missing { #a6 }

**What it means.** The log lacks `XKF1`, `ATT`, `POS` or `ORGN`, or the EKF never reports a height above 10 m, so no flight can be found. This is an error, not a warning: the flight cannot be processed.

**Why it matters.** These messages are the basis of the analysis.

**How to fix.**

- Only `NKF` messages (EKF2) in the log: set `AHRS_EKF_TYPE` to `3` and make sure `EK3_ENABLE` is `1`. In the survey every log already had these, so this case did not occur.
- No `ORGN` or `POS`: wait for a GPS fix and the EKF origin before take-off.
- No height above 10 m: the file may not contain a flight.

ArduPilot: [AHRS_EKF_TYPE](https://ardupilot.org/plane/docs/parameters.html#ahrs-ekf-type), [EKF overview](https://ardupilot.org/plane/docs/common-apm-navigation-extended-kalman-filter-overview.html).

### A7: Log starts in the air { #a7 }

**What it means.** The first EKF height sample is more than 10 m above the origin, so the take-off is missing.

**Why it matters.** FCScore expects to see the flight from the ground. Without the take-off the start of the flight is not well defined. This never fired in the survey.

**How to fix.** Check that logging starts at arming and not part way through the flight: confirm the card was not full or removed, and see `LOG_DISARMED` (1 logs while disarmed; 2 logs while disarmed unless USB is connected). The cause of a late start has not been verified beyond this.

ArduPilot: [LOG_DISARMED](https://ardupilot.org/plane/docs/parameters.html#log-disarmed), [Logs](https://ardupilot.org/plane/docs/common-logs.html).

### A8: Log ends in the air { #a8 }

**What it means.** The last EKF height sample is more than 10 m above the origin, so the log stops before the landing (0.5% of surveyed logs).

**Why it matters.** The end of the flight, and possibly the last manoeuvre, may be missing or truncated.

**How to fix.** Possible causes are a power brown-out, a card failure or a crash. Check the power supply (see [B6](#b6)) and the SD card (see [A5](#a5)).

ArduPilot: [Diagnosing problems using logs](https://ardupilot.org/plane/docs/common-diagnosing-problems-using-logs.html) (power problems), [Powering the autopilot](https://ardupilot.org/plane/docs/common-powering-the-pixhawk.html).

## In-flight sensor checks

These look only at the airborne part of the log.

### B1: Poor GPS quality { #b1 }

**What it means.** For more than 5% of the flight, `HDop` was above 1.5 or fewer than 10 satellites were in use, or the GPS had no 3D fix (Status below 3) for more than 1% of the flight. Single bad samples are ignored.

**Why it matters.** Position and velocity come from the GPS and EKF. Poor GPS quality means position errors that show up as track and distance errors in the scores.

**How to fix.** Mount the GPS antenna away from ESCs, motors, video transmitters and carbon fibre, with a clear view of the sky. Wait for a good fix before take-off. A multi-constellation receiver may help; `GPS1_GNSS_MODE` (older firmware: `GPS_GNSS_MODE`) selects constellations, but suitable values depend on your receiver and have not been verified here.

ArduPilot: [How GPS works](https://ardupilot.org/plane/docs/common-gps-how-it-works.html), [GPS1_GNSS_MODE](https://ardupilot.org/plane/docs/parameters.html#gps1-gnss-mode).

### B2: GPS glitch { #b2 }

**What it means.** The log has a GPS glitch error (`ERR` subsystem 11, code 2), or the GPS reported horizontal accuracy (`GPA.HAcc`) jumping by more than 2 m between samples.

**Why it matters.** A glitch moves the estimated position suddenly. Manoeuvres near the glitch can show false track or position errors.

**How to fix.** As [B1](#b1): improve antenna placement and interference.

ArduPilot: [Diagnosing problems using logs](https://ardupilot.org/plane/docs/common-diagnosing-problems-using-logs.html) (GPS glitches), [How GPS works](https://ardupilot.org/plane/docs/common-gps-how-it-works.html).

### B3: High vibration or accelerometer clipping { #b3 }

**What it means.** Filtered vibration on an axis (`VibeX/Y/Z`) was above 30 m/s/s for more than 10% of the flight, or above 60 m/s/s for more than 1%, or the clipping count rose by more than 100. ArduPilot's vibration page treats below 30 as normally acceptable and above 60 as nearly always a problem. This check runs only when the log has `VIBE` messages, which need the IMU bit ([A1](#a1)).

**Why it matters.** Vibration disturbs the accelerometers the EKF uses, which degrades the velocity and attitude estimates. Clipping, where the accelerometer saturates, is worse.

**How to fix.** Soft-mount the autopilot, balance the propeller and spinner, and check the motor mount. Clipping can also come from the manoeuvre itself (snaps in particular), not only from vibration.

ArduPilot: [Measuring vibration](https://ardupilot.org/plane/docs/common-measuring-vibration.html), [Vibration damping](https://ardupilot.org/plane/docs/common-vibration-damping.html).

### B4: Compass problems { #b4 }

**What it means.** The log reports a compass error (`ERR` subsystem 3 with a non-zero code), or messages such as "switching to compass", "emergency yaw reset" or "mag anomaly", or the magnetic field strength changes by more than 30% between low and high throttle. The throttle test only runs on the minority of logs that have throttle (`CTUN`) data and a wide enough throttle range; otherwise it is not tested.

**Why it matters.** A bad compass gives a wrong heading estimate. FCScore can then see the aircraft turned the wrong way, and the heading can jump.

**How to fix.** Move the compass away from power wiring and motors, recalibrate it, and run CompassMot if the field changes with throttle.

ArduPilot: [Advanced compass setup](https://ardupilot.org/plane/docs/common-compass-setup-advanced.html), [Compass calibration in Mission Planner](https://ardupilot.org/plane/docs/common-compass-calibration-in-mission-planner.html).

### B5: EKF problems { #b5 }

**What it means.** The EKF reported a bad variance or failsafe (`ERR` subsystem 16 or 17 with a non-zero code), switched lanes (a change of the primary core, or a "lane switch" message), or had innovation test ratios above 1 for more than 20% of the flight. A ratio above 1 means measurements were being rejected.

**Why it matters.** The EKF output is the flight path FCScore scores. A lane switch can step the estimate, and rejected measurements mean the estimate is drifting from the sensors.

**How to fix.** It depends on which measurement was rejected. In the survey the magnetometer ratio was the commonest cause, so see [B4](#b4); also see [B1](#b1) (GPS) and [B3](#b3) (vibration).

ArduPilot: [EK3 affinity and lane switching](https://ardupilot.org/plane/docs/common-ek3-affinity-lane-switching.html), [EKF overview](https://ardupilot.org/plane/docs/common-apm-navigation-extended-kalman-filter-overview.html).

### B6: Power over-current { #b6 }

**What it means.** The power status flags (`POWR.Flags`) show an over-current condition (peripheral or high-power over-current) while airborne. This check runs only when the log has `POWR` messages, which need the battery monitor bit (512) of `LOG_BITMASK`. The supply voltage (Vcc) is not checked because most boards do not report it.

**Why it matters.** Power problems can reset sensors or stop logging, leaving gaps or truncated logs (see [A8](#a8)).

**How to fix.** Use a dedicated, adequate BEC for the autopilot, and power servos from a separate supply.

ArduPilot: [Powering the autopilot](https://ardupilot.org/plane/docs/common-powering-the-pixhawk.html), [Diagnosing problems using logs](https://ardupilot.org/plane/docs/common-diagnosing-problems-using-logs.html).

### B7: High CPU load { #b7 }

**What it means.** The autopilot's 95th percentile CPU load (`PM.Load`) was above 80%, or more than 1% of loops were long. This check runs only when the log has `PM` messages, which need bit 3 (8) of `LOG_BITMASK`. It is informational and does not trigger the red card on its own. It never fired in the survey (load never exceeded about 16%).

**Why it matters.** An overloaded autopilot can skip log samples and run the controller and EKF late.

**How to fix.** Disable unused features and check the loop rate (`SCHED_LOOP_RATE`).

ArduPilot: [SCHED_LOOP_RATE](https://ardupilot.org/plane/docs/parameters.html#sched-loop-rate), [Log messages (PM)](https://ardupilot.org/plane/docs/logmessages.html).

### B8: Other logged errors { #b8 }

**What it means.** The log has `ERR` records with a non-zero code in subsystems not covered above (for example failsafes, radio, barometer or crash check) while airborne. It is informational. Code 0 means "resolved" and is ignored. This never fired in the survey; a radio failsafe, for instance, appears as message text rather than `ERR`.

**Why it matters.** It tells you something else happened in flight that may have disturbed the flight or its recording.

**How to fix.** Look up the subsystem and code in the ArduPilot log message tables, and address the cause.

ArduPilot: [Log messages (ERR)](https://ardupilot.org/plane/docs/logmessages.html#err), [Diagnosing problems using logs](https://ardupilot.org/plane/docs/common-diagnosing-problems-using-logs.html).
