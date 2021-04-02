from habmaps import MapTracker, HabMapsMessage
import time

mt = MapTracker.MapTracker(id="hb-basestation-1",
                           mqtt_url="localhost",
                           mqtt_port=1883,
                           user='habmaps',
                           password='root')
mt.startAlive()

while True:
    mt.sendHabMessage(HabMapsMessage.HabMapsMessage(
        TimeStamp='2021-04-02 15:33:43',
        HabId='Mi-Hab',
        HabPosition=[5, 3],
        Signals={
            "miSensorUno": 122.4,
            "miSensorDos": 400.5
        },
        BasestationPosition=[5, 3]))
    time.sleep(5)