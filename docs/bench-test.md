# Bench test checklist

Test everything on the desk, one step at a time, before building the enclosure. If a step
fails, fix it before continuing.

## A. Software
- [ ] `cp esphome/secrets.yaml.example esphome/secrets.yaml` and fill in your values.
- [ ] `esphome config esphome/brook_gateway.yaml` says *Configuration is valid* (same for the node and the air node).
- [ ] Flash the **gateway** by USB (antenna attached!). In the log you see Wi-Fi connected.
- [ ] The gateway appears in Home Assistant (Settings → Devices).

## B. Radio link (no sensors yet)
- [ ] Flash the **node** by USB with the antenna attached. Set `sleep_time: 15s` for testing.
- [ ] Node log shows `TX: B1,1,...` lines, with the counter increasing.
- [ ] Gateway log shows `seq 1 level ... flags ...` lines.
- [ ] Home Assistant shows **Node Online = on**, an RSSI value (stronger than about −100 dBm),
      and **Readings Lost = 0**.
- [ ] Unplug the node's USB for a minute: **Node Online** switches off after 20 minutes
      (shorten `offline_after_ms` to test).

## C. Sensors, one by one (values from the node log, `-999` = not connected)
- [ ] **Battery:** `vbat` matches a multimeter within about 0.1 V.
- [ ] **DS18B20:** water temperature is plausible (room temperature in air; warms in your hand).
- [ ] **TL-136:** in air the loop voltage is about 0.48 V (4 mA × 120 Ω). Lifting the probe
      out of water returns it there. Under about 3.6 mA means a wiring fault.
- [ ] **Loop booster:** measure the booster output (about 15 V) before connecting the sensor,
      and the supply at the sensor terminals (should be at least the sensor's minimum, with
      the loop at 20 mA). With a 120 Ω shunt and 15 V expect about 12.6 V; under 12 V see
      wiring.md section 2.
- [ ] **SEN0244 (EC):** voltage in distilled water is near zero and rises in tap water
      (tap water is typically a few hundred µS/cm, giving roughly 0.6–1.0 V). A stronger
      solution (1413 µS/cm, about 1.7 V) gives a higher voltage.
- [ ] **SEN0189 (turbidity):** clear water gives the highest voltage (about 4 V on the sensor side).
      Stirring a pinch of fine soil into the water lowers it.
- [ ] **Ultrasonic:** distance matches a tape measure at 0.3, 0.5 and 1.0 m.

## D. Power
- [ ] Measure the awake current and the sleep current with a multimeter in series with the battery.
      Compare with the estimates in `wiring.md` and update them.
- [ ] After a full cycle the boosters are off (measure the 15 V and 5 V rails while the node sleeps: 0 V).
- [ ] Vext switching: with a multimeter on the Vext pin, it reads 3.3 V while measuring and 0 V while the node sleeps.
- [ ] Booster input current (multimeter in series) stays well under 350 mA, and the node log shows no brownout resets.
- [ ] (Only if you built Option B or C from `wiring.md`: test the switch on its own before connecting the boosters.)
- [ ] Battery protection works: the cells are in parallel and the fuse is fitted.

## E. Air node
- [ ] Serial log shows the I2C scan finding the BME280 (0x76 or 0x77).
- [ ] PM2.5 / PM10 appear in Home Assistant after the first interval.
- [ ] The log shows `sensor.community (SDS011) HTTP 200` (a 4xx error means the sensor ID is
      not registered or the format is wrong).

## F. Outdoors
- [ ] Walk-test the radio range with the node at the final place before gluing anything.
- [ ] Watch **Readings Lost** and **Node Resets** for a week before trusting the data.
