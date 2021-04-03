from . import Appender

class GPSAppender(Appender.Appender):
    """docstring for GPSAppender."""
    def __init__(self, chandler):
        super(GPSAppender, self).__init__()
        self.path = chandler.getConfig()['basestation']['appenders']['gpsappender']

    def readValue(self):
        if self.path == '':
            return {
                'lat': 0.0,
                'lon': 0.0,
                'height': 0.0
            }
        try:
            values = self.getLastLine(self.path)
            splt = values.split(",")
            return {
                'lat': splt[0],
                'lon': splt[1],
                'height': splt[2]
            }
        except Exception as e:
            raise e

    def getValueAsArray(self):
        val = self.readValue()
        return [val['lat'], val['lon'], val['height']]