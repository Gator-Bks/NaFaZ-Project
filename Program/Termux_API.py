#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
from time import sleep
import sys
import os
from Program.Mulai import NFZ as Mulai


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
sh = "neofetch"
tbs = "termux-battery-status"
tci = "termux-camera-info"
tcl = "termux-contact-list"
tl = "termux-location"
tcli = "termux-telephony-cellinfo"
ttdi = "termux-telephony-deviceinfo"
twci = "termux-wifi-connectioninfo"
twsi = "termux-wifi-scaninfo"


def Gator_Bks():
	os.system(Clears)
	print("""\033[91m	╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[0m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
\033[93m		    🅃🄴🅁🄼🅄🅇 🄰🄿🄸
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[0m
\033[0m • Gunakan Tools Ini Dengan Bijak!!!
\033[0m • Dilarang Memperjual Belikan Tools Ini Tanpa
\033[0m   Seizin Saya!!!
\033[0m • Dilarang Keras Untuk Recode Tools Ini Tanpa
\033[0m   Seizin Saya!!!
\033[0m • For Credit/Bug Chat WA : 081310662343
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0m
""")


def NFZ():
	Gator_Bks()
	print("""\033[91m[\033[0m1\033[91m]\033[93m INFO SPESIFIKASI HP SAAT INI
\033[91m[\033[0m2\033[91m]\033[93m INFO BATERAI SAAT INI
\033[91m[\033[0m3\033[91m]\033[93m INFO KAMERA SAAT INI
\033[91m[\033[0m4\033[91m]\033[93m INFO LIST KONTAK HP SAAT INI
\033[91m[\033[0m5\033[91m]\033[93m INFO LOKASI SAAT INI
\033[91m[\033[0m6\033[91m]\033[93m INFO SEL TELEPON SAAT INI
\033[91m[\033[0m7\033[91m]\033[93m INFO PERANGKAT TELEPON SAAT INI
\033[91m[\033[0m8\033[91m]\033[93m INFO KONEKSI WIFI SAAT INI
\033[91m[\033[0m9\033[91m]\033[93m INFO PEMINDAIAN WIFI SAAT INI
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")

	Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Bang_Jago is "1":
		Spesifikasi_HP()
	elif Bang_Jago is "2":
		Battery_Status()
	elif Bang_Jago is "3":
		Camera_Info()
	elif Bang_Jago is "4":
		Contact_List()
	elif Bang_Jago is "5":
		Location()
	elif Bang_Jago is "6":
		Cell_Info()
	elif Bang_Jago is "7":
		Cell_Dev_Info()
	elif Bang_Jago is "8":
		WiFi_Conn_Info()
	elif Bang_Jago is "9":
		WiFi_Scan_Info()
	elif Bang_Jago == "10":
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
		NFZ()


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
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM TERMUX API
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
	print("\033[37m")
	GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if GatorBks is "1":
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
		NFZ()
	elif GatorBks is "2":
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
		Mulai()
	elif GatorBks is "3":
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
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


def Spesifikasi_HP():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO SPESIFIKASI HP SAAT INI")
	print("\033[93m")
	os.system(sh)
	print("\033[37m")
	Balik()
	

def Battery_Status():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO BATERAI SAAT INI")
	print("\033[93m")
	os.system(tbs)
	print("\033[37m")
	Balik()
	

def Camera_Info():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO KAMERA SAAT INI")
	print("\033[93m")
	os.system(tci)
	print("\033[37m")
	Balik()


def Contact_List():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO LIST KONTAK HP SAAT INI")
	print("\033[93m")
	os.system(tcl)
	print("\033[37m")
	Balik()


def Location():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO LOKASI SAAT INI")
	print("\033[93m")
	os.system(tl)
	print("\033[37m")
	Balik()


def Cell_Info():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO SEL TELEPON SAAT INI")
	print("\033[93m")
	os.system(tcli)
	print("\033[37m")
	Balik()


def Cell_Dev_Info():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO PERANGKAT TELEPON SAAT INI")
	print("\033[93m")
	os.system(ttdi)
	print("\033[37m")
	Balik()


def WiFi_Conn_Info():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO KONEKSI WIFI SAAT INI")
	print("\033[93m")
	os.system(twci)
	print("\033[97m")
	Balik()


def WiFi_Scan_Info():
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m INFO PEMINDAIAN WIFI SAAT INI")
	print("\033[93m")
	os.system(twsi)
	print("\033[37m")
	Balik()


if __name__ == '__main__':
    NFZ()