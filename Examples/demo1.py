from habmapslib import MapTracker,HabMapsMessage

hm = HabMapsMessage.HabMapsMessage()
mt = MapTracker.MapTracker(id="default-station-id",
                           mqtt_url="localhost",
                           mqtt_port=1883,
                           user='habmaps',
                           password='root')

# Añadimos información del globo
hm.setTimeStamp("2021-04-02 15:33:43")
hm.setHabId('Mi-Hab')
hm.setBasestationId('Mi-Estacion-base')
hm.setHabPosition([5,3])
hm.setBasestationPosition([5,3])
# Añadimos información de los sensores
hm.addSignal('miSensorUno',12.5)   # -> Optional
hm.addSignal('miSensorDos',12.4)

print(hm.isValidMessage())
hm.printMessage()