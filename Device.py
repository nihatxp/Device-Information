import os
import ctypes
import socket
import pyperclip
import psutil
import time
from datetime import datetime


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Device:
    def __init__(self, clear_terminal=True, colorful_output=True):
        self.clear_terminal = clear_terminal
        self.colorful_output = colorful_output

    def print_device_info(self):
        if self.clear_terminal:
            self.clear_terminal_func()

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"{Color.BOLD}Host name: {hostname}")
        print(f"IP Address: {ip_address}{Color.END}\n")

    def clear_terminal_func(self):
        if os.name == 'nt':  # Windows işletim sistemi için
            _ = os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW("Your Title")  # Başlığı yeniden ayarlayın
        else:  # Diğer işletim sistemleri için (Linux, macOS)
            _ = os.system('clear')

    def print_disk_usage(self):
        disk_usage = psutil.disk_usage('C:/')
        total_gb = round(disk_usage.total / (1024 ** 3), 2)
        used_gb = round(disk_usage.used / (1024 ** 3), 2)
        free_gb = round(disk_usage.free / (1024 ** 3), 2)
        percent = disk_usage.percent

        print(f"{Color.PURPLE}--- Disk Kullanımı ---{Color.END}")
        print(f"Toplam: {total_gb} GB")
        print(f"Kullanılabilir: {used_gb} GB")
        print(f"Boşta: {free_gb} GB")
        print(f"Percent: {percent}%")
        print(Color.END)

    def print_cpu_usage(self):
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)

        print(f"{Color.BOLD}-{Color.YELLOW * 30} CPU {Color.END}{Color.BOLD}-{Color.YELLOW * 30}")
        for i, percent in enumerate(cpu_percent):
            print(f"Çekirdek {i + 1}: {percent}%")
        print(Color.END)

    def print_ram_usage(self):
        ram_usage = psutil.virtual_memory()

        print(f"{Color.BOLD}-{Color.YELLOW * 30} RAM {Color.END}{Color.BOLD}-{Color.YELLOW * 30}")
        print(f"Toplam: {self.format_size(ram_usage.total)}")
        print(f"Kullanılabilir: {self.format_size(ram_usage.available)}")
        print(f"Percent: {ram_usage.percent}%")
        print(f"Kullanılıyor: {self.format_size(ram_usage.used)}")
        print(f"Boşta: {self.format_size(ram_usage.free)}")
        print(Color.END)

    def print_battery_info(self):
        battery = psutil.sensors_battery()

        print(f"{Color.BLUE}Batarya Yüzdesi: {battery.percent}%")
        print(f"Sarj Durumu: {battery.power_plugged}")
        print(f"Pil Kalan Süre: {self.convert_time(battery.secsleft)}{Color.END}")


    def print_copied_text(self):
        spam = pyperclip.paste()
        print(f"{Color.BOLD}------ KOPYALANAN METİN -------")
        print(spam)
        print(f"\n-------------------------------{Color.END}")
        print(Color.END)

    def format_size(self, size):
        power = 1024
        n = 0
        power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while size > power:
            size /= power
            n += 1
        return f"{round(size, 2)} {power_labels[n]}B"

    def convert_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours}:{minutes:02d}:{seconds:02d}"

    def print_current_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{Color.GREEN}Current Time: {current_time}{Color.END}")
        print(Color.END)

    def print_network_info(self):
        network_info = psutil.net_if_addrs()

        print(f"{Color.BOLD}-{Color.CYAN * 30} Network {Color.END}{Color.BOLD}-{Color.CYAN * 30}")
        for interface, addresses in network_info.items():
            print(f"Interface: {interface}")
            for address in addresses:
                if address.family == socket.AF_INET:
                    print(f"IPv4 Address: {address.address}")
                    print(f"Netmask: {address.netmask}")
                elif address.family == socket.AF_INET6:
                    print(f"IPv6 Address: {address.address}")
        print(Color.END)

    def run(self, args):
        if args.all:
            self.print_device_info()
            time.sleep(1)
            self.print_disk_usage()
            time.sleep(1)
            self.print_cpu_usage()
            time.sleep(1)
            self.print_ram_usage()
            time.sleep(1)
            self.print_battery_info()
            time.sleep(1)
            self.print_copied_text()
            time.sleep(1)
            self.print_current_time()
            time.sleep(1)
            self.print_network_info()
        else:
            if args.device_info:
                self.print_device_info()
            if args.disk_usage:
                self.print_disk_usage()
            if args.cpu_usage:
                self.print_cpu_usage()
            if args.ram_usage:
                self.print_ram_usage()
            if args.battery_info:
                self.print_battery_info()
            if args.copied_text:
                self.print_copied_text()
            if args.current_time:
                self.print_current_time()
            if args.network_info:
                self.print_network_info()

