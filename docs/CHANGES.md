# Changes

## `lite` branch: first version (23 November 2026)
A simple brook station as a first step towards the full station on `main`. It is the groundwater lite design (`Groundwater-citizen-science-sensors-with-Lora-and-Home-Assistant-`, branch `lite`), adapted to a brook:

* **Level:** TL-136 with a **0-2 m** range (`range_m`), 100 Ω shunt, ESP32 ADC. The gateway reports *Water Level* on the staff gauge = water above sensor + editable *Sensor Height Above Gauge Zero*. New flags: *Sensor Dry* and *Level Above Sensor Range*.
* **Interval:** 10 minutes (was 60 for groundwater); low-battery sleep 2 h; *Node Online* timeout 35 min.
* **Radio:** 869.525 MHz (10 % duty-cycle sub-band), as on `main`.
* **BME280:** air temperature, humidity **and pressure** (pressure is measured anyway, and helps to spot a blocked vent tube).
* **EC:** DFRobot SEN0244 with two-point calibration; not uploaded while the sensor is dry.
* **openSenseMap:** six values per station.
* **Docs:** field guide rewritten for a brook (stilling pipe, staff gauge, permission, flood checks, monthly cleaning, power budget at 10 minutes), BOM (2 × 18650 in parallel, stilling pipe, conduit, post, staff gauge), new installation diagram.
* Includes the two compile fixes found in the groundwater repo (`random_uint32()`, `token.c_str()`).
* The full station files of `main` are not on this branch.
* Validated with ESPHome 2026.11.0: `esphome config` and `esphome compile` pass in CI for the node and the gateway. Not tested on hardware.
