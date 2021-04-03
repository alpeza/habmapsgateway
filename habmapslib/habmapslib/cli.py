import click
import sys
from . import confyaml

@click.command()
@click.option('--conffile', help='Fichero de configuración')
@click.option('--genconffile', is_flag=True, help='Muestra un fichero de configuración de ejemplo')
def cline(conffile, genconffile):
    if genconffile:
        print(confyaml.conf)

if __name__ == '__main__':
    cline()