import argparse
from Device import Device

parser = argparse.ArgumentParser()
parser.add_argument('--all', '-a', action='store_true', help='Tüm bilgileri gösterir')
parser.add_argument('--device-info', '-d', action='store_true', help='Cihaz bilgilerini gösterir')
parser.add_argument('--disk-usage', '-du', action='store_true', help='Disk kullanımını gösterir')
parser.add_argument('--cpu-usage', '-cu', action='store_true', help='CPU kullanımını gösterir')
parser.add_argument('--ram-usage', '-ru', action='store_true', help='RAM kullanımını gösterir')
parser.add_argument('--battery-info', '-b', action='store_true', help='Batarya bilgilerini gösterir')
parser.add_argument('--copied-text', '-c', action='store_true', help='Kopyalanan metni gösterir')
parser.add_argument('--current-time', '-ct', action='store_true', help='Geçerli zamanı gösterir')
parser.add_argument('--network-info', '-ni', action='store_true', help='Ağ bilgilerini gösterir')

args = parser.parse_args()
device = Device()
device.run(args)
