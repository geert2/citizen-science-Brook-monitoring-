# De Meetbeek: review notes from the groundwater sensor set

*20 November 2026. Written against the files in this repository on `main` (commit `137d432`).*

The Meetbeek set and the groundwater set share the same core (Heltec V3, TL-136 4–20 mA loop,
DS18B20, analog EC probe, raw LoRa, ESPHome, Home Assistant), so each has lessons for the other.
This note records what the groundwater set found in the Meetbeek files and what it took over.

## Scope and limits

Read: `README.md`, `docs/wiring.md`, `docs/calibration.md`, `docs/bench-test.md` and the ESPHome
files in `esphome/`. The earlier version of the three ESPHome files (the `meetbeek-corrected` zip)
also passed `esphome config` with ESPHome 2026.10.2; the files on `main` were **not** re-run.
Nothing was compiled and nothing was tested on hardware, so every point below is a review finding,
not a measurement.

## Suggested changes, most useful first

The design is sound. None of the points is a build blocker.

1. **Check the TL-136 supply at full scale.** `wiring.md` sets the booster to about 15 V and says the
   sensor then gets about 11.8 V at 20 mA across the 160 Ω shunt, with a "typical 9–12 V" minimum.
   Seller manuals for the generic TL-136 list **12–32 V** (there is no authoritative datasheet, so read
   the label on your unit). If yours needs 12 V, 11.8 V is just below it exactly where the level is
   highest. Either raise the booster to about 18 V (the groundwater set does) or use a lower shunt such
   as 120 Ω (the earlier Meetbeek version) or 100 Ω.
2. **Protect the ADS1115 input against an open shunt.** If the shunt fails open, the booster voltage
   reaches `A0` through the 1 kΩ resistor: about 11 mA at 15 V. As I remember the TI datasheet,
   continuous input current is limited to 10 mA; please verify that figure. A BAT54S clamp (one diode to
   `GND`, one to `3V3`) on `A0`, or a larger series resistor, removes the doubt.
3. **The LoRa link is plain text and unauthenticated.** The README already says so. The sync word is not
   security. Anyone on 869.525 MHz can inject a valid `B1,...` line. The QC flags catch absurd values but
   not plausible fake ones. If the data goes into open datasets, consider ESPHome's `packet_transport`
   with a per-provider key (the groundwater set uses it), or at least a shared secret field checked in
   the gateway.
4. **Check the V3.2 battery-divider default.** `vbat_ctrl_inverted: "true"` (GPIO37 LOW) is right for V3
   and V3.1. For V3.2 the Heltec update log and the RNode firmware point to HIGH, so a V3.2 board would
   read near 0 V and set the low-battery QC bit on every packet. The comment says "V3/V3.1"; the revision
   on the silkscreen decides. The Vext level on V3.2 is not confirmed either (see the open points).
5. **Measure the Vext load.** `wiring.md` powers both MT3608 boosters from Vext and cites 350 mA for the
   V3. I could not verify that rating, and the margin in your own estimate is not large. Measure the
   current as the guide suggests. If it is too close, the groundwater set now switches the booster input
   from the battery with an AO3401 P-MOSFET driven by a 2N7002 (one GPIO, 100 kΩ pull-down), which keeps
   the loop current off the 3.3 V regulator.
6. **Verify the packet counter on the bench.** `static RTC_DATA_ATTR uint32_t seq` inside a lambda should
   survive deep sleep, but it has not been compiled or run. Watch the log over several sleep cycles and
   confirm the counter rises by one each time and restarts only after a power loss.
7. **Use a real air temperature for the speed of sound.** The gateway uses the water temperature as a
   proxy. A BME280 at the stream node (air temperature, and enclosure humidity for the desiccant) would
   remove that approximation; the groundwater set carries one.
8. **State the frequency rules with their source.** 869.525 MHz in the 869.4–869.65 MHz sub-band (10 %
   duty cycle, higher power than 868.0–868.6 MHz) is a good choice. I could only check the limits through
   secondary sources, not the CEPT text itself, so cite the regulation in the README.

## Repository housekeeping

These were found while reading the repository on GitHub. They are separate from the design.

