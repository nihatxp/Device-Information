"""
Bu projede cihaz adını, Dinamik, Statik IP adresini, Kullanılabilir, Toplam
Depolama alanı/Önbellek, Kullanılıan sürücü, CPU kullanılma durumu, Batarya yuzdesi,
Kopyalanmış metin gibi bilgileri işleyip disk.txt adında txt dosyasına yazıyoruz.


In this project, device name, Dynamic, Static IP address, Available/Total
Storage/Cache, Drive used, CPU usage status,Battery percentage,
We process information such as copied text and write it to a txt file named disk.txt
"""

import socket
import time
import sys 
stdoutOrigin=sys.stdout #Dosyaya Yaz
sys.stdout = open("disk.txt", "w")
print("____________DISK_____________")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
d=("-"*30)
print(f"Host name: {hostname}")
print(f"IP Address: {ip_address}\n",d)
import netifaces
from netifaces import interfaces, ifaddresses, AF_INET
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    print ('%s: %s' % (ifaceName, ', '.join(addresses)))
from urllib.request import urlopen
import re
#3 kez dene
i=0
l=False
while i<3:
    try:
        data = str(urlopen('http://chckip.dyndns.com/').read())
        time.sleep(1)
        print(re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1))
        print("BASARILI")
        l=True
        break
    except:
        print("hata:",i)
        i=i+1
        continue
#disk kullanimi
import psutil
a="\n"+("-"*30)+"Hafiza"+("-"*30)+"\n"
DiskKullanimi = psutil.disk_usage('C:/');
b=("TOPLAM : "+str(DiskKullanimi[0])+"~"+str(round(int(DiskKullanimi[0])/1078500000))+" GB\n")
p=("KULLANILABILIR : "+str(DiskKullanimi[1])+"~"+str(round(int(DiskKullanimi[1])/1078500000))+" GB\n")
x=("BOSTA : "+str(DiskKullanimi[2])+"~"+str(round(int(DiskKullanimi[2])/1078500000))+" GB\n")
y=("Percent : "+str(DiskKullanimi[3])+"\n")
c=("-"*20+"Device"+"-"*20)
print(str(a)+str(b)+str(p)+str(x)+str(y)+str(c)+str(d))

DiskBilgileri = psutil.disk_partitions();
deger1=DiskBilgileri[0]
deger2=DiskBilgileri[1]
cihaz="Cihaz: "+DiskBilgileri[0][0]
mountpoint="Mountpint:",DiskBilgileri[0][1]
bicim="Bicim: ",DiskBilgileri[0][2]
print(str(deger1)+str(deger2)+str(cihaz)+str(mountpoint)+str(bicim))
print("-"*30)
ramKullanimi = psutil.virtual_memory()
print("-"*30,"RAM","-"*30)
print("RAM Toplam:",ramKullanimi[0])
print("RAM Kullanilabilir:",ramKullanimi[1])
print("RAM Percent:",ramKullanimi[2])
print("RAM Kullaniliyor:",ramKullanimi[3])
print("RAM Bosta:",ramKullanimi[4])
print("-"*30)
cpuyazisi="-"*20+"CPU"+"-"*20
print("-"*30)
for x in range(5):
     cpu="|CPU "+str(psutil.cpu_percent(interval=1))+"|"
     print(cpu)
#anlık işlemci kullanım değeri.
print("-"*30)
print("-"*30)
#Batarya Durumu
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
  
battery = psutil.sensors_battery()
  
print("Batarya Yuzdesi : ", battery.percent)
print("Sarj durumu : ", battery.power_plugged)
  
print("Pil kaldi : ", convertTime(battery.secsleft))
#pyperclip ile kopyalanmis metni alalim
import pyperclip
spam = pyperclip.paste()
print('\n\t\t\t------COPY-------')
print(spam)
print('\n\t\t\t------------------')

i=0
if l==False: #Az onceki ip adresi alma islemi basarisiz ise simdi yeniden deneyelim
    while i<3:
        try:
            data = str(urlopen('http://checkip.dyndns.com/').read())
            time.sleep(1)
            print(re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1))
            print("IKINCI DENEME BASARILI OLDU")
            break
        except:
            print("hata:",i)
            i=i+1
            continue
sys.stdout.close() #metin belgesini kapatalim
sys.stdout=stdoutOrigin
#Sistem bilgileri system data.txt adinda klasorde mevcutdur.
