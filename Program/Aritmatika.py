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
\033[93m		    🄰🅁🄸🅃🄼🄰🅃🄸🄺🄰
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m PERTAMBAHAN
\033[91m[\033[0m2\033[91m]\033[93m PENGURANGAN
\033[91m[\033[0m3\033[91m]\033[93m PERKALIAN
\033[91m[\033[0m4\033[91m]\033[93m PEMBAGIAN
\033[91m[\033[0m5\033[91m]\033[93m PERPANGKATAN
\033[91m[\033[0m6\033[91m]\033[93m SISA BAGIERPANGKATAN
\033[91m[\033[0m7\033[91m]\033[91m KELUAR
""")
	Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Bang_Jago == "1":
		Pertambahan()
	elif Bang_Jago == "2":
		Pengurangan()
	elif Bang_Jago == "3":
		Perkalian()
	elif Bang_Jago == "4":
		Pembagian()
	elif Bang_Jago == "5":
		Perpangkatan()
	elif Bang_Jago == "6":
		Sisa_Bagi()
	elif Bang_Jago == "7":
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM ARITMATIKA
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
	print("\033[37m")
	GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if GatorBks == "1":
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
		NFZ()
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


def Pertambahan():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m PERTAMBAHAN")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	tambah = Nilai1 + Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",tambah)
	print("\033[37m")
	Balik()


def Pengurangan():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m PENGURANGAN")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	Kurang = Nilai1 - Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",Kurang)
	print("\033[37m")
	Balik()


def Perkalian():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m PERKALIAN")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	Kali = Nilai1 * Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",Kali)
	print("\033[37m")
	Balik()


def Pembagian():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m PEMBAGIAN")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	Bagi = Nilai1 / Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",Bagi)
	print("\033[37m")
	Balik()


def Perpangkatan():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m PERPANGKATAN")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	Pangkat = Nilai1 ** Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",Pangkat)
	print("\033[37m")
	Balik()


def Sisa_Bagi():
	os.system(Clears)
	Gator_Bks()
	print("\033[93m[\033[91m+\033[93m]\033[0m SISA BAGI")
	print("\n")
	Nilai1 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Pertama\033[93m =\033[0m "))
	Nilai2 = int(input("\033[91m[\033[93m+\033[91m]\033[93m Masukkan Nilai Kedua\033[93m =\033[0m "))
	Modulus = Nilai1 % Nilai2
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",Modulus)
	print("\033[37m")
	Balik()


NFZ()
