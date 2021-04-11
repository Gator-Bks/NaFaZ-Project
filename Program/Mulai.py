#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
import sys
import os
from time import sleep
import time


Kal = time.strftime("%d-%m-%Y")
Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Salah = "\033[92m[\033[93m+\033[92m]\033[91m Terjadi Kesalahan!!!"
Pesan = "\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar"


def Gator_Bks():
	os.system(Clears)
	print("""\033[91m	╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[0m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[93m		  ▇ ◢▇▇▇◣◢▇▇▇◣ ▇
\033[93m		  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇
\033[93m		  ▇\033[91m╳\033[93m◥▇▇▇▇▇▇▇▇◤\033[91m╳\033[93m▇
\033[93m		  ▇\033[91m╳╳\033[93m◥▇▇▇▇▇▇◤\033[91m╳╳\033[93m▇
\033[93m		  ▇\033[91m╳╳╳\033[93m◥▇▇▇▇◤\033[91m╳╳╳\033[93m▇
\033[93m		  ▇\033[91m╳╳╳╳\033[93m▇▇▇▇\033[91m╳╳╳╳\033[93m▇
\033[93m		  ◥▇▇▇▇▇▇▇▇▇▇▇▇◤
\033[93m 		   ◥▇▇▇▇\033[91m◢◣\033[93m▇▇▇▇◤
\033[93m  		    ◥▇▇▇▇▇▇▇▇◤
\033[93m    		     ◥▇▇▇▇▇▇◤
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m HACK INSTAGRAM (VIA WEB)
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 SAAT INI
\033[91m[\033[0m3\033[91m]\033[93m IP GEOLOCATION
\033[91m[\033[0m4\033[91m]\033[93m SUBNETTING IP
\033[91m[\033[0m5\033[91m]\033[93m TEST JARINGAN INTERNET
\033[91m[\033[0m6\033[91m]\033[93m IP & DOMAIN CONVERTER
\033[91m[\033[0m7\033[91m]\033[93m ENCRYPTION & DECRYPTION
\033[91m[\033[0m8\033[91m]\033[93m DOWNLOAD FILE ISO LINUX (ARCHIVE)
\033[91m[\033[0m9\033[91m]\033[93m DOWNLOAD FILE ISO WINDOWS ALL VERSION
\033[91m[\033[0m10\033[91m]\033[93m SCRIPT DEFACE
\033[91m[\033[0m11\033[91m]\033[93m TERMUX TEMPLATE
\033[91m[\033[0m12\033[91m]\033[93m TERMUX API
\033[91m[\033[0m13\033[91m]\033[93m ANIMASI HACKER
\033[91m[\033[0m14\033[91m]\033[93m ARITMATIKA
\033[91m[\033[0m15\033[91m]\033[93m SUHU TEMPERATUR
\033[91m[\033[0m16\033[91m]\033[93m SEGITIGA BINTANG
\033[91m[\033[0m17\033[91m]\033[93m JOIN GROUP WHATSAPP & TELEGRAM
\033[91m[\033[0m18\033[91m]\033[93m TENTANG SAYA
\033[91m[\033[0m19\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        Hack_Instagram()
    elif Bang_Jago == "2":
        Covid19()
    elif Bang_Jago == "3":
        IP_Geolocation()
    elif Bang_Jago == "4":
        Subnetting_IP()
    elif Bang_Jago == "5":
        Test_Jaringan_Internet()
    elif Bang_Jago == "6":
        IP_Domain_Converter()
    elif Bang_Jago == "7":
        Encryption_Decryption()
    elif Bang_Jago == "8":
        File_ISO_Linux()
    elif Bang_Jago == "9":
        File_ISO_Windows()
    elif Bang_Jago == "10":
        Script_Deface()
    elif Bang_Jago == "11":
        Termux_Template()
    elif Bang_Jago == "12":
        Termux_API()
    elif Bang_Jago == "13":
        Animasi_Hacker()
    elif Bang_Jago == "14":
        Aritmatika()
    elif Bang_Jago == "15":
        Suhu_Temperatur()
    elif Bang_Jago == "16":
        Segitiga_Bintang()
    elif Bang_Jago == "17":
        JOIN()
    elif Bang_Jago == "18":
        Tentang_Saya()
    elif Bang_Jago == "19":
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


def Hack_Instagram():
    try:
        from Program.Hack_Instagram import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Covid19():
    try:
        from Program.Data_Covid import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def IP_Geolocation():
    try:
        from Program.IPGeoloc import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Subnetting_IP():
    os.system(Clears)
    print("\n")
    print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
    Loading()
    print("\n")
    print(Author)
    print(Thanks)
    print("\033[37m")
    sleep(5)
    os.system(Clears)
    print("\033[91m[\033[93m+\033[91m]\033[93m Script Sedang Diperbaiki")
    print("\033[91m[\033[93m+\033[91m]\033[93m Mohon Maaf Ya :")
    sleep(10)
    NFZ()


def Test_Jaringan_Internet():
    try:
        from Program.Test_Jaringan import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def IP_Domain_Converter():
    try:
        from Program.IP_Domain_Converter import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Encryption_Decryption():
    try:
        from Program.Enc_Dec import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        Encryption_Decryption()


def File_ISO_Linux():
    try:
        from Program.File_ISO_Linux import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def File_ISO_Windows():
    try:
        from Program.File_ISO_Windows import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Script_Deface():
    try:
        from Program.Script_Deface import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Termux_Template():
    try:
        from Program.Termux_Template import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Termux_API():
    try:
        from Program.Termux_API import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Animasi_Hacker():
    try:
        from Program.Animasi_Hacker import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Aritmatika():
    try:
        from Program.Aritmatika import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Suhu_Temperatur():
    try:
        from Program.Suhu_Temperatur import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Segitiga_Bintang():
    try:
        from Program.Segitiga_Bintang import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def JOIN():
    try:
        from Program.Join_Grup import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


def Tentang_Saya():
    try:
        from Program.Tentang_Saya import NFZ as Run
        Gator_Bks()
        print("""\033[91m[\033[0m1\033[91m]\033[93m JALANKAN SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
        GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
        if GatorBks == "1":
            os.system(Clears)
            print("\n")
            print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
            Loading()
            print("\n")
            print(Author)
            print(Thanks)
            print("\033[37m")
            sleep(5)
            os.system(Clears)
            Run()
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
            Animasi_Hacker()
    except ImportError:
        os.system(Clears)
        print("\n")
        print(Salah)
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
        print(Salah)
        sleep(3)
        os.system(Clears)
        print("\n")
        print(Author)
        print(Thanks)
        print("\033[37m")
        sleep(3)
        os.system(Clears)
        NFZ()


if __name__ == '__main__':
    NFZ()