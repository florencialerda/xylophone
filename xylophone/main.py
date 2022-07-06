import argparse
from xylophone.client import XyloClient
from xylophone.xylo import XyloNote
from client import read_score

parser = argparse.ArgumentParser(description="Lee una partitura y se comunica con un dispositivo para tocar una canción")
parser.add_argument("-p", "--partitura", type=str, required=True, help="Nombre del archivo de entrada que describe la partitura")
parser.add_argument("-d", "--dispositivo", type=int, required=True, help="Nombre del dispositivo con el cual se quiere comunicar")
args=parser.parse_args()

def main(partitura, dispositivo):
    read_score(partitura)
    read_xylophone(dispositivo)

if __name__ == '__main__':
    main(args.partitura, args.dispositivo)