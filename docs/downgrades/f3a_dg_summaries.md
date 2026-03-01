## LINE

| name            | measure                 | visibility       | selectors      | criteria        | last                                 | this        | next                     |
|:----------------|:------------------------|:-----------------|:---------------|:----------------|:-------------------------------------|:------------|:-------------------------|
| roll_angle      | roll_angle              | roll_angle       | last           | Single          | NONE                                 | LINE        | ANY                      |
| track_y         | rf_y_track              | vector_direction | last           | Single          | NONE                                 | LINE        | !SPIN                    |
| track_z         | rf_z_track              | vector_direction | last           | Single          | NONE                                 | LINE        | !SPIN                    |
| roll_angle      | roll_angle              | roll_angle       |                | Continuous      | !NONE                                | LINE, !ROLL | ANY                      |
| downwind_yaw    | downwind_attitude_error | vector_direction | take_end       | Continuous      | NONE                                 | LINE        | SPIN                     |
| excessive_yaw   | upwind_attitude         | vector_direction | take_end       | Peak            | NONE                                 | LINE        | SPIN                     |
| initial_track_y | rf_y_track              | vector_direction | take_end,first | Single          | NONE                                 | LINE        | SPIN                     |
| initial_track_z | rf_z_track              | vector_direction | take_end,first | Single          | NONE                                 | LINE        | SPIN                     |
| track_y         | rf_y_track              | vector_direction | take_end       | Continuous      | NONE                                 | LINE        | SPIN                     |
| upwind_track    | upwind_track_error      | vector_direction | take_end       | Continuous      | NONE                                 | LINE        | SPIN                     |
| roll_rate       | roll_rate               | roll_rate        |                | Deviation       | ANY                                  | LINE, ROLL  | ANY                      |
| roll_angle      | roll_angle              | roll_angle       | last           | Single          | ANY                                  | LINE, ROLL  | ANY                      |
| speed           | speed                   | vector_direction |                | ContinuousValue | !SPIN, !STALLTURN, !TAILSLIDE, !NONE | LINE / LOOP | !SPIN, !STALLTURN, !NONE |
| track_y         | rf_y_track              | vector_direction |                | Continuous      | !SPIN, !STALLTURN, !TAILSLIDE, !NONE | LINE        | !SPIN, !STALLTURN, !NONE |
| track_z         | rf_z_track              | vector_direction |                | Continuous      | !SPIN, !STALLTURN, !TAILSLIDE, !NONE | LINE        | !SPIN, !STALLTURN, !NONE |

## LOOP

| name             | measure                   | visibility       | selectors   | criteria   | last   | this        | next   |
|:-----------------|:--------------------------|:-----------------|:------------|:-----------|:-------|:------------|:-------|
| axial_track      | loop_axial_track          | vector_direction |             | Continuous | ANY    | LOOP        | ANY    |
| curvature        | curvature                 | loop_rate        |             | Deviation  | ANY    | LOOP        | ANY    |
| inst_radius      | instantanious_radius      | loop_rate        |             | Total      | ANY    | LOOP        | ANY    |
| roll_angle       | roll_angle_p              | roll_angle       |             | Continuous | ANY    | LOOP, !ROLL | ANY    |
| roll_angle       | roll_angle_p              | roll_angle       | last        | Single     | ANY    | LOOP, ROLL  | ANY    |
| roll_rate        | roll_rate                 | roll_rate        |             | Deviation  | ANY    | LOOP, ROLL  | ANY    |
| radial_track     | loop_radial_track         | vector_direction | last        | Single     | ANY    | LOOP        | ANY    |
| radius           | radius_curve_fit          | loop_shape       |             | Deviation  | ANY    | LOOP        | ANY    |
| roll_integration | rolling_circle_roll_track | roller_track     |             | Continuous | ANY    | LOOP, ROLL  | ANY    |

## SNAP

| name             | measure           | visibility   | selectors     | criteria   | last   | this   | next   |
|:-----------------|:------------------|:-------------|:--------------|:-----------|:-------|:-------|:-------|
| break_pitch_rate | pitch_rate        | pitch_rate   | autorot_break | Bounded    | ANY    | SNAP   | ANY    |
| peak_break_pr    | pitch_rate        | pitch_rate   | autorot_break | AbsTrough  | ANY    | SNAP   | ANY    |
| alpha            | alpha             | pitch_rate   | autorotation  | Bounded    | ANY    | SNAP   | ANY    |
| snap_rate        | autorotation_rate | roll_rate    | autorotation  | Bounded    | ANY    | SNAP   | ANY    |

## SPIN

| name            | measure         | visibility   | selectors       | criteria   | last         | this        | next   |
|:----------------|:----------------|:-------------|:----------------|:-----------|:-------------|:------------|:-------|
| drop_pitch_rate | pitch_down_rate | pitch_rate   | autorot_break   | Bounded    | !SPIN        | SPIN        | ANY    |
| inst_rotation   | inst_roll       | roll_angle   | after_break     | Total      | !SPIN, !SNAP | SPIN / SNAP | ANY    |
| inst_rotation   | inst_roll       | roll_angle   |                 | Total      | SPIN, SNAP   | SPIN / SNAP | ANY    |
| peak_drop_pr    | pitch_down_rate | pitch_rate   | autorot_break   | AbsTrough  | !SPIN        | SPIN        | ANY    |
| alpha           | spin_alpha      | pitch_rate   | before_recovery | Bounded    | ANY          | SPIN        | ANY    |
| turns           | roll_angle_y    | roll_angle   | last            | Single     | ANY          | SPIN / SNAP | ANY    |

## STALLTURN

| name              | measure                     | visibility       | selectors   | criteria   | last   | this      | next   |
|:------------------|:----------------------------|:-----------------|:------------|:-----------|:-------|:----------|:-------|
| exit_groundspeed  | stallturn_exit_ground_speed | vector_direction | last        | Single     | ANY    | STALLTURN | ANY    |
| height_over_end   | stallturn_height_over_end   | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |
| height_over_start | stallturn_height_over_start | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |
| roll_angle        | roll_angle_z                | roll_angle       |             | Continuous | ANY    | STALLTURN | ANY    |
| width             | stallturn_width             | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |

## TAILSLIDE



## ROLL

| name      | measure   | visibility   | selectors   | criteria   | last   | this   | next   |
|:----------|:----------|:-------------|:------------|:-----------|:-------|:-------|:-------|
| inst_roll | inst_roll | roll_angle   |             | Total      | ANY    | ROLL   | ANY    |

