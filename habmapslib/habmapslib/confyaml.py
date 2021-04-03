conf='''
basestation:
  id: id-de-mi-estacion
  appenders:
    - name: gps
      filepath: /fichero/con/tramas/gps.txt
mqtt:
  url: localhost
  topic: hablistener
  port: 1883
  user: habmaps
  password: root
  alive: 60
frame:
  # Definición de la trama donde
  # $time : Es la hora expresada en HHMMSS
  # $pos : Es la posición gps del hab expresada en lat,lon
  # $id  : Es el identificador del hab
  format: "$time|AlturaGPS|$pos|VelocidadHorizontalGPS|Temperatura|Presion|AlturaBarometrica|$id"
  # Fichero donde se van insertando las trazas de LoRa
  file: logs_de_lora.log
  # Cada cuantos segundos se mira el fichero de envio
  refresh: 1
'''