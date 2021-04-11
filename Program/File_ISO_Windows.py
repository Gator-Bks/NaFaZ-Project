#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
import sys
import os
import json
import requests
from urllib import request
from time import sleep
import time
from Program.Mulai import NFZ as Mulai


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Gagal = "\033[92m[\033[93m+\033[92m]\033[91m Terdapat Kesalahan Yang Tidak Diketahui!!!"
Pesan = "\033[92m[\033[93m+\033[92m]\033[93m Sebentar Lagi Anda Akan Dialihkan Ke Browser"


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
\033[93m		 🄳🄰🅃🄰 🄲🄾🅁🄾🄽🄰 🅅🄸🅁🅄🅂
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


def NFZ():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m WINDOWS 7 HOME BASIC WITH SP1 32 BIT (2,39 GB)
\033[91m[\033[0m2\033[91m]\033[93m WINDOWS 7 STARTER WITH SP1 32 BIT (2,39 GB)
\033[91m[\033[0m3\033[91m]\033[93m WINDOWS 7 HOME PREMIUM 32 BIT (2,39 GB)
\033[91m[\033[0m4\033[91m]\033[93m WINDOWS 7 HOME PREMIUM 64 BIT (3,09 GB)
\033[91m[\033[0m5\033[91m]\033[93m WINDOWS 7 PRO 32 BIT (2,39 GB)
\033[91m[\033[0m6\033[91m]\033[93m WINDOWS 7 PRO 64 BIT (3,1 GB)
\033[91m[\033[0m7\033[91m]\033[93m WINDOWS 7 ULTIMATE 32 BIT (2,39 GB)
\033[91m[\033[0m8\033[91m]\033[93m WINDOWS 7 ULTIMATE 64 BIT (3,09 GB)
\033[91m[\033[0m9\033[91m]\033[93m WINDOWS 7 SP CLIENT ULTIMATE 32 BIT (3,71 GB)
\033[91m[\033[0m10\033[91m]\033[93m WINDOWS 7 SP CLIENT ULTIMATE 64 BIT (5,47 GB)
\033[91m[\033[0m11\033[91m]\033[93m WINDOWS 7 ENTERPRISE 32 BIT (2,27 GB)
\033[91m[\033[0m12\033[91m]\033[93m WINDOWS 7 ENTERPRISE 64 BIT (2,96 GB)
\033[91m[\033[0m13\033[91m]\033[93m WINDOWS 8 PRO 64 BIT (2,85 GB)
\033[91m[\033[0m14\033[91m]\033[93m WINDOWS 8.1 ENGLISH 32 BIT (2,99 GB)
\033[91m[\033[0m15\033[91m]\033[93m WINDOWS 8.1 ENGLISH 64 BIT (4,02 GB)
\033[91m[\033[0m16\033[91m]\033[93m WINDOWS 8.1 ENTERPRISE 32 BIT (2,85 GB)
\033[91m[\033[0m17\033[91m]\033[93m WINDOWS 8.1 ENTERPRISE 64 BIT (3,85 GB)
\033[91m[\033[0m18\033[91m]\033[93m WINDOWS 10 PRO ENGLISH 32 BIT (4,17 GB)
\033[91m[\033[0m19\033[91m]\033[93m WINDOWS 10 PRO ENGLISH 64 BIT (5,73 GB)
\033[91m[\033[0m20\033[91m]\033[93m WINDOWS 10 PRO ENGLISH 32 BIT (4,20 GB) [MICROSOFT]
\033[91m[\033[0m21\033[91m]\033[93m WINDOWS 10 PRO ENGLISH 64 BIT (5,79 GB) [MICROSOFT]
\033[91m[\033[0m22\033[91m]\033[93m WINDOWS 10 ENTERPRISE 32 BIT (4,0 GB)
\033[91m[\033[0m23\033[91m]\033[93m WINDOWS 10 ENTERPRISE 64 BIT (5,55 GB)
\033[91m[\033[0m24\033[91m]\033[93m WINDOWS SERVER 2008 R2 STANDARD & ENTERPRISE 64 BIT (2,8 GB)
\033[91m[\033[0m25\033[91m]\033[93m WINDOWS SERVER 2012 STANDARD 64 BIT (4,2 GB)
\033[91m[\033[0m26\033[91m]\033[93m WINDOWS SERVER 2012 R2 STANDARD 64 BIT (4,2 GB)
\033[91m[\033[0m27\033[91m]\033[93m WINDOWS SERVER 2012 R2 ESSENTIALS 64 BIT (3,8 GB)
\033[91m[\033[0m28\033[91m]\033[93m WINDOWS SERVER 2016 DATACENTER/STANDARD 64 BIT (5,3 GB)
\033[91m[\033[0m29\033[91m]\033[93m WINDOWS SERVER 2016 ESSENTIALS 64 BIT (4,48 GB)
\033[91m[\033[0m30\033[91m]\033[93m WINDOWS SERVER 2019 DATACENTER/STANDARD 64 BIT (4,5 GB)
\033[91m[\033[0m31\033[91m]\033[93m WINDOWS SERVER 2019 ESSENTIALS 64 BIT (4,3 GB)
\033[91m[\033[0m32\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        DOWN1()
    elif Bang_Jago == "2":
        DOWN2()
    elif Bang_Jago == "3":
        DOWN3()
    elif Bang_Jago == "4":
        DOWN4()
    elif Bang_Jago == "5":
        DOWN5()
    elif Bang_Jago == "6":
        DOWN6()
    elif Bang_Jago == "7":
        DOWN7()
    elif Bang_Jago == "8":
        DOWN8()
    elif Bang_Jago == "9":
        DOWN9()
    elif Bang_Jago == "10":
        DOWN10()
    elif Bang_Jago == "11":
        DOWN11()
    elif Bang_Jago == "12":
        DOWN12()
    elif Bang_Jago == "13":
        DOWN13()
    elif Bang_Jago == "14":
        DOWN14()
    elif Bang_Jago == "15":
        DOWN15()
    elif Bang_Jago == "16":
        DOWN16()
    elif Bang_Jago == "17":
        DOWN17()
    elif Bang_Jago == "18":
        DOWN18()
    elif Bang_Jago == "19":
        DOWN19()
    elif Bang_Jago == "20":
        DOWN20()
    elif Bang_Jago == "21":
        DOWN21()
    elif Bang_Jago == "22":
        DOWN22()
    elif Bang_Jago == "23":
        DOWN23()
    elif Bang_Jago == "24":
        DOWN24()
    elif Bang_Jago == "25":
        DOWN25()
    elif Bang_Jago == "26":
        DOWN26()
    elif Bang_Jago == "27":
        DOWN27()
    elif Bang_Jago == "28":
        DOWN28()
    elif Bang_Jago == "29":
        DOWN29()
    elif Bang_Jago == "30":
        DOWN30()
    elif Bang_Jago == "31":
        DOWN31()
    elif Bang_Jago == "32":
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM DOWNLOAD FILE ISO WINDOWS ALL VERSION
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    print("\033[37m")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
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
        Mulai()
    elif GatorBks == "3":
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


def Loading():
    os.system(Clears)
    print("\n")
    print(Pesan)
    countdownTimer(1,0)
    os.system(Clears)
    print("\n")
    print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
    os.system(Clears)


def countdownTimer(start_minute, start_second):
    total_second = start_minute * 10 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1


def DOWN1():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3iC6Yt1"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2MhuyiM"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/362KLPT"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Y26l2p"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN1()


def DOWN2():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2LXMjDE"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/362Wldy"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3qNRpBv"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3qIHrB6"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN2()


def DOWN3():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3o6BCvC"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3iBq5mU"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Y5eJ0Y"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3iBt5zB"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN3()


def DOWN4():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3ofEAhH"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Ygk9GR"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2M967Uu"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3iyVQ03"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN4()


def DOWN5():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Njl1Ig"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/363BJSC"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3qKdels"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3c2nCAU"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN5()


def DOWN6():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Y6me7O"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3o4THtV"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Y0GCYf"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3o7VH4S"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN6()


def DOWN7():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/3o6EkBi"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2YgnwgZ"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://bit.ly/2Y9yc0t"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3o6Lxl4"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN7()


def DOWN8():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/36kh1y7"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LTfSX7"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sMNRBb"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39V7nCJ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN8()


def DOWN9():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qG4qNh"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3660aim"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qJ03kE"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3660bTs"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN9()


def DOWN10():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c0NOLX"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/361WFtb"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sUGwQf"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c05cAu"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN10()


def DOWN11():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39SYiKX"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c2bDmE"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c7SUGB"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c2F1ZV"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN11()


def DOWN12():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39WsX9V"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qILQUU"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c0suq0"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/362RMjH"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN12()


def DOWN13():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c05SpJ"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LTzPNu"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c31w1c"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/362yTwZ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN13()


def DOWN14():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39Vz7Y8"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/363W36b"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LXeVgv"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39R9vM1"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN14()


def DOWN15():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sM5QYh"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/363G7RA"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/362WLAK"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c1kqp9"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN15()


def DOWN16():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2NiKVfc"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Nmsczn"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qKhSjo"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/360PAsK"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN16()


def DOWN17():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LVt3qn"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qzUAfU"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/360adpa"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2NrO5NX"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN17()


def DOWN18():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sOacOz"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/361Bmbh"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LUIM9h"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c39pUa"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN18()


def DOWN19():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sHVhWt"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39Y1Zig"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sWRg0q"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39RPEw4"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN19()


def DOWN20():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c0HVOV"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qO0hqN"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/362EW50"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c2wy96"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN20()


def DOWN21():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2NnLWTj"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qBvzkm"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c3anzU"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39VB9aI"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN21()


def DOWN22():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LU05Y6"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2NsGf6I"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sMS8Vf"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/363hdS3"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN22()


def DOWN23():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39XIoi6"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2M8i6lb"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sLC0Dm"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LKTgIr"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1"
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN23()


def DOWN24():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c1mX2D"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/365fYSj"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/362GyM6"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/36klWz5"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN24()


def DOWN25():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3o8R8qM"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/398BLdC"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3iCLf4b"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3iynslY"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN25()


def DOWN26():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c4OsYW"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3c2g6pq"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qCAgKE"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Nh4wwj"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN26()


def DOWN27():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3sOVK9l"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3qHM5PP"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2LVvZmT"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/365Bx58"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN27()


def DOWN28():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Mbm7FF"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Y63sgW"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3p2E2Nb"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Y2JiEF"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN28()


def DOWN29():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2Y6tZKY"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2KBjwnO"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3iBZia5"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/394nMpq"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN29()


def DOWN30():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/39bpXaV"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3oe4Jxm"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2KIyngs"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3pcrYcg"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN30()


def DOWN31():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/2MibEs4"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3p8fEtC"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3o7Yuer"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3o9AWFT"
    print("""\033[91m[\033[0m1\033[91m]\033[93m LINK DOWNLOAD 1
\033[91m[\033[0m2\033[91m]\033[93m LINK DOWNLOAD 2
\033[91m[\033[0m3\033[91m]\033[93m LINK DOWNLOAD 3
\033[91m[\033[0m4\033[91m]\033[93m LINK DOWNLOAD 4
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        NFZ()
    elif GatorBks == "6":
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
        DOWN31()


if __name__ == '__main__':
    NFZ()