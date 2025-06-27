# export_sensors.py
sensors = [e for e in hass.states.all() if e.entity_id.startswith("sensor.")]

sensor_data = []
for s in sensors:
    sensor_data.append({
        "entity_id": s.entity_id,
        "state": s.state,
        "attributes": s.attributes,
    })

path = hass.config.path("www/sensors_export.json")
with open(path, "w") as f:
    import json
    json.dump(sensor_data, f, indent=2)
