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
from Mulai import NFZ as Mulai


Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Pesan = "\033[92m[\033[93m+\033[92m]\033[93m Harap Bersabar Sedang Memuat Data Terbaru"


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
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 GLOBAL
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 GLOBAL (NEGARA)
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 GLOBAL (PROVINSI SETIAP NEGARA)
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Global()
    elif Bang_Jago == "2":
        covid_Negara()
    elif Bang_Jago == "3":
        covid_ProvinsiNegara()
    elif Bang_Jago == "4":
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
    print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM DATA COVID 19 SAAT INI
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


def covid_Global():
    Loading()
    Gator_Bks()
    try:
        url = "https://api.coronatracker.com/v3/stats/worldometer/global"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 GLOBAL")
        print("\n")
        print(f"\033[93mTotal Cases      :\033[92m {nadhiffz['totalConfirmed']}")
        print(f"\033[93mActive Cases     :\033[92m {nadhiffz['totalActiveCases']}")
        print(f"\033[93mNew Cases        :\033[92m {nadhiffz['totalNewCases']}")
        print(f"\033[93mTotal Recovered  :\033[92m {nadhiffz['totalRecovered']}")
        print(f"\033[93mTotal Deaths     :\033[92m {nadhiffz['totalDeaths']}")
        print(f"\033[93mNew Deaths       :\033[92m {nadhiffz['totalNewDeaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Negara():
    Loading()
    Gator_Bks()
    try:
        url = "https://api.coronatracker.com/v3/stats/worldometer/country"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 GLOBAL (NEGARA)")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mCountry Name     :\033[97m {data['countryName']}")
            print(f"\033[93mTotal Cases      :\033[92m {data['totalConfirmed']}")
            print(f"\033[93mActive Cases     :\033[92m {data['activeCases']}")
            print(f"\033[93mTotal Recovered  :\033[92m {data['totalRecovered']}")
            print(f"\033[93mTotal Critical   :\033[92m {data['totalCritical']}")
            print(f"\033[93mTotal Deaths     :\033[92m {data['totalDeaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_ProvinsiNegara():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA A
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA B
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA C
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA D
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA E
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA F
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA G
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA H
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA I
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA J
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA K
\033[91m[\033[0m12\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA L
\033[91m[\033[0m13\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA M
\033[91m[\033[0m14\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA N
\033[91m[\033[0m15\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA O
\033[91m[\033[0m16\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA P
\033[91m[\033[0m17\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA Q
\033[91m[\033[0m18\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA R
\033[91m[\033[0m19\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA S
\033[91m[\033[0m20\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA T
\033[91m[\033[0m21\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA U
\033[91m[\033[0m22\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA V
\033[91m[\033[0m23\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA W
\033[91m[\033[0m24\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA Y
\033[91m[\033[0m25\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA Z
\033[91m[\033[0m26\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1" or Bang_Jago == "a" or Bang_Jago == "A":
        covid_ProvinsiNegara_A()
    elif Bang_Jago == "2" or Bang_Jago == "b" or Bang_Jago == "B":
        covid_ProvinsiNegara_B()
    elif Bang_Jago == "3" or Bang_Jago == "c" or Bang_Jago == "C":
        covid_ProvinsiNegara_C()
    elif Bang_Jago == "4" or Bang_Jago == "d" or Bang_Jago == "D":
        covid_ProvinsiNegara_D()
    elif Bang_Jago == "5" or Bang_Jago == "e" or Bang_Jago == "E":
        covid_ProvinsiNegara_E()
    elif Bang_Jago == "6" or Bang_Jago == "f" or Bang_Jago == "F":
        covid_ProvinsiNegara_F()
    elif Bang_Jago == "7" or Bang_Jago == "g" or Bang_Jago == "G":
        covid_ProvinsiNegara_G()
    elif Bang_Jago == "8" or Bang_Jago == "h" or Bang_Jago == "H":
        covid_ProvinsiNegara_H()
    elif Bang_Jago == "9" or Bang_Jago == "i" or Bang_Jago == "I":
        covid_ProvinsiNegara_I()
    elif Bang_Jago == "10" or Bang_Jago == "j" or Bang_Jago == "J":
        covid_ProvinsiNegara_J()
    elif Bang_Jago == "11" or Bang_Jago == "k" or Bang_Jago == "K":
        covid_ProvinsiNegara_K()
    elif Bang_Jago == "12" or Bang_Jago == "l" or Bang_Jago == "L":
        covid_ProvinsiNegara_L()
    elif Bang_Jago == "13" or Bang_Jago == "m" or Bang_Jago == "M":
        covid_ProvinsiNegara_M()
    elif Bang_Jago == "14" or Bang_Jago == "n" or Bang_Jago == "N":
        covid_ProvinsiNegara_N()
    elif Bang_Jago == "15" or Bang_Jago == "o" or Bang_Jago == "O":
        covid_ProvinsiNegara_O()
    elif Bang_Jago == "16" or Bang_Jago == "p" or Bang_Jago == "P":
        covid_ProvinsiNegara_P()
    elif Bang_Jago == "17" or Bang_Jago == "q" or Bang_Jago == "Q":
        covid_ProvinsiNegara_Q()
    elif Bang_Jago == "18" or Bang_Jago == "r" or Bang_Jago == "R":
        covid_ProvinsiNegara_R()
    elif Bang_Jago == "19" or Bang_Jago == "s" or Bang_Jago == "S":
        covid_ProvinsiNegara_S()
    elif Bang_Jago == "20" or Bang_Jago == "t" or Bang_Jago == "T":
        covid_ProvinsiNegara_T()
    elif Bang_Jago == "21" or Bang_Jago == "u" or Bang_Jago == "U":
        covid_ProvinsiNegara_U()
    elif Bang_Jago == "22" or Bang_Jago == "v" or Bang_Jago == "V":
        covid_ProvinsiNegara_V()
    elif Bang_Jago == "23" or Bang_Jago == "w" or Bang_Jago == "W":
        covid_ProvinsiNegara_W()
    elif Bang_Jago == "24" or Bang_Jago == "y" or Bang_Jago == "Y":
        covid_ProvinsiNegara_Y()
    elif Bang_Jago == "25" or Bang_Jago == "z" or Bang_Jago == "Z":
        covid_ProvinsiNegara_Z()
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
        NFZ()


def covid_ProvinsiNegara_A():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA AFGHANISTAN
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ALBANIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ALGERIA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ANDORRA
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ANGOLA
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ANTIGUA AND BARBUDA
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ARGENTINA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ARMENIA
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA AUSTRALIA
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA AUSTRIA
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA AZERBAIJAN
\033[91m[\033[0m12\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m13\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Afghanistan()
    elif Bang_Jago == "2":
        covid_Albania()
    elif Bang_Jago == "3":
        covid_Algeria()
    elif Bang_Jago == "4":
        covid_Andorra()
    elif Bang_Jago == "5":
        covid_Angola()
    elif Bang_Jago == "6":
        covid_Antigua()
    elif Bang_Jago == "7":
        covid_Argentina()
    elif Bang_Jago == "8":
        covid_Armenia()
    elif Bang_Jago == "9":
        covid_Australia()
    elif Bang_Jago == "10":
        covid_Austria()
    elif Bang_Jago == "11":
        covid_Azerbaijan()
    elif Bang_Jago == "12":
        NFZ()
    elif Bang_Jago == "13":
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


def covid_ProvinsiNegara_B():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BAHAMAS
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BAHRAIN
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BANGLADESH
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BARBADOS
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BELARUS
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BELGIUM
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BELIZE
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BENIN
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BHUTAN
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BOLIVIA
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BOSNIA AND HERZEGOVINA
\033[91m[\033[0m12\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BOTSWANA
\033[91m[\033[0m13\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BRAZIL
\033[91m[\033[0m14\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BRUNEI
\033[91m[\033[0m15\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BULGARIA
\033[91m[\033[0m16\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BURKINA FASO
\033[91m[\033[0m17\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BURMA
\033[91m[\033[0m18\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA BURUNDI
\033[91m[\033[0m19\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m20\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Bahamas()
    elif Bang_Jago == "2":
        covid_Bahrain()
    elif Bang_Jago == "3":
        covid_Bangladesh()
    elif Bang_Jago == "4":
        covid_Barbados()
    elif Bang_Jago == "5":
        covid_Belarus()
    elif Bang_Jago == "6":
        covid_Belgium()
    elif Bang_Jago == "7":
        covid_Belize()
    elif Bang_Jago == "8":
        covid_Benin()
    elif Bang_Jago == "9":
        covid_Bhutan()
    elif Bang_Jago == "10":
        covid_Bolivia()
    elif Bang_Jago == "11":
        covid_Bosnia()
    elif Bang_Jago == "12":
        covid_Botswana()
    elif Bang_Jago == "13":
        covid_Brazil()
    elif Bang_Jago == "14":
        covid_Brunei()
    elif Bang_Jago == "15":
        covid_Bulgaria()
    elif Bang_Jago == "16":
        covid_Burkina()
    elif Bang_Jago == "17":
        covid_Burma()
    elif Bang_Jago == "18":
        covid_Burundi()
    elif Bang_Jago == "19":
        NFZ()
    elif Bang_Jago == "20":
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


def covid_ProvinsiNegara_C():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CAMBODIA
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CAMEROON
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CANADA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CENTRAL AFRICAN REPUBLIC
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CHAD
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CHILE
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CHINA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA COLOMBIA
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA COMOROS
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA COSTA RICA
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CROATIA
\033[91m[\033[0m12\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CUBA
\033[91m[\033[0m13\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CYPRUS
\033[91m[\033[0m14\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA CZECHIA
\033[91m[\033[0m15\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m16\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Cambodia()
    elif Bang_Jago == "2":
        covid_Cameroon()
    elif Bang_Jago == "3":
        covid_Canada()
    elif Bang_Jago == "4":
        covid_Central()
    elif Bang_Jago == "5":
        covid_Chad()
    elif Bang_Jago == "6":
        covid_Chile()
    elif Bang_Jago == "7":
        covid_China()
    elif Bang_Jago == "8":
        covid_Colombia()
    elif Bang_Jago == "9":
        covid_Comoros()
    elif Bang_Jago == "10":
        covid_Costa()
    elif Bang_Jago == "11":
        covid_Croatia()
    elif Bang_Jago == "12":
        covid_Cuba()
    elif Bang_Jago == "13":
        covid_Cyprus()
    elif Bang_Jago == "14":
        covid_Czechia()
    elif Bang_Jago == "15":
        NFZ()
    elif Bang_Jago == "16":
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


def covid_ProvinsiNegara_D():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA DENMARK
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA DJIBOUTI
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA DOMINICA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA DOMINICAN REPUBLIC
\033[91m[\033[0m5\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m6\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Denmark()
    elif Bang_Jago == "2":
        covid_Djibouti()
    elif Bang_Jago == "3":
        covid_Dominica()
    elif Bang_Jago == "4":
        covid_Dominican()
    elif Bang_Jago == "5":
        NFZ()
    elif Bang_Jago == "6":
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


def covid_ProvinsiNegara_E():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ECUADOR
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA EGYPT
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA EL SAVADOR
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA EQUATORIAL GUINEA
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ERITREA
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ESTONIA
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ESWATINI
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ETHIOPIA
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Ecuador()
    elif Bang_Jago == "2":
        covid_Egypt()
    elif Bang_Jago == "3":
        covid_El()
    elif Bang_Jago == "4":
        covid_Equatorial()
    elif Bang_Jago == "5":
        covid_Eritrea()
    elif Bang_Jago == "6":
        covid_Estonia()
    elif Bang_Jago == "7":
        covid_Eswatini()
    elif Bang_Jago == "8":
        covid_Ethiopia()
    elif Bang_Jago == "9":
        NFZ()
    elif Bang_Jago == "10":
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


def covid_ProvinsiNegara_F():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA FIJI
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA FINLAND
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA FRANCE
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Fiji()
    elif Bang_Jago == "2":
        covid_Finland()
    elif Bang_Jago == "3":
        covid_France()
    elif Bang_Jago == "4":
        NFZ()
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


def covid_ProvinsiNegara_G():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GABON
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GEORGIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GERMANY
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GHANA
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GREECE
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GRENADA
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GUATEMALA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GUINEA
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GUINEA-BISSAU
\033[91m[\033[0m10\033\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA GUYANA
\033[91m[\033[0m11\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m12\033\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Gabon()
    elif Bang_Jago == "2":
        covid_Georgia()
    elif Bang_Jago == "3":
        covid_Germany()
    elif Bang_Jago == "4":
        covid_Ghana()
    elif Bang_Jago == "5":
        covid_Greece()
    elif Bang_Jago == "6":
        covid_Grenada()
    elif Bang_Jago == "7":
        covid_Guatemala()
    elif Bang_Jago == "8":
        covid_Guinea()
    elif Bang_Jago == "9":
        covid_GB()
    elif Bang_Jago == "10":
        covid_Guyana()
    elif Bang_Jago == "11":
        NFZ()
    elif Bang_Jago == "12":
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


def covid_ProvinsiNegara_H():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA HAITI
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA HONDURAS
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA HUNGARY
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Haiti()
    elif Bang_Jago == "2":
        covid_Honduras()
    elif Bang_Jago == "3":
        covid_Hungary()
    elif Bang_Jago == "4":
        NFZ()
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


def covid_ProvinsiNegara_I():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ICELAND
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA INDIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA INDONESIA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA IRAN
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA IRAQ
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA IRELAND
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ISRAEL
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ITALY
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Iceland()
    elif Bang_Jago == "2":
        covid_India()
    elif Bang_Jago == "3":
        covid_Indonesia()
    elif Bang_Jago == "4":
        covid_Iran()
    elif Bang_Jago == "5":
        covid_Iraq()
    elif Bang_Jago == "6":
        covid_Ireland()
    elif Bang_Jago == "7":
        covid_Israel()
    elif Bang_Jago == "8":
        covid_Italy()
    elif Bang_Jago == "9":
        NFZ()
    elif Bang_Jago == "10":
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


def covid_ProvinsiNegara_J():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA JAMAICA
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA JAPAN
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA JORDAN
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Jamaica()
    elif Bang_Jago == "2":
        covid_Japan()
    elif Bang_Jago == "3":
        covid_Jordan()
    elif Bang_Jago == "4":
        NFZ()
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


def covid_ProvinsiNegara_K():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA KAZAKHSTAN
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA KENYA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA KOSOVO
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA KUWAIT
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA KYRGYZSTAN
\033[91m[\033[0m6\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m7\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Kazakhstan()
    elif Bang_Jago == "2":
        covid_Kenya()
    elif Bang_Jago == "3":
        covid_Kosovo()
    elif Bang_Jago == "4":
        covid_Kuwait()
    elif Bang_Jago == "5":
        covid_Kyrgyzstan()
    elif Bang_Jago == "6":
        NFZ()
    elif Bang_Jago == "7":
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


def covid_ProvinsiNegara_L():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LAOS
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LATVIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LEBANON
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LESOTHO
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LIBERIA
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LIBYA
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LIECHTENSTEIN
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LITHUANIA
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA LUXEMBOURG
\033[91m[\033[0m10\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m11\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Laos()
    elif Bang_Jago == "2":
        covid_Latvia()
    elif Bang_Jago == "3":
        covid_Lebanon()
    elif Bang_Jago == "4":
        covid_Lesotho()
    elif Bang_Jago == "5":
        covid_Liberia()
    elif Bang_Jago == "6":
        covid_Libya()
    elif Bang_Jago == "7":
        covid_Liechtenstein()
    elif Bang_Jago == "8":
        covid_Lithuania()
    elif Bang_Jago == "9":
        covid_Luxembourg()
    elif Bang_Jago == "10":
        NFZ()
    elif Bang_Jago == "11":
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


def covid_ProvinsiNegara_M():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MADAGASCAR
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MALAYSIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MALDIVES
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MALI
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MALTA
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MARSHALL ISLANDS
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MAURITANIA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MAURITIUS
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MEXICO
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MICRONESIA
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MOLDOVA
\033[91m[\033[0m12\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MONACO
\033[91m[\033[0m13\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MONGOLIA
\033[91m[\033[0m14\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MONTENEGRO
\033[91m[\033[0m15\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MOROCCO
\033[91m[\033[0m16\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA MOZAMBIQUE
\033[91m[\033[0m17\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m18\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Madagascar()
    elif Bang_Jago == "2":
        covid_Malaysia()
    elif Bang_Jago == "3":
        covid_Maldives()
    elif Bang_Jago == "4":
        covid_Mali()
    elif Bang_Jago == "5":
        covid_Malta()
    elif Bang_Jago == "6":
        covid_Marshall()
    elif Bang_Jago == "7":
        covid_Mauritania()
    elif Bang_Jago == "8":
        covid_Mauritius()
    elif Bang_Jago == "9":
        covid_Mexico()
    elif Bang_Jago == "10":
        covid_Micronesia()
    elif Bang_Jago == "11":
        covid_Moldova()
    elif Bang_Jago == "12":
        covid_Monaco()
    elif Bang_Jago == "13":
        covid_Mongolia()
    elif Bang_Jago == "14":
        covid_Montenegro()
    elif Bang_Jago == "15":
        covid_Morocco()
    elif Bang_Jago == "16":
        covid_Mozambique()
    elif Bang_Jago == "17":
        NFZ()
    elif Bang_Jago == "18":
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


def covid_ProvinsiNegara_N():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NAMIBIA
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NEPAL
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NETHERLANDS
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NEW ZEALAND
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NICARAGUA
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NIGER
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NIGERIA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA NORWAY
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Namibia()
    elif Bang_Jago == "2":
        covid_Nepal()
    elif Bang_Jago == "3":
        covid_Netherlands()
    elif Bang_Jago == "4":
        covid_New()
    elif Bang_Jago == "5":
        covid_Nicaragua()
    elif Bang_Jago == "6":
        covid_Niger()
    elif Bang_Jago == "7":
        covid_Nigeria()
    elif Bang_Jago == "8":
        covid_Norway()
    elif Bang_Jago == "9":
        NFZ()
    elif Bang_Jago == "10":
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


def covid_ProvinsiNegara_O():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA OMAN
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m2\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Oman()
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


def covid_ProvinsiNegara_P():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PAKISTAN
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PANAMA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PAPUA NEW GUINEA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PARAGUAY
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PERU
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PHILIPPINES
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA POLAND
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA PORTUGAL
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Pakistan()
    elif Bang_Jago == "2":
        covid_Panama()
    elif Bang_Jago == "3":
        covid_Papua()
    elif Bang_Jago == "4":
        covid_Paraguay()
    elif Bang_Jago == "5":
        covid_Peru()
    elif Bang_Jago == "6":
        covid_Philippines()
    elif Bang_Jago == "7":
        covid_Poland()
    elif Bang_Jago == "8":
        covid_Portugal()
    elif Bang_Jago == "9":
        NFZ()
    elif Bang_Jago == "10":
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


def covid_ProvinsiNegara_Q():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA QATAR
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Qatar()
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


def covid_ProvinsiNegara_R():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ROMANIA
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA RUSSIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA RWANDA
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Romania()
    elif Bang_Jago == "2":
        covid_Russia()
    elif Bang_Jago == "3":
        covid_Rwanda()
    elif Bang_Jago == "4":
        NFZ()
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


def covid_ProvinsiNegara_S():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAINT KITTS AND NEVIS
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAINT LUCIA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAINT VINCENT AND THE GRENADIES
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAMOA
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAN MARINO
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAO TOME AND PRINCIPE
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SAUDI ARABIA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SENEGAL
\033[91m[\033[0m9\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SERBIA
\033[91m[\033[0m10\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SEYCHELLES
\033[91m[\033[0m11\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SIERRA LEONE
\033[91m[\033[0m12\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SINGAPORE
\033[91m[\033[0m13\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SLOVAKIA
\033[91m[\033[0m14\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SLOVENIA
\033[91m[\033[0m15\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SOLOMON
\033[91m[\033[0m16\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SOMALIA
\033[91m[\033[0m17\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SOUTH AFRICA
\033[91m[\033[0m18\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SOUTH KOREA
\033[91m[\033[0m19\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SOUTH SUDAN
\033[91m[\033[0m20\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SPAIN
\033[91m[\033[0m21\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SRI LANKA
\033[91m[\033[0m22\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SUDAN
\033[91m[\033[0m23\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SURINAME
\033[91m[\033[0m24\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SWEDEN
\033[91m[\033[0m25\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SWITZERLAND
\033[91m[\033[0m26\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA SYRIA
\033[91m[\033[0m27\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m28\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_SKN()
    elif Bang_Jago == "2":
        covid_SL()
    elif Bang_Jago == "3":
        covid_SVG()
    elif Bang_Jago == "4":
        covid_Samoa()
    elif Bang_Jago == "5":
        covid_San()
    elif Bang_Jago == "6":
        covid_Sao()
    elif Bang_Jago == "7":
        covid_Saudi()
    elif Bang_Jago == "8":
        covid_Senegal()
    elif Bang_Jago == "9":
        covid_Serbia()
    elif Bang_Jago == "10":
        covid_Seychelles()
    elif Bang_Jago == "11":
        covid_Sierra()
    elif Bang_Jago == "12":
        covid_Singapore()
    elif Bang_Jago == "13":
        covid_Slovakia()
    elif Bang_Jago == "14":
        covid_Slovenia()
    elif Bang_Jago == "15":
        covid_Solomon()
    elif Bang_Jago == "16":
        covid_Somalia()
    elif Bang_Jago == "17":
        covid_SA()
    elif Bang_Jago == "18":
        covid_SK()
    elif Bang_Jago == "19":
        covid_SS()
    elif Bang_Jago == "20":
        covid_Spain()
    elif Bang_Jago == "21":
        covid_Sri()
    elif Bang_Jago == "22":
        covid_Sudan()
    elif Bang_Jago == "23":
        covid_Suriname()
    elif Bang_Jago == "24":
        covid_Sweden()
    elif Bang_Jago == "25":
        covid_Switzerland()
    elif Bang_Jago == "26":
        covid_Syria()
    elif Bang_Jago == "27":
        NFZ()
    elif Bang_Jago == "28":
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


def covid_ProvinsiNegara_T():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TAIWAN
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TAJIKISTAN
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TANZANIA
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA THAILAND
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TOGO
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TRINIDAD AND TOBAGO
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TUNISIA
\033[91m[\033[0m8\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA TURKEY
\033[91m[\033[0m9\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m10\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Taiwan()
    elif Bang_Jago == "2":
        covid_Tajikistan()
    elif Bang_Jago == "3":
        covid_Tanzania()
    elif Bang_Jago == "4":
        covid_Thailand()
    elif Bang_Jago == "5":
        covid_Togo()
    elif Bang_Jago == "6":
        covid_Trinidad()
    elif Bang_Jago == "7":
        covid_Tunisia()
    elif Bang_Jago == "8":
        covid_Turkey()
    elif Bang_Jago == "9":
        NFZ()
    elif Bang_Jago == "10":
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


def covid_ProvinsiNegara_U():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI UNITED STATES
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA UGANDA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA UKRAINE
\033[91m[\033[0m4\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA UNITED ARAB EMIRATES
\033[91m[\033[0m5\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA UNITED KINGDOM
\033[91m[\033[0m6\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA URUGUAY
\033[91m[\033[0m7\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA UZBEKISTAN
\033[91m[\033[0m8\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m9\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_US()
    elif Bang_Jago == "2":
        covid_Uganda()
    elif Bang_Jago == "3":
        covid_Ukraine()
    elif Bang_Jago == "4":
        covid_UAE()
    elif Bang_Jago == "5":
        covid_UK()
    elif Bang_Jago == "6":
        covid_Uruguay()
    elif Bang_Jago == "7":
        covid_Uzbekistan()
    elif Bang_Jago == "8":
        NFZ()
    elif Bang_Jago == "9":
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


def covid_ProvinsiNegara_V():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI VANUATU
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA VENEZUELA
\033[91m[\033[0m3\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA VIETNAM
\033[91m[\033[0m4\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m5\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Vanuatu()
    elif Bang_Jago == "2":
        covid_Venezuela()
    elif Bang_Jago == "3":
        covid_Vietnam()
    elif Bang_Jago == "4":
        NFZ()
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


def covid_ProvinsiNegara_W():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI WEST BANK AND GAZA
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_West()
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


def covid_ProvinsiNegara_Y():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI YEMEN
\033[91m[\033[0m2\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Yemen()
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


def covid_ProvinsiNegara_Z():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 PROVINSI ZAMBIA
\033[91m[\033[0m2\033[91m]\033[93m DATA COVID 19 PROVINSI NEGARA ZIMBABWE
\033[91m[\033[0m3\033[91m]\033[97m KEMBALI KE MENU AWAL
\033[91m[\033[0m4\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Zambia()
    elif Bang_Jago == "2":
        covid_Zimbabwe()
    elif Bang_Jago == "3":
        NFZ()
    elif Bang_Jago == "4":
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


def covid_Afghanistan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Afghanistan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN AFGHANISTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Albania():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Albania/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ALBANIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Algeria():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Algeria/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ALGERIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Andorra():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Andorra/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ANDORRA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Angola():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Angola/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ANGOLA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Antigua():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/ATG/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ANTIGUA AND BARBUDA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Argentina():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Argentina/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ARGENTINA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Armenia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Armenia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ARMENIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Australia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Australia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN AUSTRALIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Austria():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Austria/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN AUSTRIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Azerbaijan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Azerbaijan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN AZERBAIJAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bahamas():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Bahamas/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BAHAMAS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bahrain():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Bahrain/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BAHRAIN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bangladesh():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Bangladesh/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BANGLADESH")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Barbados():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Barbados/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BARBADOS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Barbados():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Barbados/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BARBADOS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Belarus():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Belarus/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BELARUS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Belgium():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Belgium/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BELGIUM")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Belize():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Belize/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BELIZE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Benin():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Benin/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BENIN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bhutan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Bhutan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BHUTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bolivia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/BA/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BOLIVIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bosnia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/BIH/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BOSNIA AND HERZEGOVINA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Botswana():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Botswana/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BOTSWANA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Brazil():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Brazil/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BRAZIL")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Brunei():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Brunei/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BRUNEI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Bulgaria():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Bulgaria/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BULGARIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Burkina():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/BF/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BURKINA FASO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Burma():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Burma/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BURMA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Burundi():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Burundi/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN BURUNDI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Cambodia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Cambodia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CAMBODIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Cameroon():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Cameroon/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CAMEROON")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Canada():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Canada/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CANADA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Central():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/CF/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CENTRAL AFRICAN REPUBLIC")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Chad():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Chad/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CHAD")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Chile():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Chile/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CHILE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_China():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/China/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CHINA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Colombia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Colombia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN COLOMBIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Comoros():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Comoros/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN COMOROS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Costa():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/CR/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN COSTA RICA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Croatia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Croatia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CROATIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Cuba():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Cuba/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CUBA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Cyprus():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Cyprus/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CYPRUS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Czechia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Czechia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN CZECHIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Denmark():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Denmark/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN DENMARK")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Djibouti():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Djibouti/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN DJIBOUTI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Dominica():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Dominica/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN DOMINICA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Dominican():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/DO/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN DOMINICAN REPUBLIC")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Ecuador():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Ecuador/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ECUADOR")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Egypt():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Egypt/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN EGYPT")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_El():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/SLV/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN EL SAVADOR")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Equatorial():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/GQ/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN EQUATORIAL GUINEA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Eritrea():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Eritrea/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ERITREA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Estonia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Estonia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ESTONIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Eswatini():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Eswatini/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ESWATINI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Ethiopia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Ethiopia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ETHIOPIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Fiji():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Fiji/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN FIJI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Finland():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Finland/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN FINLAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_France():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/France/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN FRANCE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Gabon():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Gabon/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GABON")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Georgia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Georgia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GEORGIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Germany():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Germany/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GERMANY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Ghana():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Ghana/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GHANA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Greece():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Greece/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GREECE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Grenada():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Grenada/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GRENADA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Guatemala():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Guatemala/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GUATEMALA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Guinea():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Guinea/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GUINEA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_GB():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/GNB/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GUINEA-BISSAU")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Guyana():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Guyana/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN GUYANA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Haiti():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Haiti/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN HAITI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Honduras():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Honduras/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN HONDURAS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Hungary():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Hungary/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN HUNGARY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Iceland():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Iceland/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ICELAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_India():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/India/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN INDIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Indonesia():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m DATA COVID 19 SETIAP PROVINSI DI INDONESIA
\033[91m[\033[0m2\033[91m]\033[93m DAFTAR RUMAH SAKIT DI INDONESIA
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if Bang_Jago == "1":
        covid_Indo()
    elif Bang_Jago == "2":
        RumahSakit_Indonesia()
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
        covid_Indonesia()


def covid_Indo():
    Loading()
    Gator_Bks()
    try:
        url = "https://dekontaminasi.com/api/id/covid19/stats"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 DI INDONESIA")
        for data in nadhiffz['regions']:
            print("\n")
            print(f"\033[93mProvinsi       :\033[97m {data['name']}")
            print(f"\033[93mTerkonfirmasi  :\033[92m {data['numbers']['infected']}")
            print(f"\033[93mSembuh         :\033[92m {data['numbers']['recovered']}")
            print(f"\033[93mMeninggal      :\033[92m {data['numbers']['fatal']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def RumahSakit_Indonesia():
    Loading()
    Gator_Bks()
    try:
        url = "https://dekontaminasi.com/api/id/covid19/hospitals"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDAFTAR RUMAH SAKIT DI INDONESIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mNama    :\033[97m {data['name']}")
            print(f"\033[93mAlamat  :\033[92m {data['address']}")
            print(f"\033[93mWilayah :\033[92m {data['region']}")
            print(f"\033[93mTelepon :\033[92m {data['phone']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Iran():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Iran/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN IRAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Iraq():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Iraq/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN IRAQ")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Ireland():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Ireland/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN IRELAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Israel():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Israel/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ISRAEL")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Italy():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Italy/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ITALY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Jamaica():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Jamaica/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN JAMAICA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Japan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Japan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN JAPAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Jordan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Jordan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN JORDAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Kazakhstan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Kazakhstan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN KAZAKHSTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Kenya():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Kenya/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN KENYA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Kosovo():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Kosovo/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN KOSOVO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Kuwait():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Kuwait/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN KUWAIT")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Kyrgyzstan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Kyrgyzstan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN KYRGYZSTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Laos():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Laos/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LAOS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Latvia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Latvia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LATVIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Lebanon():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Lebanon/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LEBANON")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Lesotho():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Lesotho/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LESOTHO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Liberia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Liberia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LIBERIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Libya():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Libya/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LIBYA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Liechtenstein():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Liechtenstein/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LIECHTENSTEIN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Lithuania():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Lithuania/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LITHUANIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Luxembourg():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Luxembourg/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN LUXEMBOURG")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Madagascar():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Madagascar/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MADAGASCAR")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Malaysia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Malaysia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MALAYSIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Maldives():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Maldives/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MALDIVES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mali():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mali/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MALI")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Malta():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Malta/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MALTA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Marshall():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/MHL/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MARSHALL ISLANDS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mauritania():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mauritania/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MAURITANIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mauritius():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mauritius/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MAURITIUS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mexico():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mexico/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MEXICO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Micronesia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Micronesia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MICRONESIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Moldova():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Moldova/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MOLDOVA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Monaco():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Monaco/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MONACO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mongolia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mongolia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MONGOLIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Montenegro():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Montenegro/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MONTENEGRO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Morocco():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Morocco/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MOROCCO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Mozambique():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Mozambique/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN MOZAMBIQUE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Namibia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Namibia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NAMIBIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Nepal():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Nepal/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NEPAL")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Netherlands():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Netherlands/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NETHERLANDS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_New():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/NZ/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NEW ZEALAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Nicaragua():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Nicaragua/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NICARAGUA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Niger():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Niger/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NIGER")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Nigeria():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Nigeria/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NIGERIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Norway():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Norway/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN NORWAY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Oman():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Oman/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN OMAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Pakistan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Pakistan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PAKISTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Panama():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Panama/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PANAMA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Papua():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/PNG/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PAPUA NEW GUINEA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Paraguay():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Paraguay/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PARAGUAY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Peru():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Peru/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PERU")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Philippines():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Philippines/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PHILIPPINES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Poland():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Poland/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN POLAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Portugal():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Portugal/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN PORTUGAL")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Qatar():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Qatar/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN QATAR")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Romania():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Romania/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ROMANIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Russia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Russia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN RUSSIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Rwanda():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Rwanda/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN RWANDA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SKN():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/KNA/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAINT KITTS NEVIS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SL():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/LCA/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAINT LUCIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SVG():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/VCT/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAINT VINCENT AND GRENADIES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Samoa():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Samoa/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAMOA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_San():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/SM/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAN MARINO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Sao():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/STP/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAO TOME AND PRINCIPE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Saudi():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/STP/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SAUDI ARABIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Senegal():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Senegal/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SENEGAL")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Serbia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Serbia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SERBIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Seychelles():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Seychelles/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SEYCHELLES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Sierra():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/SL/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SIERRA LEONE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Singapore():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Singapore/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SINGAPORE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Slovakia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Slovakia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SLOVAKIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Slovenia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Slovenia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SLOVENIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Solomon():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/SLB/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOLOMON ISLANDS")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Somalia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Somalia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOMALIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SA():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/ZAF/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOUTH AFRICA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SK():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/KOR/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOUTH KOREA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_SS():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/SS/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOUTH SUDAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Spain():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Spain/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SOUTH SPAIN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Sri():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/LKA/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SRI LANKA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Sudan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Sudan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SUDAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Suriname():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Suriname/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SURINAME")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Sweden():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Sweden/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SWEDEN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Switzerland():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Switzerland/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SWITZERLAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Syria():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Syria/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN SYRIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Taiwan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Taiwan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TAIWAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Tajikistan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Tajikistan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TAJIKISTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Tanzania():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Tanzania/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TANZANIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Thailand():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Thailand/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN THAILAND")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Togo():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Togo/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TOGO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Trinidad():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/TT/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TRINIDAD AND TOBAGO")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Tunisia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Tunisia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TUNISIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Turkey():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Turkey/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN TURKEY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_US():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/US/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UNITED STATES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Uganda():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Uganda/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UGANDA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Ukraine():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Ukraine/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UKRAINE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_UAE():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/ARE/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UNITED ARAB EMIRATES")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_UK():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/GBR/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UNITED KINGDOM")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Uruguay():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Uruguay/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN URUGUAY")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Uzbekistan():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Uzbekistan/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN UZBEKISTAN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Vanuatu():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Vanuatu/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN VANUATU")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Venezuela():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Venezuela/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN VENEZUELA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Vietnam():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Vietnam/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN VIETNAM")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_West():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/West%20Bank%20and%20Gaza/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN WEST BANK AND GAZA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Yemen():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Yemen/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN YEMEN")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Zambia():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Zambia/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ZAMBIA")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


def covid_Zimbabwe():
    Loading()
    Gator_Bks()
    try:
        url = "https://covid19.mathdro.id/api/countries/Zimbabwe/confirmed"
        gatorbks = request.urlopen(url)
        nadhiffz = json.loads(gatorbks.read())
        print("\033[96mDATA COVID 19 IN ZIMBABWE")
        for data in nadhiffz:
            print("\n")
            print(f"\033[93mProvince  :\033[97m {data['provinceState']}")
            print(f"\033[93mConfirmed :\033[92m {data['confirmed']}")
            print(f"\033[93mActive    :\033[92m {data['active']}")
            print(f"\033[93mRecovered :\033[92m {data['recovered']}")
            print(f"\033[93mDeaths    :\033[92m {data['deaths']}")
        print("\033[37m")
        Balik()
    except ValueError:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()
    except:
        print("\033[93mServer Is Down")
        print("\033[92mPlease Try Again Later ●‿○")
        print("\033[37m")
        Balik()


if __name__ == '__main__':
    NFZ()