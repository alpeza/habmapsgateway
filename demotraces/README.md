# Simulador de trazas

Lee las trazas de un fichero de entrada y las va metiendo en un fichero
de salida cada `--delay` segundos. El fichero `--outfile` simula el 
comportamiento del fichero que guarda las trazas LoRa.

```
python3 simulate_input.py --infile recivedData.log --outfile out.log --delay 3
```