

Tal vez me imagine algo de este palo:

1.- Lanzas un demon rollo esto:

```
sendmq --watch-file logs_de_lora.log \
       --frame "time|latlon|misensor1|misensor2|misensorn|habid|" \
       --extradata /ficheros/datos_gps_estacion_base.json \
       --mqttconf miconfigmqtt.conf \     #Fichero de config del mqtt
       --watch 2 \`
```

El parametro extradata seria un fichero json del siguiente estilo q se iria
actualizando cada n segundos por el programa del gps

```json
{
  "basestation": "miestacion",
  "pos": {
    "lat": 12,
    "lon": 39
  }
}
```
