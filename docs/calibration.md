# Calibration

**Where the numbers go:** the node sends *raw* volts and distances. The calibration constants
live in the `substitutions:` block at the top of `esphome/brook_gateway.yaml`. After editing
them, re-flash the gateway (over Wi-Fi). The node at the stream never has to be touched.
Raw voltages stay visible in Home Assistant, so old data can be recalculated later.

Until you have entered your own EC and turbidity calibration, the **QC Flags** value includes
bit 64 (EC) and bit 128 (turbidity), so uncalibrated data is never mistaken for calibrated data.
When you are done, set `ec_calibrated: "1"` and `ntu_calibrated: "1"`.

**How to read the raw values during calibration:** connect the node by USB and run
`esphome logs brook_sensor_node.yaml`. Each wake-up prints a line such as
`TX: B1,17,3.912,14.20,1.2013,0.8044,2.0310,0.498`. The fields are
`B1, counter, battery V, water °C, loop V, EC sensor V, turbidity V (after the divider), distance m`.
For faster testing temporarily set `sleep_time: 15s`.

## 1. TL-136 level sensor (4–20 mA)

1. Measure the shunt resistor with a multimeter, set `tl136_shunt_ohm`.
2. Set `tl136_range_m` to the sensor's full-scale range (datasheet, e.g. 1.0 for 0–1 m).
3. With the sensor in air (or at your zero level) the loop current should be about 4 mA
   (`Level Loop Current` in Home Assistant, 0.64 V across the 160 Ω shunt). A reading below
   3.6 mA means a broken wire.
4. Put the sensor at a known depth (bucket + ruler, or the stream staff gauge). Compare and
   set `tl136_zero_offset_m` = true level − displayed level.
5. Repeat at a second depth to confirm the scale is right. If the error grows with depth,
   re-check the range.

Formula used: `level = (mA − 4) / 16 × range + offset`.

## 2. Ultrasonic (JSN-SR04T)

1. Define a zero level (the zero of a staff gauge or a marked post).
2. Measure from the sensor face down to that zero with a ruler: `us_mount_height_m`.
3. Compare at 2–3 water levels. Adjust `us_zero_offset_m`.
4. The speed of sound is corrected automatically using the water temperature as a stand-in
   for the air temperature (error at most about 1 cm at 50 cm distance).

The ultrasonic reading and the TL-136 should agree. A growing difference between them is an
early warning that one sensor is drifting or fouled.

## 3. Electrical conductivity (SEN0244 TDS/EC sensor)

The SEN0244 has a curved (cubic) response. The gateway uses DFRobot's published curve and
compensates the voltage to 25 °C with the live water temperature. One **calibration factor**
`ec_k_factor` then corrects your individual probe. The result is EC at 25 °C in µS/cm.

You need one standard solution of **1413 µS/cm** (at 25 °C). A second standard (for example
147 µS/cm or 2764 µS/cm) is useful as a check. Do not use distilled water as a reference: it
absorbs CO₂ and drifts.

1. Rinse the probe with distilled water, then put it in the 1413 µS/cm standard together with
   the DS18B20 (same temperature). Stir gently and wait 1–2 minutes until the logged `v_ec`
   is stable.
2. Write down the **voltage** `v_ec` and the **temperature** `T` (°C).
3. Compute the compensated voltage and the curve value:

   ```
   vc   = v_ec / (1 + 0.02 × (T − 25))
   poly = 133.42 × vc³ − 255.86 × vc² + 857.39 × vc
   k    = 1413 / poly
   ```

4. Put `k` in `ec_k_factor`, set `ec_calibrated: "1"`, re-flash the gateway.

**Worked example:** `v_ec = 1.65 V` at `T = 20 °C` gives `vc = 1.833`, `poly = 1534`,
so `k = 1413 / 1534 = 0.92`.

A healthy probe gives `k` between about 0.8 and 1.2. Check with the second standard:
the gateway value should be within about ±10 % (the sensor's own specification). A much larger
error means a dirty or worn probe.

Repeat **every 3 months** and after cleaning or replacing the probe. Keep the probe tip clean
(soft brush, no scratching).

## 4. Turbidity (relative index)

The DFRobot sensor is only a rough instrument. It is poor below about 50 NTU, so treat the
values as a **relative index** and as an event detector (storm runoff), not as a lab
measurement. Its output voltage *falls* as the water gets cloudier.

1. Mount it in its final (shaded) housing.
2. In clean water (tap or bottled, no bubbles) note the sensor voltage `turb_raw_v`
   → `ntu_cal_v_clear`.
3. Repeat in a **reference standard** (for example a 100 NTU commercial standard such as
   StablCal; formazin is hazardous, avoid it). Note the voltage → `ntu_cal_v_ref`
   and the standard's value → `ntu_cal_ref`.
4. `ntu_divider` is the divider ratio on the node (2.0 for two equal resistors).

Formula: `NTU = ref × (V_clear − V) / (V_clear − V_ref)`, clipped at 0.

Clean the lens **weekly** at first (biofilm, algae, silt). Record the clean voltage each
time: a steady drop in the clear-water voltage shows drift.

## 5. Battery voltage

Measure the battery with a multimeter and compare with `Node Battery`. If they disagree,
adjust `vbat_divider` in the **node** file (default 4.9). If the value is near zero, set
`vbat_ctrl_inverted` to `"false"`.

## Calibration log

Keep a record in the repo (a table or CSV) so every dataset can be traced to a calibration.

| Date | Sensor | Standard / reference | Raw value | Temp (°C) | Constants changed | Who |
|------|--------|----------------------|-----------|-----------|-------------------|-----|
|      |        |                      |           |           |                   |     |

## Field checks (monthly)

* Staff gauge or ruler vs both level sensors.
* Handheld conductivity meter vs the EC value.
* Photograph the sensors (fouling) and note the cleaning date.
