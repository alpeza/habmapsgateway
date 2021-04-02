# habmapsgateway

Librería para el uso de habmaps


```
from habmaps import MapTracker,HabMapsMessage

mt = MapTracker.MapTracker(id="default-station-id",
                           mqtt_url="localhost",
                           mqtt_port=1883,
                           user='habmaps',
                           password='root')
```