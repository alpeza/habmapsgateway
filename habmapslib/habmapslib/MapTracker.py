import paho.mqtt.client as mqtt
import sched
import time
import threading
import os
import json
import logging
import traceback
from datetime import datetime, timedelta
from . import GPSAppender
from . import ConfHandler
LOGLEVEL = os.environ.get('HABLIB_LOGLEVEL', 'INFO').upper()
FORMATTER = os.environ.get(
    'HABLIB_FORMAT', '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
LOGFILE = os.environ.get('HABLIB_LOGFILE', '/tmp/hablibclient.log')
logging.basicConfig(level=LOGLEVEL, format=FORMATTER, handlers=[
                    logging.FileHandler(LOGFILE), logging.StreamHandler()])


class MapTracker(object):
    """Cliente de MQTT para maptracker"""

    def __init__(self, bid="default-station-id",
                 mqtt_url="localhost",
                 mqtt_port=1883,
                 publish="hablistener",
                 alive=60,
                 user='habmaps',
                 password='root'):
        super(MapTracker, self).__init__()
        logging.info("Starting new MapTracker Client ...")
        self.client = mqtt.Client()
        self.client.username_pw_set(username=user, password=password)

        self.mqtt_url = mqtt_url
        self.mqtt_port = mqtt_port
        self.topic = publish
        self.bid = bid
        self.alive = alive
        self.gpsAppender = GPSAppender.GPSAppender(ConfHandler.ConfHandler(
            file=os.environ.get('CONF_FILE')).getConfig())

        self.s = sched.scheduler(time.time, time.sleep)

        self.alive_flag = False

    def sendAliveMessage(self):
        lastGpsLine = [-1, -1, -1]
        try:
            lastGpsLine = self.gpsAppender.getValueAsArray()
        except Exception as e:
            logging.error(
                "Error al obtener la posición gps de la traza de status " + str(e))

        msg = {
            "type": "health",
            "ftime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bid": self.bid,
            "pos": {
                "lat": lastGpsLine[0],
                "lon": lastGpsLine[1]
            }
        }
        logging.debug(msg)
        self.sendMessage(msg)

    def _runIamAlive(self):
        logging.info("Sending Alive Message ...")
        self.sendAliveMessage()
        self.s.enter(self.alive, 1, self._runIamAlive)

    def _runAlive(self):
        logging.info("Starting health signal ...")
        self.s.enter(self.alive, 1, self._runIamAlive)
        self.s.run()

    def startAlive(self):
        logging.info("Iniciando señal de alive")
        threading.Timer(1, self._runAlive).start()

    def sendMessage(self, message):
        logging.info("Sending message ...")
        logging.debug(json.dumps(message))
        try:
            self.client.connect(self.mqtt_url, self.mqtt_port, 60)
            self.client.publish(self.topic, json.dumps(message))
            self.client.disconnect()
            return {"isOK": True, "reason": ""}
        except Exception as e:
            logging.error(e)
            logging.error(traceback.format_exc())
            return {"isOK": False, "reason": str(e)}

    def sendHabMessage(self, hm):
        hm.setBasestationId(self.bid)
        if hm.isValidMessage() == False:
            raise ValueError("Please inform all required data")
        return self.sendMessage(hm.getMessage())
