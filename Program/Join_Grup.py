#!/usr/bin/env PYthon
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
Pesan = "\033[92m[\033[93m+\033[92m]\033[93m Sebentar Lagi Anda Akan Dialihkan Ke Tautan Grup"


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
\033[93m		     🄹🄾🄸🄽 🄶🅁🄾🅄🄿
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m UPDATE PROGRAM SUPERTOOLS BY GATOR BKS
\033[91m[\033[0m2\033[91m]\033[93m PROGRAMMING LANGUAGE
\033[91m[\033[0m3\033[91m]\033[93m BLOCKCHAIN
\033[91m[\033[0m4\033[91m]\033[93m DATABASE
\033[91m[\033[0m5\033[91m]\033[93m FIREBASE
\033[91m[\033[0m6\033[91m]\033[93m IOT
\033[91m[\033[0m7\033[91m]\033[93m DEVOPS
\033[91m[\033[0m8\033[91m]\033[93m SQA
\033[91m[\033[0m9\033[91m]\033[93m CLOUD COMPUTING SERVICES
\033[91m[\033[0m10\033[91m]\033[93m DATA PLAYGROUND
\033[91m[\033[0m11\033[91m]\033[93m DEVELOPMENT
\033[91m[\033[0m12\033[91m]\033[93m MICROSERVICE
\033[91m[\033[0m13\033[91m]\033[93m LINUX
\033[91m[\033[0m14\033[91m]\033[93m BSD
\033[91m[\033[0m15\033[91m]\033[93m MIKROTIK
\033[91m[\033[0m16\033[91m]\033[93m SECURITY
\033[91m[\033[0m17\033[91m]\033[93m WINDOWS
\033[91m[\033[0m18\033[91m]\033[93m IOS
\033[91m[\033[0m19\033[91m]\033[93m OPEN SOURCE
\033[91m[\033[0m20\033[91m]\033[93m GAME DEVELOPMENT
\033[91m[\033[0m21\033[91m]\033[93m STARTUP
\033[91m[\033[0m22\033[91m]\033[93m SCIENCE
\033[91m[\033[0m23\033[91m]\033[93m LOWONGAN KERJA
\033[91m[\033[0m24\033[91m]\033[93m TENTANG TELEGRAM
\033[91m[\033[0m25\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        SUPERTOOLS()
    elif Bang_Jago == "2":
        PROGRAMMING_LANGUAGE()
    elif Bang_Jago == "3":
        BLOCKCHAIN()
    elif Bang_Jago == "4":
        DATABASE()
    elif Bang_Jago == "5":
        FIREBASE()
    elif Bang_Jago == "6":
        IOT()
    elif Bang_Jago == "7":
        DEVOPS()
    elif Bang_Jago == "8":
        SQA()
    elif Bang_Jago == "9":
        CLOUD_COMPUTING_SERVICES()
    elif Bang_Jago == "10":
        DATA_PLAYGROUND()
    elif Bang_Jago == "11":
        DEVELOPMENT()
    elif Bang_Jago == "12":
        MICROSERVICE()
    elif Bang_Jago == "13":
        LINUX()
    elif Bang_Jago == "14":
        BSD()
    elif Bang_Jago == "15":
        MIKROTIK()
    elif Bang_Jago == "16":
        SECURITY()
    elif Bang_Jago == "17":
        WINDOWS()
    elif Bang_Jago == "18":
        IOS()
    elif Bang_Jago == "19":
        OPEN_SOURCE()
    elif Bang_Jago == "20":
        GAME_DEVELOPMENT()
    elif Bang_Jago == "21":
        STARTUP()
    elif Bang_Jago == "22":
        SCIENCE()
    elif Bang_Jago == "23":
        LOWONGAN_KERJA()
    elif Bang_Jago == "24":
        TENTANG_TELEGRAM()
    elif Bang_Jago == "25":
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM JOIN GROUP WHATSAPP & TELEGRAM
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


def SUPERTOOLS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://chat.whatsapp.com/K8FHkgl5ZcU5jo83npVJqq"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/joinchat/LY278KonMDowYzk1"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP WHATSAPP 
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        SUPERTOOLS()


def PROGRAMMING_LANGUAGE():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM AGILE
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM ASSEMBLY
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM BASH
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM BOOTSTRAP
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM C/C++
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM CRYSTAL
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM DART
\033[91m[\033[0m9\033[91m]\033[93m GRUP TELEGRAM DELPHI
\033[91m[\033[0m10\033[91m]\033[93m GRUP TELEGRAM ELIXIR
\033[91m[\033[0m11\033[91m]\033[93m GRUP TELEGRAM GOLANG
\033[91m[\033[0m12\033[91m]\033[93m GRUP TELEGRAM HASKELL
\033[91m[\033[0m13\033[91m]\033[93m GRUP TELEGRAM JAVA
\033[91m[\033[0m14\033[91m]\033[93m GRUP TELEGRAM JAVASCRIPT
\033[91m[\033[0m15\033[91m]\033[93m GRUP TELEGRAM KOTLIN
\033[91m[\033[0m16\033[91m]\033[93m GRUP TELEGRAM MICROSOFT
\033[91m[\033[0m17\033[91m]\033[93m GRUP TELEGRAM PASCAL
\033[91m[\033[0m18\033[91m]\033[93m GRUP TELEGRAM PHP
\033[91m[\033[0m19\033[91m]\033[93m GRUP TELEGRAM PYTHON
\033[91m[\033[0m20\033[91m]\033[93m GRUP TELEGRAM RUBY
\033[91m[\033[0m21\033[91m]\033[93m GRUP TELEGRAM RUST
\033[91m[\033[0m22\033[91m]\033[93m GRUP TELEGRAM SWIFT
\033[91m[\033[0m23\033[91m]\033[93m GRUP TELEGRAM TYPESCRIPT
\033[91m[\033[0m24\033[91m]\033[93m GRUP TELEGRAM SAP ABAP INDONESIA
\033[91m[\033[0m25\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m26\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        PROGRAMMING_LANGUAGE_ANDROID()
    elif Bang_Jago == "2":
        PROGRAMMING_LANGUAGE_AGILE()
    elif Bang_Jago == "3":
        PROGRAMMING_LANGUAGE_ASSEMBLY()
    elif Bang_Jago == "4":
        PROGRAMMING_LANGUAGE_BASH()
    elif Bang_Jago == "5":
        PROGRAMMING_LANGUAGE_BOOTSTRAP()
    elif Bang_Jago == "6":
        PROGRAMMING_LANGUAGE_C()
    elif Bang_Jago == "7":
        PROGRAMMING_LANGUAGE_CRYSTAL()
    elif Bang_Jago == "8":
        PROGRAMMING_LANGUAGE_DART()
    elif Bang_Jago == "9":
        PROGRAMMING_LANGUAGE_DELPHI()
    elif Bang_Jago == "10":
        PROGRAMMING_LANGUAGE_ELIXIR()
    elif Bang_Jago == "11":
        PROGRAMMING_LANGUAGE_GOLANG()
    elif Bang_Jago == "12":
        PROGRAMMING_LANGUAGE_HASKELL()
    elif Bang_Jago == "13":
        PROGRAMMING_LANGUAGE_JAVA()
    elif Bang_Jago == "14":
        PROGRAMMING_LANGUAGE_JAVASCRIPT()
    elif Bang_Jago == "15":
        PROGRAMMING_LANGUAGE_KOTLIN()
    elif Bang_Jago == "16":
        PROGRAMMING_LANGUAGE_MICROSOFT()
    elif Bang_Jago == "17":
        PROGRAMMING_LANGUAGE_PASCAL()
    elif Bang_Jago == "18":
        PROGRAMMING_LANGUAGE_PHP()
    elif Bang_Jago == "19":
        PROGRAMMING_LANGUAGE_PYTHON()
    elif Bang_Jago == "20":
        PROGRAMMING_LANGUAGE_RUBY()
    elif Bang_Jago == "21":
        PROGRAMMING_LANGUAGE_RUST()
    elif Bang_Jago == "22":
        PROGRAMMING_LANGUAGE_SWIFT()
    elif Bang_Jago == "23":
        PROGRAMMING_LANGUAGE_TYPESCRIPT()
    elif Bang_Jago == "24":
        PROGRAMMING_LANGUAGE_SAP()
    elif Bang_Jago == "25":
        NFZ()
    elif Bang_Jago == "26":
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
        PROGRAMMING_LANGUAGE()


def PROGRAMMING_LANGUAGE_ANDROID():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/androidDevBdg"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/BelajarBarengAndroid"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/androiddevelopernasional"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/AndroidSemarang"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/androiddevsurabaya"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/android_lombok"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/teknorialcom"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/source_code_android"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER BANDUNG
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER JAKARTA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER NASIONAL
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER SEMARANG
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER SURABAYA
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER LOMBOK
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM ANDROID DEVELOPER TEKNORIAL
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM SOURCE CODE ANDROID
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        NFZ()
    elif GatorBks == "10":
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
        PROGRAMMING_LANGUAGE_ANDROID()


def PROGRAMMING_LANGUAGE_AGILE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/agilecirclesid"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM AGILE CIRCLE INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_AGILE()


def PROGRAMMING_LANGUAGE_ASSEMBLY():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/AssemblyID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ASSEMBLY PROGRAMMING
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_ASSEMBLY()


def PROGRAMMING_LANGUAGE_BASH():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/bashidorg"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM BASH ID
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_BASH()


def PROGRAMMING_LANGUAGE_BOOTSTRAP():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/bootstrap_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM BOOTSTRAP INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_BOOTSTRAP()


def PROGRAMMING_LANGUAGE_C():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/CCpp_INDONESIA"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/idcplc"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM C/C++ INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m GRUP TELEGRAM INDONESIA C/C++ WARRIORS
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        PROGRAMMING_LANGUAGE_C()


def PROGRAMMING_LANGUAGE_CRYSTAL():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/CrystalID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM CRYSTAL USER GROUP INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_CRYSTAL()


def PROGRAMMING_LANGUAGE_DART():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/dart_web"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/flutter_id"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/flutter_jkt"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/fluttermakassar"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/lombokflutter"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM DART WEB
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM FLUTTER INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM FLUTTER JAKARTA
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM FLUTTER MAKASSAR
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM LOMBOK FLUTTER
\033[91m[\033[0m6\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m7\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        NFZ()
    elif GatorBks == "7":
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
        PROGRAMMING_LANGUAGE_DART()


def PROGRAMMING_LANGUAGE_DELPHI():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kppdi"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM DELPHI INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_DELPHI()


def PROGRAMMING_LANGUAGE_ELIXIR():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/elixir_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ELIXIR ID
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_ELIXIR()


def PROGRAMMING_LANGUAGE_GOLANG():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/golangID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/golangSurabaya"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM GOLANG INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM GOLANG SURABAYA
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        PROGRAMMING_LANGUAGE_GOLANG()


def PROGRAMMING_LANGUAGE_HASKELL():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/haskell_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM HASKELL ID
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_HASKELL()


def PROGRAMMING_LANGUAGE_JAVA():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/JVMUserGroup"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM JVM USER GROUP
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_JAVA()


def PROGRAMMING_LANGUAGE_JAVASCRIPT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/adonisid"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/AngularID"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/deno_id"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/electronatom"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/indonesiaionic"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/jakartajs"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/js_id"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/jogjajs"
    url8 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/lombokjs"
    url9 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/nativescript_id"
    url10 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/nodejsid"
    url11 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/nuxtjsid"
    url12 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/polymer_id"
    url13 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/react_id"
    url14 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/reactnative_id"
    url15 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/SemarangJS"
    url16 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/surabayajs"
    url17 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/svelte_id"
    url18 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/vuejsindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ADONIS.JS INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM ANGULAR INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM DENO INDONESIA
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM ELECTRON DESKTOP USER GROUP
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM IONIC INDONESIA
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM JAKARTA JS
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM JAVASCRIPT INDONESIA
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM JOGJA JS
\033[91m[\033[0m9\033[91m]\033[93m GRUP TELEGRAM LOMBOK JS
\033[91m[\033[0m10\033[91m]\033[93m GRUP TELEGRAM NATIVESCRIPT ID
\033[91m[\033[0m11\033[91m]\033[93m GRUP TELEGRAM NODEJS INDONESIA
\033[91m[\033[0m12\033[91m]\033[93m GRUP TELEGRAM NUXTJS INDONESIA
\033[91m[\033[0m13\033[91m]\033[93m GRUP TELEGRAM POLYMER INDONESIA
\033[91m[\033[0m14\033[91m]\033[93m GRUP TELEGRAM REACT INDONESIA
\033[91m[\033[0m15\033[91m]\033[93m GRUP TELEGRAM REACT NATIVE INDONESIA
\033[91m[\033[0m16\033[91m]\033[93m GRUP TELEGRAM SEMARANG JS
\033[91m[\033[0m17\033[91m]\033[93m GRUP TELEGRAM SURABAYA JS
\033[91m[\033[0m18\033[91m]\033[93m GRUP TELEGRAM SVELTE INDONESIA
\033[91m[\033[0m19\033[91m]\033[93m GRUP TELEGRAM VUE.JS INDONESIA
\033[91m[\033[0m20\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m21\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url8)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "10":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url9)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "11":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url10)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "12":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url11)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "13":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url12)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "14":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url13)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "15":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url14)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "16":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url15)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "17":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url16)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "18":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "19":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url18)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "20":
        NFZ()
    elif GatorBks == "21":
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
        PROGRAMMING_LANGUAGE_JAVASCRIPT()


def PROGRAMMING_LANGUAGE_KOTLIN():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kotlin_crb"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/KotlinID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM KOTLIN CIREBON
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM KOTLIN INDONESIA
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        PROGRAMMING_LANGUAGE_KOTLIN()


def PROGRAMMING_LANGUAGE_MICROSOFT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/dotnetcore_id"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/dotnetusergroup"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sqlserverid"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/xamarinindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM .NETCORE INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM .NET INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM SQL SERVER INDONESIA
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM XAMARIN INDONESIA
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
        PROGRAMMING_LANGUAGE_MICROSOFT()


def PROGRAMMING_LANGUAGE_PASCAL():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/PascalID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM PASCAL INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_PASCAL()


def PROGRAMMING_LANGUAGE_PHP():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/codeigniterindonesia"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/laravelindonesia"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/PHPIDforBusiness"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/PHPIDforStudent"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/phpjogloraya"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/symfonyid"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/botphp"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/YiiFrameworkIndonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM CODEIGNITER  INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM LARAVEL INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM PHP INDONESIA
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM PHP INDONESIA
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM PHP INDONESIA
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM SYMFONY FRAMEWORK INDONESIA
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM TELEGRAM BOT PHP INDONESIA
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM YII FRAMEWORK INDONESIA
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        NFZ()
    elif GatorBks == "10":
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
        PROGRAMMING_LANGUAGE_PHP()


def PROGRAMMING_LANGUAGE_PYTHON():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/DjangoID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/flaskid"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/lombok_py"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/mkspy"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/pythonID"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/pyjogja"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/surabayadotpy"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM DJANGO INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM FLASH ID
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM LOMBOK.PY
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM MKS.PY
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM PYTHON ID
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM PYTHON ID JOGJA
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM SURABAYA.PY
\033[91m[\033[0m8\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m8\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        NFZ()
    elif GatorBks == "9":
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
        PROGRAMMING_LANGUAGE_PYTHON()


def PROGRAMMING_LANGUAGE_RUBY():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/RailsID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ruby_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM RAILS INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM RUBY INDONESIA
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        PROGRAMMING_LANGUAGE_RUBY()


def PROGRAMMING_LANGUAGE_RUST():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/rustindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM RUST INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_RUST()


def PROGRAMMING_LANGUAGE_SWIFT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/swiftID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM SWIFT INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_SWIFT()


def PROGRAMMING_LANGUAGE_TYPESCRIPT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/TypescriptIndonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM TYPESCRIPT INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_TYPESCRIPT()


def PROGRAMMING_LANGUAGE_SAP():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sapabapindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM SAP-ABAP INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        PROGRAMMING_LANGUAGE_SAP()


def BLOCKCHAIN():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/friendswithblockchain"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/hl_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM FRIENDS WITH BLOCKCHAIN
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM HYPERLEDGER (ENTERPRISE) BLOCKCHAIN INDONESIA
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        BLOCKCHAIN()


def DATABASE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/MongoDB_ID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/mysqlid"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/postgresql_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM MONGODB INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM MYSQL INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM POSTGRESSQL INDONESIA
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        DATABASE()


def FIREBASE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/firebaseindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM FIREBASE INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        FIREBASE()


def IOT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ArduinoIndonesianCommunity"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/raspberrypi_id"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ARDUINO INDONESIAN COMMUNITY
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM RASPBERRY PI Indonesia
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        IOT()


def DEVOPS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/cloudcomputingindonesia"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/dockeridn"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/IDDevOps"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kubernetesindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM CLOUD COMPUTING INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM DOCKER.ID
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM ID DEVOPS
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM KUBERNETES INDONESIA
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
        DEVOPS()


def SQA():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sqa_id"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/joinchat/HxMrghPz5z3hr0eiRBcXOQ"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/qamalang"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM INDONESIAN SOFTWARE QUALITY ASSURAGE
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM INDONESIAN SOFTWARE QUALITY ASSURAGE CHAPTER JOGJA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM MALANG QUALITY ASSURAGE
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        SQA()


def CLOUD_COMPUTING_SERVICES():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/JuaraGCP"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/AWSUserGroupID"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/AWSDataUserGroupID"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/GCPUserID"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/GCP_ID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM #JUARAGCP
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM AWS USER GROUP INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM AWS ANALYTICS USER GROUP INDONESIA
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM GCP USER GROUP INDONESIA
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM GOOGLE CLOUD PLATFORM INDONESIA
\033[91m[\033[0m6\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m7\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        NFZ()
    elif GatorBks == "7":
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
        CLOUD_COMPUTING_SERVICES()


def DATA_PLAYGROUND():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ArtificialIntelligence_Indonesia"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/aidindonesia"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/idbigdata"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/businessintelligenceID"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/datascienceindonesia"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/machinelearningid"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/machinelearninglombok"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/nlp_lounge"
    url8 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/pytorchid"
    url9 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ScrapeID"
    url10 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/tensorflowid"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ARTIFICIAL INTELLIGENCE INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM ASOSIASI ILMUWAN DATA INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM BIG DATA OFFICIAL GROUP
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM BUSINESS INTELLIGENCE INDONESIA
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM DATA Scientist INDONESIA
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM MACHINE LEARNNG INDONESIA
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM MACHINE LEARNNG ID Lombok
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM NATURAL LANGUAGE ID
\033[91m[\033[0m9\033[91m]\033[93m GRUP TELEGRAM PYTORCH INDONESIA
\033[91m[\033[0m10\033[91m]\033[93m GRUP TELEGRAM SCRAPE ID
\033[91m[\033[0m11\033[91m]\033[93m GRUP TELEGRAM TENSORFLOW INDONESIA
\033[91m[\033[0m12\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m13\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url8)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "10":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url9)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "11":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url10)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "12":
        NFZ()
    elif GatorBks == "13":
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
        DATA_PLAYGROUND()


def DEVELOPMENT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/GNURIndonesia"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/BelajarGolangMariaDB"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/belajarhtmlcss"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/BogorDev"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/TgBotID"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/cilegondev"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/crbdev"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/femalegeek"
    url8 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/freekelasgithub"
    url9 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/FrontEndID"
    url10 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/gresikdev"
    url11 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/IAMIndonesia"
    url12 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/idstack"
    url13 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/eventteknologi"
    url14 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ITNusantara"
    url15 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/DjemberDev"
    url16 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kabayan_coding"
    url17 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/KelasMobileMalang"
    url18 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/BackEndID"
    url19 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/komunitasbk"
    url20 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kongkowITMedan"
    url21 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kongkowITpekanbaru"
    url22 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kotakodebetachat"
    url23 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/odooindonesia"
    url24 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/pasuruandev"
    url25 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/programersemarangraya"
    url26 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/rantaudev"
    url27 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/santrenkoding"
    url28 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sarccomuniverse"
    url29 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sidoarjodev"
    url30 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sinaudev"
    url31 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/soft_eng_id"
    url32 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/sparkarindonesia"
    url33 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/surabayadev"
    url34 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/lamongandev"
    url35 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/tamankodekode"
    url36 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/TailwindID"
    url37 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/TIAdevcommunity"
    url38 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/UiuxIndo"
    url39 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/uxidlombok"
    url40 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/VimID"
    url41 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/idwordpress"
    url42 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/otodidak_ngoding"
    url43 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kulkultech"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM BELAJAR GNU R INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM BELAJAR GOLANG MARIADB
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM BELAJAR HTML & CSS
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM BOGOR DEVELOPER
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM BOT TELEGRAM API
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM CILEGON DEVELOPER
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM CIREBON DEV
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM FEMALEGEEK
\033[91m[\033[0m9\033[91m]\033[93m GRUP TELEGRAM FREE KELAS GITHUB
\033[91m[\033[0m10\033[91m]\033[93m GRUP TELEGRAM Frontend DEVELOPER INDONESIA
\033[91m[\033[0m11\033[91m]\033[93m GRUP TELEGRAM GRESIK DEV
\033[91m[\033[0m12\033[91m]\033[93m GRUP TELEGRAM IAM INDONESIA
\033[91m[\033[0m13\033[91m]\033[93m GRUP TELEGRAM ID STACK
\033[91m[\033[0m14\033[91m]\033[93m GRUP TELEGRAM INFO EVENT TEKNOLOGI
\033[91m[\033[0m15\033[91m]\033[93m GRUP TELEGRAM IT NUSANTARA
\033[91m[\033[0m16\033[91m]\033[93m GRUP TELEGRAM JEMBER DEV
\033[91m[\033[0m17\033[91m]\033[93m GRUP TELEGRAM KABAYAN Coding
\033[91m[\033[0m18\033[91m]\033[93m GRUP TELEGRAM KELAS MOBILE MALANG
\033[91m[\033[0m19\033[91m]\033[93m GRUP TELEGRAM KOMUNITAS Backend DEVELOPER
\033[91m[\033[0m20\033[91m]\033[93m GRUP TELEGRAM KOMUNITAS BELAJAR KODING
\033[91m[\033[0m21\033[91m]\033[93m GRUP TELEGRAM KONGKOW IT MEDAN
\033[91m[\033[0m22\033[91m]\033[93m GRUP TELEGRAM KONGKOW IT PEKANBARU
\033[91m[\033[0m23\033[91m]\033[93m GRUP TELEGRAM KOTA KODE
\033[91m[\033[0m24\033[91m]\033[93m GRUP TELEGRAM ODOO - OPENERP INDONESIA
\033[91m[\033[0m25\033[91m]\033[93m GRUP TELEGRAM PASURUAN DEV
\033[91m[\033[0m26\033[91m]\033[93m GRUP TELEGRAM PROGRAMMER SEMARANG RAYA
\033[91m[\033[0m27\033[91m]\033[93m GRUP TELEGRAM RANTAU DEV
\033[91m[\033[0m28\033[91m]\033[93m GRUP TELEGRAM SANTREN KODING
\033[91m[\033[0m29\033[91m]\033[93m GRUP TELEGRAM SARCCOM UNIVERSE
\033[91m[\033[0m30\033[91m]\033[93m GRUP TELEGRAM SIDOARJO DEV
\033[91m[\033[0m31\033[91m]\033[93m GRUP TELEGRAM SINAUDEV - SINAU DEVELOPMENT
\033[91m[\033[0m32\033[91m]\033[93m GRUP TELEGRAM SOFTWARE ENGINEER INDONESIA
\033[91m[\033[0m33\033[91m]\033[93m GRUP TELEGRAM SPARKAR INDONESIA
\033[91m[\033[0m34\033[91m]\033[93m GRUP TELEGRAM SURABAYA DEV
\033[91m[\033[0m35\033[91m]\033[93m GRUP TELEGRAM LAMONGAN DEV
\033[91m[\033[0m36\033[91m]\033[93m GRUP TELEGRAM TAMAN KODE-KODE
\033[91m[\033[0m37\033[91m]\033[93m GRUP TELEGRAM TAILWIND INDONESIA
\033[91m[\033[0m38\033[91m]\033[93m GRUP TELEGRAM TECH IN ASIA DEV COMMUNITY
\033[91m[\033[0m39\033[91m]\033[93m GRUP TELEGRAM UI/UX INDONESIA
\033[91m[\033[0m40\033[91m]\033[93m GRUP TELEGRAM UXID Lombok
\033[91m[\033[0m41\033[91m]\033[93m GRUP TELEGRAM VIM  INDONESIA
\033[91m[\033[0m42\033[91m]\033[93m GRUP TELEGRAM WORDPRESS
\033[91m[\033[0m43\033[91m]\033[93m GRUP TELEGRAM CHANNEL OTODIDAK PEMROGRAMAN
\033[91m[\033[0m44\033[91m]\033[93m GRUP TELEGRAM KULKUL.TECH COMMUNITY - MEETUP AND DEV COMMUNITY
\033[91m[\033[0m45\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m46\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url8)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "10":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url9)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "11":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url10)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "12":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url11)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "13":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url12)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "14":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url13)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "15":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url14)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "16":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url15)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "17":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url16)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "18":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "19":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url18)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "20":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url19)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "21":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url20)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "22":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url21)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "23":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url22)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "23":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url23)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "24":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url23)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "25":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url24)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "26":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url25)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "27":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url26)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "28":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url27)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "29":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url28)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "30":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url29)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "31":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url30)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "32":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url31)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "33":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url32)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "34":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url33)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "35":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url34)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "36":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url35)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "37":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url36)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "38":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "39":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url38)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "40":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url39)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "41":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url40)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "42":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url41)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "43":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url42)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "44":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url43)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "45":
        NFZ()
    elif GatorBks == "46":
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
        DEVELOPMENT()


def MICROSERVICE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/msarchitecture"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM MICROSERVICE ARCHITECTURE
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        MICROSERVICE()


def LINUX():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ArchLinuxID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/GNULinuxIndonesia"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/BlankOnLinux"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/centosID"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/deepin_indonesia"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/dotfiles_id"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/elementaryID"
    url7 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/FedoraID"
    url8 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/gnomeid"
    url9 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/GPG_Indonesia"
    url10 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/KaliLinuxID"
    url11 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/kdeid"
    url12 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/linuxmalang"
    url13 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/linuxjember"
    url14 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/mint_id"
    url15 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/manjaroID"
    url16 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/openSUSE_ID"
    url17 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/parrotsecurityindonesia"
    url18 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/joinchat/AAAAAEFFHm4-NdDP7aRREA"
    url19 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ubuntu_id"
    url20 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/linuxsolo"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM ARCH LINUX INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM BELAJAR GNU/LINUX INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM BLANKON LINUX
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM CENTOS.ID
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM DEEPIN LINUX INDONESIA
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM DOTFILES INDONESIA
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM ELEMENTARY OS INDONESIA
\033[91m[\033[0m8\033[91m]\033[93m GRUP TELEGRAM FEDORA INDONESIA
\033[91m[\033[0m9\033[91m]\033[93m GRUP TELEGRAM GNOME INDONESIA
\033[91m[\033[0m10\033[91m]\033[93m GRUP TELEGRAM GENTOO INDONESIA
\033[91m[\033[0m11\033[91m]\033[93m GRUP TELEGRAM KALI LINUX INDONESIA
\033[91m[\033[0m12\033[91m]\033[93m GRUP TELEGRAM KDE INDONESIA
\033[91m[\033[0m13\033[91m]\033[93m GRUP TELEGRAM KOMUNITAS GNU/LINUX MALANG
\033[91m[\033[0m14\033[91m]\033[93m GRUP TELEGRAM KOMUNITAS LINUX JEMBER
\033[91m[\033[0m15\033[91m]\033[93m GRUP TELEGRAM LINUX MINT INDONESIA
\033[91m[\033[0m16\033[91m]\033[93m GRUP TELEGRAM MANJARO INDONESIA
\033[91m[\033[0m17\033[91m]\033[93m GRUP TELEGRAM OPENSUSE  INDONESIA
\033[91m[\033[0m18\033[91m]\033[93m GRUP TELEGRAM PARROTSEC INDONESIA
\033[91m[\033[0m19\033[91m]\033[93m GRUP TELEGRAM TEA LINUX OS
\033[91m[\033[0m20\033[91m]\033[93m GRUP TELEGRAM UBUNTU INDONESIA
\033[91m[\033[0m21\033[91m]\033[93m GRUP TELEGRAM PAGUYUBAN LINUX SOLO
\033[91m[\033[0m22\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m23\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "9":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url8)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "10":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url9)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "11":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url10)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "12":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url11)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "13":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url12)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "14":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url13)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "15":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url14)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "16":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url15)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "17":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url16)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "18":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url7)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "19":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url18)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "20":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url9)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "21":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url20)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "22":
        NFZ()
    elif GatorBks == "23":
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
        LINUX()


def BSD():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/setanmerahID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM LASKAR SETAN MERAH - SHARING ALL ABOUT FREEBSD
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        BSD()


def MIKROTIK():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/setanmerahID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM MIKROTIK INDONESIA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        MIKROTIK()


def SECURITY():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/DevSecOpsIndonesia"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ForensicaID"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/reversingid"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/orangsiber"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/itsecurityindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM DEVSECOPS INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM FORENSICA ID
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM REVERSING.ID
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM ORANG SIBER INDONESIA
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM IT SECURITY INDONESIA
\033[91m[\033[0m6\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m7\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        NFZ()
    elif GatorBks == "7":
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
        SECURITY()


def WINDOWS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/pegelwindows"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/WinTenGroup"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/WindServID"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM PEGEL WINDOWS
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM WINDOWS 10 COMMUNITY ID
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM WINDOWS SERVER INDONESIA
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        WINDOWS()


def IOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/ikaskus"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d http://t.me/initialestore"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM IKASKUS
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM INITIAL E
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "4":
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
        IOS()


def OPEN_SOURCE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/doscomedia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM DOSCOM - DINUS OPEN SOURCE COMMUNITY
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        OPEN_SOURCE()


def GAME_DEVELOPMENT():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/lombokgamedev"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM LOMBOK GAMES DEVELOPERS (LGD)
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
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
        NFZ()
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
        GAME_DEVELOPMENT()


def STARTUP():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/cafestartup"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/startupindonesia"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/startupweekendindonesia"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM CAFE STARTUP 140315
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM STARTUP INDONESIA ON TELEGRAM
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM STARTUP WEEKEND INDONESIA
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        STARTUP()


def SCIENCE():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m GEOGRAPHIC INFORMATION SYSTEM AND REMOTE SENSING
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        SCIENCE_GEOGRAPHIC()
    elif GatorBks == "2":
        NFZ()
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
        SCIENCE()


def SCIENCE_GEOGRAPHIC():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/gis_id"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/qgisindonesia"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/leafletid"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM GIS INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM QGIS INDONESIA
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM LEAFLET.JS INDONESIA
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        SCIENCE_GEOGRAPHIC()


def LOWONGAN_KERJA():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/freelancerID"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/freelance_01"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/LokerDeveloper"
    url3 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/loker_jakarta"
    url4 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/LowonganKerjaIT"
    url5 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/RailsID_LOKER"
    url6 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/RubyID_LOKER"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM FREELANCER INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM FREELANCE PROJECT IT
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM LOKER DEVELOPER/PROGRAMMER
\033[91m[\033[0m4\033[91m]\033[93m GRUP TELEGRAM LOKER JAKARTA
\033[91m[\033[0m5\033[91m]\033[93m GRUP TELEGRAM LOWONGAN Kerja IT
\033[91m[\033[0m6\033[91m]\033[93m GRUP TELEGRAM RAILS INDONESIA LOKER
\033[91m[\033[0m7\033[91m]\033[93m GRUP TELEGRAM RUBY INDONESIA LOKER
\033[91m[\033[0m8\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m8\033[91m]\033[91m KELUAR
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
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "6":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "7":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url6)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "8":
        NFZ()
    elif GatorBks == "9":
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
        LOWONGAN_KERJA()


def TENTANG_TELEGRAM():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/tgbeta"
    url1 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/themeschannel"
    url2 = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://t.me/tentangtelegram"
    print("""\033[91m[\033[0m1\033[91m]\033[93m GRUP TELEGRAM TELEGRAM BETA
\033[91m[\033[0m2\033[91m]\033[93m GRUP TELEGRAM TELEGRAM THEMES
\033[91m[\033[0m3\033[91m]\033[93m GRUP TELEGRAM TELEGRAM TELEGRAM
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
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
        NFZ()
    elif GatorBks == "5":
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
        TENTANG_TELEGRAM()


if __name__ == '__main__':
    NFZ()