#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
import sys
import os
import json
import socket
import requests
from urllib import request
import time
from time import sleep
from Mulai import NFZ


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Ulangi = NFZ()
Pesan = "\033[92m[\033[93m+\033[92m]\033[93m Harap Bersabar Sedang Memuat Data"
Gagal = "\033[92m[\033[93m+\033[92m]\033[91m Terdapat Kesalahan Yang Tidak Diketahui!!!"


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
\033[93m	      🄸🄿 🄳🄰🄽 🄳🄾🄼🄰🄸🄽 🄲🄾🄽🅅🄴🅁🅃🄴🅁
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m CONVERT DOMAIN TO IP ADDRESS
\033[91m[\033[0m2\033[91m]\033[93m CONVERT IP ADDRESS TO DOMAIN
\033[91m[\033[0m3\033[91m]\033[93m SHORTLINK DOMAIN TO BITLY
\033[91m[\033[0m4\033[91m]\033[93m SHORTLINK DOMAIN TO CUTTLY
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        DomainToIP()
    elif Bang_Jago == "2":
        IPToDomain()
    elif Bang_Jago == "3":
        Bitly()
    elif Bang_Jago == "4":
        Cuttly()
    elif Bang_Jago == "5":
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM IP & DOMAIN CONVERTER
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
        os.system(Ulangi)
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


def DomainToIP():
    os.system(Clears)
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m CONVERT SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Gator_Bks()
        URL = input("\n\033[91m[\033[93m+\033[91m]\033[96m Masukkan Nama Domain\033[93m =>\033[0m ")
        HASIL = socket.gethostbyname(URL)
        Loading()
        Gator_Bks()
        print("\n")
        print("\033[93m Domain      =", URL)
        print("\033[93m IP Address  =", HASIL)
        print("\033[37m")
        Balik()
    elif Bang_Jago == "2":
        NFZ()
    elif Bang_Jago == "3":
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


def IPToDomain():
    os.system(Clears)
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m CONVERT SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Gator_Bks()
        URL = input("\n\033[91m[\033[93m+\033[91m]\033[96m Masukkan Nama Domain\033[93m =>\033[0m ")
        HASIL = socket.gethostbyaddr(URL)
        Loading()
        Gator_Bks()
        print("\n")
        print("\033[93m Domain      =", URL)
        print("\033[93m IP Address  =", HASIL)
        print("\033[37m")
        Balik()
    elif Bang_Jago == "2":
        NFZ()
    elif Bang_Jago == "3":
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


def Bitly():
    os.system(Clears)
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m CONVERT SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        Bitly_Converter()
    elif Bang_Jago == "2":
        NFZ()
    elif Bang_Jago == "3":
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


def Cuttly():
    os.system(Clears)
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m CONVERT SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        Cuttly_Converter()
    elif Bang_Jago == "2":
        NFZ()
    elif Bang_Jago == "3":
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


def Bitly_Converter():
    os.system(Clears)
    Loading()
    try:
        akun = "o_508580e35c"
        sandi = "GATOR1903"
        auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(akun, sandi))
        if auth_res.status_code == 200:
            access_token = auth_res.content.decode()
        else:
            os.system(Clears)
            print("\n")
            print(Gagal)
            sleep(3)
            os.system(Clears)
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(3)
            os.system(Clears)
            NFZ()
        headers = {"Authorization": f"Bearer {access_token}"}
        groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
        if groups_res.status_code == 200:
            groups_data = groups_res.json()['groups'][0]
            guid = groups_data['guid']
        else:
            os.system(Clears)
            print("\n")
            print(Gagal)
            sleep(3)
            os.system(Clears)
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(3)
            os.system(Clears)
            NFZ()
        Loading()
        url = input("\n\033[91m[\033[93m+\033[91m]\033[96m Masukkan Nama Domain\033[93m =>\033[0m ")
        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
        if shorten_res.status_code == 200:
            link = shorten_res.json().get("link")
            print("\033[91m[\033[93m+\033[91m]\033[93m Shortened URL :\033[92m", link)
        else:
            os.system(Clears)
            print("\n")
            print(Gagal)
            sleep(3)
            os.system(Clears)
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(3)
            os.system(Clears)
            NFZ()
    except ValueError:
        os.system(Clears)
        print("\n")
        print(Gagal)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()
    except:
        os.system(Clears)
        print("\n")
        print(Gagal)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Cuttly_Converter():
    os.system(Clears)
    Loading()
    try:
        api_key = "a2b5dd4c6ecbfb0b3ba2a8c10c9e78313139a"
        url = input("\n\033[91m[\033[93m+\033[91m]\033[96m Masukkan Nama Domain\033[93m =>\033[0m ")
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            shortened_url = data["shortLink"]
            print("\033[91m[\033[93m+\033[91m]\033[93m Shortened URL :\033[92m", shortened_url)
        else:
            os.system(Clears)
            print("\n")
            print(Gagal)
            sleep(3)
            os.system(Clears)
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(3)
            os.system(Clears)
            NFZ()
    except ValueError:
        os.system(Clears)
        print("\n")
        print(Gagal)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()
    except:
        os.system(Clears)
        print("\n")
        print(Gagal)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


NFZ()