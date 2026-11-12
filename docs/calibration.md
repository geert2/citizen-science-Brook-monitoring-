# 🧪 Sensor Calibration Guide

## TL-136 (Water Level)
### Steps
1. Submerge in **0cm** of water → should read **~0.64V** (4mA × 160Ω).
2. Submerge in **100cm** → should read **~3.20V** (20mA × 160Ω).
3. Formula: `level_m = (V - 0.64) / 2.56`.

## SEN0189 (EC)
### Steps
1. Distilled water (0 µS/cm) → note `V0`.
2. 1413 µS/cm solution → note `V1413`.
3. Formula: `EC = (1413 / (V1413 - V0)) * (V - V0)`.

## Turbidity
### Steps
1. Distilled water (0 NTU) → note `V0`.
2. 100 NTU solution → note `V100`.
3. Formula: `NTU = (100 / (V100 - V0)) * (V - V0)`.

## JSN-SR04T (Ultrasonic)
### Steps
1. Measure **mount height** from sensor to water at 0m.
2. Update `mount_height` in YAML.
3. Temperature compensation: `speed_of_sound = 331 + 0.6 * T` (m/s).
