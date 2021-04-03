import click
import time

@click.command()
@click.option('--infile', help='Fichero de entrada con toda la coleccion de trazas')
@click.option('--outfile', help='Fichero sobre el que se esribira la traza')
@click.option('--delay', default=3, help='Segundos que tardara en enviarse la siguiete traza')
def simulog(infile, outfile,delay):
    print("Se inicia el append de lineas")
    with open(infile) as fp:
        Lines = fp.readlines()
        for line in Lines:
            with open(outfile, "a") as fpo:
                fpo.writelines(line)
            time.sleep(delay)

if __name__ == '__main__':
    simulog()