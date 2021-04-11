#!/usr/bin/env python
#coding: utf-8


import codecs
import binascii
import sys
import os
import time
from time import sleep
from Program.Mulai import NFZ as Mulai


Kal = time.strftime("%d-%m-%Y")
Clears = "clear"
Author = "\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks"
Thanks = "\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○"
Wrongs = "\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Pilihan Dengan Benar!!!"
Pesan = "\033[92m[\033[93m+\033[92m]\033[93m Sebentar Lagi Anda Akan Dialihkan Ke Browser"
Install = """termux-setup-storage
apt update && pkg upgrade -y
pkg update && pkg upgrade -y
apt install git -y
pkg install git -y
apt install bash -y
pkg install bash -y
apt install python -y
pkg install python -y
apt install python2 -y
pkg install python2 -y
apt install python3 -y
pkg install python3 -y
apt install cmatrix -y
pkg install cmatrix -y
apt install libcaca -y
pkg install libcaca -y
apt install sl -y
pkg install sl -y
apt install neofetch -y
pkg install neofetch -y
pkg install tqdm -y
apt install tqdm -y
apt install api-termux -y
pkg install api-termux -y
pip install -r requirements.txt
pip2 install -r requirements.txt
pip install requests
pip install mechanize
pip2 install requests
pip2 install mechanize
pip2 install requests mechanize tqdm
pip2 install --upgrade pip
pip install pytube
python -m install pytube
python -m install git+https://github.com/pytube/pytube
apt install -y git zsh -y
pkg install -y git zsh -y

git clone https://github.com/Cabbagec/termux-ohmyzsh.git "$HOME/termux-ohmyzsh" --depth 1

mv "$HOME/.termux" "$HOME/.termux.bak.$(date +%Y.%m.%d-%H:%M:%S)"
cp -R "$HOME/termux-ohmyzsh/.termux" "$HOME/.termux"

git clone git://github.com/robbyrussell/oh-my-zsh.git "$HOME/.oh-my-zsh" --depth 1

cp "$HOME/.oh-my-zsh/templates/zshrc.zsh-template" "$HOME/.zshrc"

mv "$HOME/.zshrc" "$HOME/.zshrc.bak.$(date +%Y.%m.%d-%H:%M:%S)"

cp "$HOME/.oh-my-zsh/templates/zshrc.zsh-template" "$HOME/.zshrc"

sed -i '/^ZSH_THEME/d' "$HOME/.zshrc"

sed -i '1iZSH_THEME="agnoster"' "$HOME/.zshrc"

echo "alias chcolor='$HOME/.termux/colors.sh'" >> "$HOME/.zshrc"

echo "alias chfont='$HOME/.termux/fonts.sh'" >> "$HOME/.zshrc"

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$HOME/.zsh-syntax-highlighting" --depth 1

echo "source $HOME/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> "$HOME/.zshrc"

chsh -s zsh"""


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
\033[0m   Seizin Saya!!
\033[0m • For Credit/Bug Chat WA : 081310662343
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0m
""")


def NFZ():
    Tutorial()


def Login():
    Gator_Bks()
    User = input("\033[91m[\033[93m+\033[91m]\033[93m Username\033[92m :\033[0m ")
    Pass = input("\033[91m[\033[93m+\033[91m]\033[93m Password\033[92m :\033[0m ")
    if User == "GBKS" and Pass == "NaFaZ":
        Berhasil()
    elif User != "GBKS" and Pass == "NaFaZ":
        os.system(Clears)
        print("\033[92m[\033[93m+\033[92m]\033[91m Username Salah!!!")
        print("\033[37m")
        print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Username Dengan Benar!!!")
        print("\033[37m")
        sleep(3)
        NFZ()
    elif User == "GBKS" and Pass != "NaFaZ":
        os.system(Clears)
        print("\033[92m[\033[93m+\033[92m]\033[91m Password Salah!!!")
        print("\033[37m")
        print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Password Dengan Benar!!!")
        print("\033[37m")
        sleep(3)
        NFZ()
    else:
        os.system(Clears)
        print("\n")
        print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Username & Password Dengan Benar!!!")
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


def countdownTimer(start_minute,start_second):
    total_second = start_minute * 10 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1


def Berhasil():
    os.system(Clears)
    print("\033[96m[\033[93m+\033[96m]\033[93m Login Berhasil")
    print("\n")
    sleep(5)
    os.system(Clears)
    print("\n")
    print("\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks")
    print("\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○")
    print("\n")
    sleep(5)
    os.system(Clears)
    print("\n")
    Bang_Jago = input("\033[92m[\033[93m+\033[92m]\033[93m Tekan Enter Untuk Melanjutkan Program")
    Installer()


def Installer():
    Gator_Bks()
    print("""\033[91m[\033[0m1\033[91m]\033[93m INSTALL PACKAGE PROGRAM
\033[91m[\033[0m2\033[91m]\033[93m JALANKAN PROGRAM SEKARANG\033[91m!!
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        installed()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        install()
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
        Lanjutan()


def installed():
    os.system(Clears)
    print("\033[92m")
    os.system(Install)
    os.system(Clears)
    print("\n")
    print("\033[92m[\033[93m+\033[92m]\033[92m Install Program SuperTools Berhasil")
    print("\033[37m")
    print(Author)
    print(Thanks)
    print("\033[37m")
    print("\033[92m[\033[93m+\033[92m]\033[93m Selanjutnya Download Aplikasi\033[91m Termux API\033[93m Di\033[97m Play Store")
    print("\033[37m")
    sleep(5)
    Lanjutan()


def install():
    Gator_Bks()
    Test = input("\033[91m[\033[93m+\033[91m]\033[96m Yakin Ingin Melanjutkan Program Tanpa Menginstall Package?\033[97m (y/n)\033[93m =>\033[0m ")
    if Test == "Y" or "y":
        os.system(Clears)
        print("\n")
        print("\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks")
        print("\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○")
        print("\n")
        sleep(5)
        os.system(Clears)
        print("\n")
        print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
        sleep(10)
        os.system(Clears)
        print("\n")
        Bang_Jago = input("\033[92m[\033[93m+\033[92m]\033[93m Tekan Enter Untuk Melanjutkan Program")
        Mulai()
    elif Test =="N" or "n":
        installed()
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
        install()


def Lanjutan():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://play.google.com/store/apps/details?id=com.termux.api"
    print("""\033[91m[\033[0m1\033[91m]\033[93m DOWNLOAD TERMUX API SEKARANG\033[91m!!
\033[91m[\033[0m2\033[91m]\033[93m JALANKAN PROGRAM SEKARANG\033[91m!!
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
    GatorBks = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        Lanjutan()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print("\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks")
        print("\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○")
        print("\n")
        print("\n")
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
        Lanjutan()


def Tutorial():
    Gator_Bks()
    url = "am start -a android.intent.action.VIEW -d https://bit.ly/3szQaa3"
    url1 = "am start -a android.intent.action.VIEW -d https://bit.ly/3sxYOpv"
    print("""\033[91m[\033[0m1\033[91m]\033[93m CARA MENJALANKAN PROGRAM NAFAZ-PROJECT
\033[91m[\033[0m2\033[91m]\033[93m FUNGSI & FITUR PROGRAM NAFAZ-PROJECT
\033[91m[\033[0m3\033[91m]\033[93m JALANKAN PROGRAM NAFAZ-PROJECT
""")
    GatorBks = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
    if GatorBks == "1":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url)
        Gator_Bks()
        print("\033[37m")
        NFZ()
    elif GatorBks == "2":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Loading()
        os.system(url1)
        Gator_Bks()
        print("\033[37m")
        NFZ()
    elif GatorBks == "3":
        os.system(Clears)
        print("\n")
        print(input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Melanjutkan"))
        Login()
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
        Tutorial()


if __name__ == '__main__':
    NFZ()