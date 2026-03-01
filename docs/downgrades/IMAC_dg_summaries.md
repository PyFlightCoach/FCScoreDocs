## LINE

| name             | measure       | visibility       | selectors   | criteria   | last                   | this        | next                   |
|:-----------------|:--------------|:-----------------|:------------|:-----------|:-----------------------|:------------|:-----------------------|
| entry_roll_angle | roll_angle    | roll_angle       | first       | Single     | NONE                   | LINE        | ANY                    |
| entry_track_y    | rf_y_track    | vector_direction | first       | Single     | NONE                   | LINE        | ANY                    |
| entry_track_z    | rf_z_track    | vector_direction | first       | Single     | NONE | STALLTURN       | LINE        | ANY                    |
| yaw              | rf_z_attitude | vector_direction | first       | Single     | TAILSLIDE              | LINE        | ANY                    |
| roll_angle       | roll_angle    | roll_angle       |             | Continuous | ANY                    | LINE, !ROLL | ANY                    |
| roll_rate        | roll_rate     | roll_rate        |             | Deviation  | ANY                    | LINE, ROLL  | ANY                    |
| roll_angle       | roll_angle    | roll_angle       | last        | Single     | ANY                    | LINE, ROLL  | ANY                    |
| track_y          | rf_y_track    | vector_direction |             | Continuous | !STALLTURN, !TAILSLIDE | LINE        | !STALLTURN, !TAILSLIDE |
| track_z          | rf_z_track    | vector_direction |             | Continuous | !TAILSLIDE             | LINE        | !TAILSLIDE             |

## LOOP

| name         | measure              | visibility       | selectors   | criteria   | last   | this        | next          |
|:-------------|:---------------------|:-----------------|:------------|:-----------|:-------|:------------|:--------------|
| axial_track  | loop_axial_track     | vector_direction |             | Continuous | ANY    | LOOP        | ANY           |
| curvature    | curvature            | loop_rate        |             | Deviation  | ANY    | LOOP        | ANY           |
| inst_radius  | instantanious_radius | loop_rate        |             | Total      | ANY    | LOOP        | ANY           |
| roll_angle   | roll_angle_p         | roll_angle       |             | Continuous | ANY    | LOOP, !ROLL | ANY           |
| roll_angle   | roll_angle_p         | roll_angle       | last        | Single     | ANY    | LOOP, ROLL  | ANY           |
| roll_rate    | roll_rate            | roll_rate        |             | Deviation  | ANY    | LOOP, ROLL  | ANY           |
| radial_track | loop_radial_track    | vector_direction | last        | Single     | ANY    | LOOP        | !LOOPSEQUENCE |
| radius       | radius_curve_fit     | loop_shape       |             | Deviation  | ANY    | LOOP        | ANY           |

## SNAP

| name             | measure           | visibility   | selectors     | criteria   | last   | this   | next   |
|:-----------------|:------------------|:-------------|:--------------|:-----------|:-------|:-------|:-------|
| break_pitch_rate | pitch_rate        | pitch_rate   | autorot_break | Bounded    | ANY    | SNAP   | ANY    |
| peak_break_pr    | pitch_rate        | pitch_rate   | autorot_break | AbsTrough  | ANY    | SNAP   | ANY    |
| alpha            | alpha             | pitch_rate   | autorotation  | Bounded    | ANY    | SNAP   | ANY    |
| snap_rate        | autorotation_rate | roll_rate    | autorotation  | Bounded    | ANY    | SNAP   | ANY    |

## SPIN

| name            | measure         | visibility   | selectors       | criteria   | last   | this        | next   |
|:----------------|:----------------|:-------------|:----------------|:-----------|:-------|:------------|:-------|
| drop_pitch_rate | pitch_down_rate | pitch_rate   | autorot_break   | Bounded    | ANY    | SPIN        | ANY    |
| inst_rotation   | inst_roll       | roll_angle   | after_break     | Total      | !SPIN  | SPIN | SNAP | ANY    |
| peak_drop_pr    | pitch_down_rate | pitch_rate   | autorot_break   | AbsTrough  | ANY    | SPIN        | ANY    |
| alpha           | spin_alpha      | pitch_rate   | before_recovery | Bounded    | ANY    | SPIN        | ANY    |
| turns           | roll_angle_y    | roll_angle   | last            | Single     | ANY    | SPIN | SNAP | ANY    |

## STALLTURN

| name              | measure                     | visibility       | selectors   | criteria   | last   | this      | next   |
|:------------------|:----------------------------|:-----------------|:------------|:-----------|:-------|:----------|:-------|
| exit_groundspeed  | stallturn_exit_ground_speed | vector_direction | last        | Single     | ANY    | STALLTURN | ANY    |
| height_over_end   | stallturn_height_over_end   | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |
| height_over_start | stallturn_height_over_start | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |
| roll_angle        | roll_angle_z                | roll_angle       |             | Continuous | ANY    | STALLTURN | ANY    |
| width             | stallturn_width             | vector_direction |             | Peak       | ANY    | STALLTURN | ANY    |

## TAILSLIDE

| name            | measure                | visibility       | selectors   | criteria   | last   | this      | next   |
|:----------------|:-----------------------|:-----------------|:------------|:-----------|:-------|:----------|:-------|
| radial_attitude | rf_y_attitude          | vector_direction | last        | Single     | ANY    | TAILSLIDE | ANY    |
| roll_angle      | roll_angle_y           | roll_angle       |             | Continuous | ANY    | TAILSLIDE | ANY    |
| tailslide_drop  | tailslide_drop         | vector_direction |             | Trough     | ANY    | TAILSLIDE | ANY    |
| axial_attitude  | rf_y_attitude_parallel | vector_direction |             | Continuous | ANY    | TAILSLIDE | ANY    |

## ROLL

| name      | measure   | visibility   | selectors   | criteria   | last   | this   | next   |
|:----------|:----------|:-------------|:------------|:-----------|:-------|:-------|:-------|
| inst_roll | inst_roll | roll_angle   |             | Total      | ANY    | ROLL   | ANY    |

