import click
import sys


def showConfFile():
    print('Se va a abrir')
    with open('conf.yaml', 'r') as f:
        print(f)

@click.command()
@click.option('--conffile', help='Fichero de configuración')
@click.option('--genconffile', is_flag=True, help='Muestra un fichero de configuración de ejemplo')
def cline(conffile, genconffile):
    if genconffile:
        showConfFile()

if __name__ == '__main__':
    cline()