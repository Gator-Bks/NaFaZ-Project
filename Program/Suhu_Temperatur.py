#!/usr/bin/env python
#coding: utf-8
 

import codecs
import binascii
import time
from time import sleep
import sys
import os
from Program.Mulai import NFZ as Mulai


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"


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
\033[93m		   🅂🅄🄷🅄 🅃🄴🄼🄿🄴🅁🄰🅃🅄🅁
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m SUHU DALAM CELCIUS
\033[91m[\033[0m2\033[91m]\033[93m SUHU DALAM REAMUR 
\033[91m[\033[0m3\033[91m]\033[93m SUHU DALAM FAHRENHEIT
\033[91m[\033[0m4\033[91m]\033[93m SUHU DALAM KELVIN
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
	Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Bang_Jago is "1":
		Celcius()
	elif Bang_Jago is "2":
		Reamur()
	elif Bang_Jago is "3":
		Fahrenheit()
	elif Bang_Jago is "4":
		Kelvin()
	elif Bang_Jago == "5":
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM SUHU TEMPERATUR
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


def Celcius():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m SUHU DALAM CELCIUS")
	print("\n")
	C = int(input("\n\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Suhu\033[92m =\033[0m "))
	# Rumus Celcius By ǴaͲor βks
	R = (4/5) * C
	F = ((9/5) * C) + 32
	K = C + 273
	print("\n")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Celcius Ke Reamur")
	print("\033[91m=>\033[92m",C,"\b°C \033[96m=\033[93m",R,"\b°R")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Celcius Ke Fahrenheit")
	print("\033[91m=>\033[92m",C,"\b°C \033[96m=\033[93m",F,"\b°F")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Celcius Ke Kelvin")
	print("\033[91m=>\033[92m",C,"\b°C \033[96m=\033[93m",K,"\b°K")
	print("\033[97m")
	Balik()


def Reamur():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m SUHU DALAM REAMUR")
	print("\n")
	R = int(input("\n\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Suhu\033[92m =\033[0m "))
	# Rumus Reamur By ǴaͲor βks
	C = (5/4) * R
	F = ((9/4) * R) + 32
	K = ((5/4) * R) + 273
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[97m Reamur Ke Celcius")
	print("\033[91m=>\033[92m",R,"\b°R \033[96m=\033[93m",C,"\b°C")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Reamur Ke Fahrenheit")
	print("\033[91m=>\033[92m",R,"\b°R \033[96m=\033[93m",F,"\b°F")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Reamur Ke Kelvin")
	print("\033[91m=>\033[92m",R,"\b°R \033[96m=\033[93m",K,"\b°K")
	print("\033[97m")
	Balik()


def Fahrenheit():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m SUHU DALAM FAHRENHEIT")
	print("\n")
	F = int(input("\n\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Suhu\033[92m =\033[0m "))
	# Rumus Fahrenheit By ǴaͲor βks
	C = ((5/9) * F) - 32
	R = ((4/9) * F) - 32
	K = (((5/9) * F) - 32) + 273		
	print("\n")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Fahrenheit Ke Celcius")
	print("\033[91m=>\033[92m",F,"\b°F \033[96m=\033[93m",C,"\b°C")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Fahrenheit Ke Reamur")
	print("\033[91m=>\033[92m",F,"\b°F \033[96m=\033[93m",R,"\b°R")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Fahrenheit Ke Kelvin")
	print("\033[91m=>\033[92m",F,"\b°F \033[96m=\033[93m",K,"\b°K")
	print("\033[97m")
	Balik()


def Kelvin():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m SUHU DALAM KELVIN")
	print("\n")
	K = int(input("\n\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Suhu\033[92m =\033[0m "))
	# Rumus Kelvin By ǴaͲor βks
	C = K - 273
	R = ((4/5) * K) - 273
	F = (((9/5) * K) - 273) + 32
	print("\n")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Kelvin Ke Celcius")
	print("\033[91m=>\033[92m",K,"\b°K \033[96m=\033[93m",C,"\b°C")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Kelvin Ke Reamur")
	print("\033[91m=>\033[92m",K,"\b°K \033[96m=\033[93m",R,"\b°R")
	print("\033[97m")
	print("\033[96m[\033[93m+\033[96m]\033[97m Kelvin Ke Fahrenheit")
	print("\033[91m=>\033[92m",K,"\b°K \033[96m=\033[93m",F,"\b°F")
	print("\033[97m")
	Balik()


if __name__ == '__main__':
    NFZ()