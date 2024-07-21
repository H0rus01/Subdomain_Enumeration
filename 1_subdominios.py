import urllib.request
import urllib.error
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Indicar el dominio de la victima')
args = parser.parse_args()

def main():
    if args.target:
        if path.exists('subdominios.txt'):
            with open('subdominios.txt','r') as f:
                worldlist = f.read().splitlines()
            if worldlist:    
                for subdominio in worldlist:
                    url = "http://"+subdominio+"."+args.target
                    try: 
                        urllib.request.urlopen(url)
                    except urllib.error.URLError:
                        pass
                    else: 
                        print("(+)Subdominio encontrado: " + url)
            else:
                print("(-) La lista de subdominios esta vacia")
        else:
            print("(-) El archivo 'ubdominios.txt' no existe")
    else:
        print("(-) Ingresa un dominio")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: 
        sys.exit()