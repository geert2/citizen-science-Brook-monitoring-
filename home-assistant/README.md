# Home Assistant (brook lite)

* `dashboard-card.yaml` - Lovelace card: gauges for water level, water temperature and EC, node health, a 48-hour graph for storm events and 7-day graphs.

The **gateway** calculates the *Water Level* on the staff gauge itself and exposes an editable **Sensor Height Above Gauge Zero** number. If you move or re-hang the probe, measure the new height and change that number in Home Assistant (Settings > Devices > Brook Lite Gateway); no reflashing is needed.

Entities (prefix `Brook`):

| Entity | Meaning |
| :-- | :-- |
| `Water Level` | metres on the staff gauge (water above sensor + sensor height above gauge zero) |
| `Water Above Sensor` | water above the TL-136, as measured |
| `Water Temperature` | DS18B20 next to the probe |
| `Electrical Conductivity` | EC at 25 °C (µS/cm), compensated with the DS18B20 |
| `Air Temperature`, `Air Humidity`, `Air Pressure` | BME280 in the radiation shield on the bank |
| `Battery Voltage` | node battery (diagnostic) |
| `Node Online` | false after 35 min without a packet |
| `Sensor Dry` | water level at or below the TL-136 |
| `Level Above Sensor Range` | the TL-136 is at the top of its 0-2 m range; the real level may be higher |

Useful automations:
* "Water Level above *x* m" (your local flood warning level from the staff gauge)
* "Water Level rose more than 0.2 m in 1 hour" (use a *derivative* helper on *Water Level*)
* "Node Online turns off for 10 minutes", "Battery Voltage below 3.5 V"
