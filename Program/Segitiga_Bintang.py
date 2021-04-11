#!/usr/bin/env python
#coding: utf-8


import hashlib
from base64 import b64encode, b64decode
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
\033[93m		  🅂🄴🄶🄸🅃🄸🄶🄰 🄱🄸🄽🅃🄰🄽🄶
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m POLA 1
\033[91m[\033[0m2\033[91m]\033[93m POLA 2
\033[91m[\033[0m3\033[91m]\033[93m POLA 3
\033[91m[\033[0m4\033[91m]\033[93m POLA 4
\033[91m[\033[0m5\033[91m]\033[93m POLA 5
\033[91m[\033[0m6\033[91m]\033[93m POLA 6
\033[91m[\033[0m7\033[91m]\033[93m POLA 7
\033[91m[\033[0m8\033[91m]\033[93m POLA 8
\033[91m[\033[0m9\033[91m]\033[91m KELUAR
""")
	Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Bang_Jago is "1":
		Pola1()
	elif Bang_Jago is "2":
		Pola2()
	elif Bang_Jago is "3":
		Pola3()
	elif Bang_Jago is "4":
		Pola4()
	elif Bang_Jago is "5":
		Pola5()
	elif Bang_Jago is "6":
		Pola6()
	elif Bang_Jago is "7":
		Pola7()
	elif Bang_Jago is "8":
		Pola8()
	elif Bang_Jago == "9":
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM SEGITIGA BINTANG
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


def Pola1():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 1")
	print("\n")
	string = ""
	bar = 1
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	# Looping Baris
	while bar <= x:
		kol = bar
		# Looping Kolom
		while kol > 0:
			string = string + "*"
			kol = kol - 1
		string = string + "\n"
		bar = bar + 1
	print(string)
	print("\033[37m")
	Balik()


def Pola2():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 2")
	print("\n")
	string = ""
	bar = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	# Looping Baris
	while bar >= 0:
		kol = bar
		# Looping Kolom
		while kol > 0:
			string = string + "*"
			kol = kol - 1
		string = string + "\n"
		bar = bar - 1
	print(string)
	print("\033[37m")
	Balik()


def Pola3():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 3")
	print("\n")
	string = ""
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	bar = x
	# Looping Baris
	while bar >= 0:
		# Looping Kolom Spasi Kosong
		kol = bar
		while kol > 0:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang	
		kanan = 1
		while kanan < (x - (bar-1)):
			string = string + "*"
			kanan = kanan + 1		
		string = string + "\n"
		bar = bar - 1
	print(string)
	print("\033[37m")
	Balik()


def Pola4():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 4")
	print("\n")
	string = ""
	bar = 1
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	# Looping Baris
	while bar <= x:
		# Looping Kolom Spasi Kosong
		kol = bar	
		while kol > 1:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang	
		kanan = 0
		while kanan <= (x - bar):
			string = string + "*"
			kanan = kanan + 1	
		string = string + "\n"
		bar = bar + 1
	print(string)
	print("\033[37m")
	Balik()


def Pola5():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 5")
	print("\n")
	string = ""
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	bar = x
	# Looping Baris
	while bar >= 0:
		# Looping Kolom Spasi Kosong
		kol = bar
		while kol > 0:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri	
		kiri = 1
		while kiri < (x - (bar-1)):
			string = string + "*"
			kiri = kiri + 1		
		# Looping Kolom Bintang Sisi Kanan
		kanan = 1
		while kanan < kiri -1:
			string = string + "*"
			kanan = kanan + 1	
		string = string + "\n"
		bar = bar - 1
	print(string)
	print("\033[37m")
	Balik()


def Pola6():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 6")
	print("\n")
	string = ""
	bar = 1
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	# Looping Baris
	while bar <= x:
		kol = bar
		# Looping Kolom Spasi Kosong
		while kol > 1:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri	
		kiri = 0
		while kiri <= (x - bar):
			string = string + "*"
			kiri = kiri + 1	
		# Looping Kolom Bintang Sisi Kanan
		kanan = kiri	
		while kanan > 1:
			string = string + "*"
			kanan = kanan - 1
		string = string + "\n"
		bar = bar + 1
	print(string)
	print("\033[37m")
	Balik()


def Pola7():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 7")
	print("\n")
	string = ""
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	bar = x
	# Looping Baris
	while bar >= 0:
		# Looping Kolom Spasi Kosong
		kol = bar
		while kol > 0:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri		
		kiri = 1
		while kiri < (x - (bar-1)):
			string = string + "*"
			kiri = kiri + 1		
		# Looping Kolom Bintang Sisi Kanan
		kanan = 1
		while kanan < kiri -1:
			string = string + "*"
			kanan = kanan + 1	
		string = string + "\n"
		bar = bar - 1
	bar = 1	
	# Looping Baris
	while bar <= x:
		kol = bar+1
		# Looping Kolom Spasi Kosong
		while kol > 1:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri	
		kiri = 0
		while kiri < (x - bar):
			string = string + "*"
			kiri = kiri + 1	
		# Looping Kolom Bintang Sisi Kanan
		kanan = kiri	
		while kanan > 1:
			string = string + "*"
			kanan = kanan - 1
		string = string + "\n"
		bar = bar + 1
	print(string)
	print("\033[37m")
	Balik()


def Pola8():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[96m Pola 8")
	print("\n")
	string = ""
	bar = 1
	x = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Jumlah Segitiga\033[92m =\033[0m "))
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :\033[92m")
	# Looping Baris
	while bar < x:
		# Looping Kolom Spasi Kosong
		kol = bar
		while kol > 1:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri
		kiri = 0
		while kiri <= (x - bar):
			string = string + "*"
			kiri = kiri + 1	
		# Looping Kolom Bintang Sisi Kanan
		kanan = kiri	
		while kanan > 1:
			string = string + "*"
			kanan = kanan - 1
		if (bar+1) <= x:
			string = string + "\n"
		bar = bar + 1
	bar = x-1	
	# Looping Baris
	while bar >= 0:
		# Looping Kolom Spasi Kosong
		kol = bar
		while kol > 0:
			string = string + " "
			kol = kol - 1
		# Looping Kolom Bintang Sisi Kiri	
		kiri = 1
		while kiri < (x - (bar-1)):
			string = string + "*"
			kiri = kiri + 1		
		# Looping Kolom Bintang Sisi Kanan
		kanan = 1
		while kanan < kiri -1:
			string = string + "*"
			kanan = kanan + 1	
		string = string + "\n"
		bar = bar - 1
	print(string)
	print("\033[37m")
	Balik()


if __name__ == '__main__':
    NFZ()