* **`esphome/secrets.yaml` is tracked and is not a secrets file.** It is an identical copy of
  `esphome/brook-Gateway.yaml`, an early gateway configuration that contains a literal
  `encryption_key`. The repository is public, so treat that key as exposed: do not reuse it, and note
  that deleting the file does not remove it from the git history. Remove it from tracking (`git rm`)
  and keep your real `secrets.yaml` local.
* **`gitignore.txt` should be `.gitignore`.** Under the current name git ignores nothing, so
  `secrets.yaml` is not protected. (Uploading through the GitHub web page often drops dotfiles.)
* **`brook-Gateway.yaml` and `brook_gateway.yaml`** differ in their name and nothing else suggests which
  is current. The old one uses `lora:` and `lora_receiver:`, which are not ESPHome components; delete it
  once nothing refers to it.
* **`home-assistant/configuration.yaml`** reads the topic `brook/sensor_node/data`, which the current
  gateway does not appear to publish (its MQTT prefix is `brook/gateway`, and Home Assistant receives
  the data through the ESPHome API). It looks like it belongs to the old design.

## Side by side

The two sets measure different things, so the differences follow the water body: a brook has fast
events, a well changes slowly.

| Topic | Meetbeek (brook) | Groundwater set (well) |
| --- | --- | --- |
| Measures | level, temperature, EC, turbidity, ultrasonic level, air quality | water column, EC, temperature, BME280 |
| Interval | 5 min | 60 min (setting `sleep_minutes`) |
| Awake per cycle | about 12–15 s | about 3 s |
| Power | 2×18650 in parallel, CN3791 MPPT, 12 V panel | one 18650, no panel |
| ADC | ADS1115 for all analog inputs | ESP32 ADC by default, ADS1115 optional |
| Shunt | 160 Ω (3.2 V at 20 mA) | 100 Ω (160 Ω works up to about 4.8 m with the ESP32 ADC) |
| Boost converters | two MT3608 (about 15 V and 5 V), input from Vext | one MT3608 (18 V), input from the battery through a MOSFET switch (now) |
| LoRa | 869.525 MHz, SF9, CR 4/6, 10 % duty cycle | 868.1 MHz, SF9, CR 4/5, 1 % duty cycle |
| Payload | own ASCII line `B1,...`, sent twice, plain text | `packet_transport`, one frame, encrypted |
| Calibration | in the gateway, node sends raw volts | in the gateway (now), node sends raw volts |
| Quality control | QC flag bits, lost and reset counters | same (now), plus a low-battery guard |
| Cloud | MQTT, sensor.community | openSenseMap |

## What the groundwater set took from Meetbeek

Four ideas are now in the groundwater repository (change log: its `docs/CHANGES.md`):

* **Calibration in the gateway.** The node sends raw shunt and EC voltages; shunt value, zero, span and
  EC calibration are gateway constants, so recalibrating needs no visit to the well.
* **Packet counter with loss and reset counters.** The gateway counts gaps and counter restarts per well.
* **QC flag bits** per well, plus an EC upper limit above which the value is not published or uploaded.
* **MOSFET switch for the booster** on `GPIO7`, with the input taken from the battery instead of `Vext`.

Not taken over: the duplicate transmission, the ultrasonic cross-check, the turbidity sensor and the
869.525 MHz sub-band. The first three do not fit a well; the frequency stays at 868.1 MHz for now.

## Still to verify on hardware

- [ ] Vext enable level on a V3.2 board (the V3.2 changed Vext to an LDO; polarity not confirmed).
      Measure `Ve` against `GND` while awake.
- [ ] GPIO37 polarity for your board revision (V3 and V3.1 LOW, V3.2 HIGH).
- [ ] Real deep-sleep current of the node (a few hundred µA is plausible; 0.2 mA is optimistic).
- [ ] Packet counter survives deep sleep and restarts only after a power loss.
- [ ] Settling time of the TL-136 loop after the booster starts.
- [ ] Supply voltage at the TL-136 terminals at 20 mA (see point 1).
- [ ] Actual LoRa frame size and airtime for the `B1,...` line.
- [ ] A real `esphome compile`.

*Sources: the Meetbeek files listed above and `docs/REFERENCES.md` of the groundwater repository.*
