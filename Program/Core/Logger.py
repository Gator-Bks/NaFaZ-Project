#!/usr/bin/env python3
# encoding: UTF-8 


from datetime import datetime
from termcolor import colored
from sys import platform as _platform
import codecs
import binascii
import time
from time import sleep
import sys
import os


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Ulangi = "python Run.py"
Run = "bash IP-GeoLocation.sh"


def Gator_Bks():
	os.system(Clears)
	print("""\033[91m
╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[0m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
\033[93m		   🄸🄿 🄶🄴🄾🄻🄾🄲🄰🅃🄸🄾🄽
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0m • Gunakan Tools Ini Dengan Bijak!!!
\033[0m • Dilarang Memperjual Belikan Tools Ini Tanpa
\033[0m   Seizin Saya!!!
\033[0m • Dilarang Keras Untuk Recode Tools Ini Tanpa
\033[0m   Seizin Saya!!!
\033[0m • For Credit/Bug Chat WA : 081310662343
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0m
""")


def Balik():
	print("\n")
	print(Author)
	print(Thanks)
	print("\033[37m")
	print("\n")
	print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Memilih Opsi Selanjutnya"))
	Lagi()
	

def Lagi():
	os.system(Clears)
	Gator_Bks()
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM ENCRYPTION & DECRYPTION
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
	print("\033[37m")
	GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if GatorBks == "1":
		os.system(Clears)
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
		sleep(5)
		os.system(Clears)
		print("\n")
		print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(5)
		os.system(Clears)
		os.system(Run)
	elif GatorBks == "2":
		os.system(Clears)
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
		sleep(10)
		os.system(Clears)
		print("\n")
		print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(5)
		os.system(Clears)
		os.system(Ulangi)
	elif GatorBks == "3":
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(5)
		os.system(Clears)
		exit()
	else:
		os.system(Clears)
		print("\n")
		print(Wrongs)
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		Lagi()


__author__ = 'Gator Bks'


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Green(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintIPGeoLocation(self, ipGeoLocation):
        Gator_Bks()
        self.PrintResult('Target ', ipGeoLocation.Query)
        self.PrintResult('IP ', ipGeoLocation.IP)
        self.PrintResult('ASN ', ipGeoLocation.ASN)
        self.PrintResult('Kota ', ipGeoLocation.City)
        self.PrintResult('Negara ', ipGeoLocation.Country)
        self.PrintResult('Kode Negara ', ipGeoLocation.CountryCode)
        self.PrintResult('ISP ', ipGeoLocation.ISP)
        self.PrintResult('Garis Lintang ', str(ipGeoLocation.Latitude))
        self.PrintResult('Garis Bujur ', str(ipGeoLocation.Longtitude))
        self.PrintResult('Organisasi ', ipGeoLocation.Organization)
        self.PrintResult('Kode Wilayah ', ipGeoLocation.Region)
        self.PrintResult('Nama Wilayah ', ipGeoLocation.RegionName)
        self.PrintResult('Zona Waktu ', ipGeoLocation.Timezone)
        self.PrintResult('Kode Zip ', ipGeoLocation.Zip)
        self.PrintResult('Google Maps ', ipGeoLocation.GoogleMapsLink)
        print("\033[37m")
        Balik()

        #.encode('cp737', errors='replace').decode('cp737')