#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
import sys
import os
import time
from time import sleep
from Program.Mulai import NFZ as Mulai


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
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
\033[93m		   🄵🄸🄻🄴 🄸🅂🄾 🄻🄸🄽🅄🅇
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m ALPINE LINUX
\033[91m[\033[0m2\033[91m]\033[93m ALT LINUX
\033[91m[\033[0m3\033[91m]\033[93m ANTIX
\033[91m[\033[0m4\033[91m]\033[93m ARCH LINUX
\033[91m[\033[0m5\033[91m]\033[93m BEOS
\033[91m[\033[0m6\033[91m]\033[93m BLACKARCH
\033[91m[\033[0m7\033[91m]\033[93m BLANKON
\033[91m[\033[0m8\033[91m]\033[93m BODHI LINUX
\033[91m[\033[0m9\033[91m]\033[93m CALDERA OPENLINUX
\033[91m[\033[0m10\033[91m]\033[93m CALCULATE
\033[91m[\033[0m11\033[91m]\033[93m CENTOS
\033[91m[\033[0m12\033[91m]\033[93m CHAKRA LINUX
\033[91m[\033[0m13\033[91m]\033[93m COREL LINUX
\033[91m[\033[0m14\033[91m]\033[93m DEBIAN
\033[91m[\033[0m15\033[91m]\033[93m DEEPIN
\033[91m[\033[0m16\033[91m]\033[93m DEMO LINUX
\033[91m[\033[0m17\033[91m]\033[93m DRAGONFLY
\033[91m[\033[0m18\033[91m]\033[93m ELEMENTARY OS
\033[91m[\033[0m19\033[91m]\033[93m ENDEAVOUR OS
\033[91m[\033[0m20\033[91m]\033[93m ENDLESS OS
\033[91m[\033[0m21\033[91m]\033[93m EXTIX
\033[91m[\033[0m22\033[91m]\033[93m FEDORA
\033[91m[\033[0m23\033[91m]\033[93m FREE BSD
\033[91m[\033[0m24\033[91m]\033[93m GARUDA
\033[91m[\033[0m25\033[91m]\033[93m GENTOO
\033[91m[\033[0m26\033[91m]\033[93m HAIKU
\033[91m[\033[0m27\033[91m]\033[93m KALI LINUX
\033[91m[\033[0m28\033[91m]\033[93m KNOPPIX
\033[91m[\033[0m29\033[91m]\033[93m KUBUNTU
\033[91m[\033[0m30\033[91m]\033[93m LINUX KERNEL
\033[91m[\033[0m31\033[91m]\033[93m LINUX MINT
\033[91m[\033[0m32\033[91m]\033[93m LUBUNTU
\033[91m[\033[0m33\033[91m]\033[93m LUNINUX OS
\033[91m[\033[0m34\033[91m]\033[93m MAGEIA
\033[91m[\033[0m35\033[91m]\033[93m MANDRIVA
\033[91m[\033[0m36\033[91m]\033[93m MANDRAKE
\033[91m[\033[0m37\033[91m]\033[93m MANJARO
\033[91m[\033[0m38\033[91m]\033[93m MX LINUX
\033[91m[\033[0m39\033[91m]\033[93m OPEN INDIANA
\033[91m[\033[0m40\033[91m]\033[93m OPEN MANDRIVA
\033[91m[\033[0m41\033[91m]\033[93m OPEN SUSE
\033[91m[\033[0m42\033[91m]\033[93m OPEN VZ
\033[91m[\033[0m43\033[91m]\033[93m PARABOLA
\033[91m[\033[0m44\033[91m]\033[93m PARROT
\033[91m[\033[0m45\033[91m]\033[93m PENTOO
\033[91m[\033[0m46\033[91m]\033[93m PC LINUX OS
\033[91m[\033[0m47\033[91m]\033[93m PC BSD
\033[91m[\033[0m48\033[91m]\033[93m PUPPY LINUX
\033[91m[\033[0m49\033[91m]\033[93m QUBES
\033[91m[\033[0m50\033[91m]\033[93m REDHAT / RHEL
\033[91m[\033[0m51\033[91m]\033[93m SABAYON
\033[91m[\033[0m52\033[91m]\033[93m SLACKWARE
\033[91m[\033[0m53\033[91m]\033[93m SOLARIS
\033[91m[\033[0m54\033[91m]\033[93m SOLYDXK
\033[91m[\033[0m55\033[91m]\033[93m SOLUS
\033[91m[\033[0m56\033[91m]\033[93m SPARKY LINUX
\033[91m[\033[0m57\033[91m]\033[93m SUSE LINUX
\033[91m[\033[0m58\033[91m]\033[93m TAILS
\033[91m[\033[0m59\033[91m]\033[93m TRIQUEL
\033[91m[\033[0m60\033[91m]\033[93m TRUE OS
\033[91m[\033[0m61\033[91m]\033[93m TURN KEY
\033[91m[\033[0m62\033[91m]\033[93m UBUNTU
\033[91m[\033[0m63\033[91m]\033[93m VOID LINUX
\033[91m[\033[0m64\033[91m]\033[93m XUBUNTU
\033[91m[\033[0m65\033[91m]\033[93m ZORIN OS
\033[91m[\033[0m66\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        Alpine_Linux()
    elif Bang_Jago == "2":
        ALT_Linux()
    elif Bang_Jago == "3":
        AntiX()
    elif Bang_Jago == "4":
        Arch_Linux()
    elif Bang_Jago == "5":
        BeOS()
    elif Bang_Jago == "6":
        BlackArch()
    elif Bang_Jago == "7":
        BlankOn()
    elif Bang_Jago == "8":
        Bodhi_Linux()
    elif Bang_Jago == "9":
        Caldera_OpenLinux()
    elif Bang_Jago == "10":
        Calculate()
    elif Bang_Jago == "11":
        CentOS()
    elif Bang_Jago == "12":
        Chakra_Linux()
    elif Bang_Jago == "13":
        Corel_Linux()
    elif Bang_Jago == "14":
        Debian()
    elif Bang_Jago == "15":
        Deepin()
    elif Bang_Jago == "16":
        DemoLinux()
    elif Bang_Jago == "17":
        DragonFly()
    elif Bang_Jago == "18":
        ElementaryOS()
    elif Bang_Jago == "19":
        EndeavourOS()
    elif Bang_Jago == "20":
        EndlessOS()
    elif Bang_Jago == "21":
        ExTiX()
    elif Bang_Jago == "22":
        Fedora()
    elif Bang_Jago == "23":
        FreeBSD()
    elif Bang_Jago == "24":
        Garuda()
    elif Bang_Jago == "25":
        Gentoo()
    elif Bang_Jago == "26":
        Haiku()
    elif Bang_Jago == "27":
        Kali_Linux()
    elif Bang_Jago == "28":
        Knoppix()
    elif Bang_Jago == "29":
        Kubuntu()
    elif Bang_Jago == "30":
        Linux_Kernel()
    elif Bang_Jago == "31":
        Linux_Mint()
    elif Bang_Jago == "32":
        Lubuntu()
    elif Bang_Jago == "33":
        LuninuxOS()
    elif Bang_Jago == "34":
        Mageia()
    elif Bang_Jago == "35":
        Mandriva()
    elif Bang_Jago == "36":
        Mandrake()
    elif Bang_Jago == "37":
        Manjaro()
    elif Bang_Jago == "38":
        MX_Linux()
    elif Bang_Jago == "39":
        OpenIndiana()
    elif Bang_Jago == "40":
        OpenMandriva()
    elif Bang_Jago == "41":
        OpenSUSE()
    elif Bang_Jago == "42":
        OpenVZ()
    elif Bang_Jago == "43":
        Parabola()
    elif Bang_Jago == "44":
        Parrot()
    elif Bang_Jago == "45":
        Pentoo()
    elif Bang_Jago == "46":
        PCLinuxOS()
    elif Bang_Jago == "47":
        PC_BSD()
    elif Bang_Jago == "48":
        Puppy_Linux()
    elif Bang_Jago == "49":
        Qubes()
    elif Bang_Jago == "50":
        RedHat()
    elif Bang_Jago == "51":
        Sabayon()
    elif Bang_Jago == "52":
        Slackware()
    elif Bang_Jago == "53":
        Solaris()
    elif Bang_Jago == "54":
        SolydXK()
    elif Bang_Jago == "55":
        Solus()
    elif Bang_Jago == "56":
        Sparky_Linux()
    elif Bang_Jago == "57":
        SUSE_Linux()
    elif Bang_Jago == "58":
        Tails()
    elif Bang_Jago == "59":
        Trisquel()
    elif Bang_Jago == "60":
        TrueOS()
    elif Bang_Jago == "61":
        TurnKey()
    elif Bang_Jago == "62":
        Ubuntu()
    elif Bang_Jago == "63":
        Void_Linux()
    elif Bang_Jago == "64":
        Xubuntu()
    elif Bang_Jago == "65":
        ZorinOS()
    elif Bang_Jago == "66":
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM DOWNLOAD FILE ISO LINUX (ARCHIVE)
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


def Alpine_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3d6AR3N"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Alpine_Linux()


def ALT_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d am start -a android.intent.action.VIEW -d https://bit.ly/3tTAvDJ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
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
        ALT_Linux()


def AntiX():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tTjKs9"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        AntiX()


def Arch_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3aWMwQ6"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3s23MdR"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Arch_Linux()


def BeOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        BeOS()


def BlackArch():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b3e7PK"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        BlackArch()


def BlankOn():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rOK5FZ"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5CEU6"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        BlankOn()


def Bodhi_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rQ7ze8"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Bodhi_Linux()


def Caldera_OpenLinux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Caldera_OpenLinux()


def Calculate():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/379SH1Y"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Calculate()


def CentOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rVdVcd"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        CentOS()


def Chakra_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2Oqj0um"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Chakra_Linux()


def Corel_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Corel_Linux()


def Debian():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rTBG4n"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Debian()


def Deepin():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b0fBtX"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/37bBtBr"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Deepin()


def DemoLinux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        DemoLinux()


def DragonFly():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3d8S395"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        DragonFly()


def ElementaryOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2N2gRor"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        ElementaryOS()


def EndeavourOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b0z6Cz"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        EndeavourOS()


def EndlessOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/379mV5r"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        EndlessOS()


def ExTiX():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/37aRyaG"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        ExTiX()


def Fedora():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tVP0XK"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3rTC6Yv"
    url3 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
\033[91m[\033[0m3\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (3)
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
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
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
        Fedora()


def FreeBSD():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        FreeBSD()


def Garuda():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3d5qfSZ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Garuda()


def Gentoo():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/37ciS8n"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Gentoo()


def Haiku():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Haiku()


def Kali_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/379S4Ws"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Kali_Linux()


def Knoppix():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3aWNkEC"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Knoppix()


def Kubuntu():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tWXuxw"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Kubuntu()


def Linux_Kernel():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2MSCTtV"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Linux_Kernel()


def Linux_Mint():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b225Gb"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3ddd6XV"
    url3 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    url4 = "am start -a android.intent.action.VIEW -d https://bit.ly/37aLjDJ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
\033[91m[\033[0m3\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (3)
\033[91m[\033[0m4\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (4)
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
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
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
        Linux_Mint()


def Lubuntu():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3d6a5Zu"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Lubuntu()


def LuninuxOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rUjsjb"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        LuninuxOS()


def Mageia():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2N17q8M"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    url3 = "am start -a android.intent.action.VIEW -d https://bit.ly/37ar6Og"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
\033[91m[\033[0m3\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (3)
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
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
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
        Mageia()


def Mandriva():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Mandriva()


def Mandrake():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Mandrake()


def Manjaro():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3dczctA"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Manjaro()


def MX_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/379S4FE"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3rQcZpj"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        MX_Linux()


def OpenIndiana():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/37arhsU"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        OpenIndiana()


def OpenMandriva():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2MZsCMg"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        OpenMandriva()


def OpenSUSE():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rUkxHL"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3qh16Zj"
    url3 = "am start -a android.intent.action.VIEW -d https://bit.ly/3tWYt0G"
    url4 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    url5 = "am start -a android.intent.action.VIEW -d https://bit.ly/3jJeym2"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
\033[91m[\033[0m3\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (3)
\033[91m[\033[0m4\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (4)
\033[91m[\033[0m5\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (5)
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
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "4":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url4)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "5":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url5)
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
        OpenSUSE()


def OpenVZ():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tRQZfz"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        OpenVZ()


def Parabola():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2MTB0ND"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Parabola()


def Parrot():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3d9LNhm"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Parrot()


def Pentoo():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tVPTQ4"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Pentoo()


def PCLinuxOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3d9Sno0"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        PCLinuxOS()


def PC_BSD():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        PC_BSD()


def Puppy_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b0gXVz"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Puppy_Linux()


def Qubes():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/37cjPNZ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Qubes()


def RedHat():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rOsz4L"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        RedHat()


def Sabayon():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tWaHqs"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Sabayon()


def Slackware():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/37d3Yi6"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    url3 = "am start -a android.intent.action.VIEW -d https://bit.ly/376LWy4"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
\033[91m[\033[0m3\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (3)
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
        os.system(url2)
        Gator_Bks()
        print("\033[37m")
        Balik()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url3)
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
        Slackware()


def Solaris():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Solaris()


def SolydXK():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5zqju"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        SolydXK()


def Solus():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3rMVYMK"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Solus()


def Sparky_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5gC3M"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3tWwzCj"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Sparky_Linux()


def SUSE_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        SUSE_Linux()


def Tails():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3dh1p2i"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/2Oor6nh"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Tails()


def Trisquel():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5zm3e"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Trisquel()


def TrueOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        TrueOS()


def TurnKey():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tUacgJ"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        TurnKey()


def Ubuntu():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2N1hK0y"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Ubuntu()


def Void_Linux():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3phabQq"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        Void_Linux()


def Xubuntu():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3tTlamt"
    url2 = "am start -a android.intent.action.VIEW -d https://bit.ly/3b5xRSE"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (1)
\033[91m[\033[0m2\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!! (2)
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
        os.system(url2)
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
        Xubuntu()


def ZorinOS():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/2Oyyw7I"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD SEKARANG\033[91m!!
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
        ZorinOS()


if __name__ == '__main__':
    NFZ()