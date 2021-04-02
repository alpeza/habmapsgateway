# habmaps

Librería para el uso de habmaps

## Quick Start

1.- Instalamos el cliente de habmaps con

```
pip3 install habmaps
```

2.- Envíamos información a la plataforma

```python
from habmaps import MapTracker, HabMapsMessage
import time

mt = MapTracker.MapTracker(id="default-station-id",
                           mqtt_url="localhost",
                           mqtt_port=1883,
                           user='habmaps',
                           password='root')

mt.startAlive() #Iniciamos la señal de alive que se enviará cada n minutos 

while True:
    mt.sendHabMessage(HabMapsMessage.HabMapsMessage(
        TimeStamp='2021-04-02 15:33:43',
        HabId='Mi-Hab',
        BasestationId='Mi-Estacion-base',
        HabPosition=[5, 3],
        Signals={
            "miSensorUno": 122.4,
            "miSensorDos": 400.5
        },
        BasestationPosition=[5, 3]))
    time.sleep(5)
```

## Logging

Para configurar los logs

```
export HABLIB_LOGLEVEL=DEBUG #INFO,ERROR
export HABLIB_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```