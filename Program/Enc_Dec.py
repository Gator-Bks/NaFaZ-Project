#!/usr/bin/env python
#coding: utf-8


import hashlib
from base64 import b64encode, b64decode
import codecs
import binascii
from time import sleep
import re
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
\033[93m	      🄴🄽🄲🅁🅈🄿🅃🄸🄾🄽 & 🄳🄴🄲🅁🅈🄿🅃🄸🄾🄽
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m MD5
\033[91m[\033[0m2\033[91m]\033[93m ENCRYPT \033[91m-\033[96m SHA1
\033[91m[\033[0m3\033[91m]\033[93m ENCRYPT \033[91m-\033[96m SHA224
\033[91m[\033[0m4\033[91m]\033[93m ENCRYPT \033[91m-\033[96m SHA256
\033[91m[\033[0m5\033[91m]\033[93m ENCRYPT \033[91m-\033[96m SHA384
\033[91m[\033[0m6\033[91m]\033[93m ENCRYPT \033[91m-\033[96m SHA512
\033[91m[\033[0m7\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m BASE64
\033[91m[\033[0m8\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m BINARY
\033[91m[\033[0m9\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m HEXADECIMAL
\033[91m[\033[0m10\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m CAESAR CIPHER
\033[91m[\033[0m11\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m TEKS
\033[91m[\033[0m12\033[91m]\033[93m ENCRYPT/DECRYPT \033[91m-\033[96m KATA
\033[91m[\033[0m13\033[91m]\033[91m KELUAR
""")
	Bang_Jago = input("\n\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Bang_Jago == "1":
		Md5()
	elif Bang_Jago == "2":
		Sha1()
	elif Bang_Jago == "3":
		Sha224()
	elif Bang_Jago == "4":
		Sha256()
	elif Bang_Jago == "5":
		Sha384()
	elif Bang_Jago == "6":
		Sha512()
	elif Bang_Jago == "7":
		Base64()
	elif Bang_Jago == "8":
		Binario()
	elif Bang_Jago == "9":
		Hexadecimal()
	elif Bang_Jago == "10":
		CifraDeCesar()
	elif Bang_Jago == "11":
		TextReverse()
	elif Bang_Jago == "12":
		WordsReverse()
	elif Bang_Jago == "13":
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
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM ENCRYPTION & DECRYPTION
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
	print("\033[37m")
	GatorBks = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if GatorBks == "1":
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


def Md5():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m MD5")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.md5(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\033[37m")
	Balik()
	
	
def Sha1():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m SHA1")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.sha1(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\033[37m")
	Balik()
	

def Sha224():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m SHA224")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.sha224(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\033[37m")
	Balik()
	

def Sha256():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m SHA256")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.sha256(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\033[37m")
	Balik()
	

def Sha384():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m SHA384")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.sha384(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\033[37m")
	Balik()
	

def Sha512():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m SHA512")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	hash_object = hashlib.sha512(mystring.encode())
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",hash_object.hexdigest())
	print("\n")
	print("\033[37m")
	Balik()
	

def Base64Encode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m BASE64")
	print("\n")
	mystring = str(input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")) 
	print("\033[33m")
	encode = b64encode(mystring.encode('utf-8')) 
	decode = encode.decode('utf-8')
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",decode)()
	print("\033[37m")
	Balik()
	
def Base64Decode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m BASE64")
	print("\n")
	mystring = str(input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")) 
	print("\033[37m")
	try:
		decode = b64decode(mystring).decode('utf-8')
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",decode)
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		Base64Decode()
	
def Base64():
	Gator_Bks()
	print("""\033[91m[\033[0m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m BASE64
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[91m-\033[96m BASE64
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		Base64Encode()
	elif Bang_Jago == "2":
		Base64Decode()
	else:
		Base64()


def BinarioEncode(encoding='utf-8', errors='surrogatepass'):
	Gator_Bks()
	try:
		print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m BINARY")
		print("\n")
		mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks/Nilai\033[93m =\033[0m ")
		bits = bin(int(binascii.hexlify(mystring.encode(encoding, errors)), 16))[2:]
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",bits.zfill(8 * ((len(bits) + 7) // 8)))
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		BinarioEncode()
	
def BinarioDecode(encoding='utf-8', errors='surrogatepass'):
	Gator_Bks()
	try:
		print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m BINARY")
		print("\n")
		binario = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks/Nilai\033[93m =\033[0m ")
		binario = binario.replace(" ", "")
		n = int(binario, 2)
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",int2bytes(n).decode(encoding, errors))
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		BinarioDecode()
	
def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def Binario():
	Gator_Bks()
	print("""\033[91m[\033[97m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m BINARY
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[91m-\033[96m BINARY
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		BinarioEncode()
	elif Bang_Jago == "2":
		BinarioDecode()
	else:
		Binario()


def HexaEncode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m HEXADECIMAL")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	encode = binascii.hexlify(bytes(mystring, "utf-8"))
	encode = str(encode).strip("b")
	encode = encode.strip("'")
	encode = re.sub(r'(..)', r'\1 ', encode).strip()
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",encode)
	print("\033[37m")
	Balik()
	
def HexaDecode():
	Gator_Bks()
	try:
		print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m HEXADECIMAL")
		print("\n")
		mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
		decode = bytes.fromhex(mystring).decode('utf-8')
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",decode)
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		HexaDecode()
	
def Hexadecimal():
	Gator_Bks()
	print("""\033[91m[\033[97m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m HEXADECIMAL
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[91m-\033[96m HEXADECIMAL
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		HexaEncode()
	elif Bang_Jago == "2":
		HexaDecode()
	else:
		Hexadecimal()


def TextReverseEncode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m TEKS")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",mystring[::-1])
	print("\033[37m")
	Balik()
	
def TextReverseDecode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m TEKS")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m",mystring[::-1])
	print("\033[37m")
	Balik()

def TextReverse():
	Gator_Bks()
	print("""\033[91m[\033[97m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m TEKS
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[91m-\033[96m TEKS
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		TextReverseEncode()
	elif Bang_Jago == "2":
		TextReverseDecode()
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
		TextReverse()


def WordsReverseEncode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m KATA")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m".join(mystring.split()[::-1]))
	print("\033[37m")
	Balik()

def WordsReverseDecode():
	Gator_Bks()
	print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m KATA")
	print("\n")
	mystring = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ")
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
	print("\033[91m=>\033[92m".join(mystring.split()[::-1]))
	print("\033[37m")
	Balik()

def WordsReverse():
	Gator_Bks()
	print("""\033[91m[\033[97m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m KATA
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[91m-\033[96m KATA
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		WordsReverseEncode()
	elif Bang_Jago == "2":
		WordsReverseDecode()
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
		WordsReverse()


def CifraDeCesar():
	Gator_Bks()
	print("""\033[91m[\033[97m1\033[91m]\033[93m ENCRYPT \033[91m-\033[96m CAESAR CHIPER
\033[91m[\033[97m2\033[91m]\033[93m DECRYPT \033[31m-\033[96m CAESAR CHIPER
""")
	Bang_Jago = input("\033[91m[\033[93m+\033[91m]\033[96m Masukkan Pilihan\033[91m  =>\033[0m ")
	if Bang_Jago == "1":
		ChamarBloco1()
	elif Bang_Jago == "2":
		ChamarBloco2()
	else:
		CifraDeCesar()

def cifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def decifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def ChamarBloco1():
	Gator_Bks()
	try:
		print("\033[92m[\033[93m+\033[92m]\033[93m ENCRYPT \033[91m-\033[96m CAESAR CIPHER")
		print("\n")
		c = str(input('\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ')).lower()
		n = int(input('\033[91m[\033[93m+\033[91m]\033[96m Masukkan Kunci Numerik\033[93m =\033[0m '))
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",cifrar())
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		ChamarBloco1()
	
def ChamarBloco2():
	Gator_Bks()
	try:
		print("		")
		print("\033[92m[\033[93m+\033[92m]\033[93m DECRYPT \033[91m-\033[96m CAESAR CIPHER")
		print("\n")
		cc = str(input('\033[91m[\033[93m+\033[91m]\033[96m Masukkan Teks\033[93m =\033[0m ')).lower()
		cn = int(input('\033[91m[\033[93m+\033[91m]\033[96m Masukkan Kunci Numerik\033[93m =\033[0m '))
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Hasilnya :")
		print("\033[91m=>\033[92m",decifrar())
		print("\033[37m")
		Balik()
	except:
		print("\033[91m[\033[93m!\033[91m] Terjadi Kesalahan!!")
		sleep(3)
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(3)
		os.system(Clears)
		ChamarBloco2()


if __name__ == '__main__':
    NFZ()