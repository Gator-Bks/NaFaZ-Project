#!/usr/bin/env python2
#coding: utf-8


import codecs
import binascii
import time
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
	print("""\033[91m	╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[0m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
\033[93m		   🅂🄲🅁🄸🄿🅃 🄳🄴🄵🄰🄲🄴
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
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN JUDUL (TITLE)")
	Judul = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN ALERT")
	Alert = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN LINK GAMBAR (LOGO)")
	Logo = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN LINK MUSIK (TOP4TOP)")
	Musik = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m HACKED BY")
	HackedBy = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN LINK GAMBAR (BACKGROUND)")
	BgImage = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN PESAN. GUNAKAN KODE <br> UNTUK TEXT SELANJUTNYA!!")
	Quotes = input("\033[92m=>\033[0m ")
	print("\033[91m[\033[0m+\033[91m]\033[93m MASUKKAN PESAN TERIMA KASIH")
	ThanksTo = input("\033[92m=>\033[0m ")
	# Buat Script HTML nya Bang Jago
	# Jangan ada yg dirubah yak ntar eror
	# Author By ǴaͲor βks
	
	Gator_Bks = open("GatorBks.html","w")
	
	
	Bang_Jago1 = """<!DOCTYPE html>
	 <html>
	 <head>
	 		<!-- Judul (Tittle) -->
		 <title>"""
	
	Bang_Jago2 = Judul
	
	Bang_Jago3 = """</title>
	
		 <!-- Alert -->
		 <script>alert('"""
	
	Bang_Jago4 = Alert
	
	Bang_Jago5 = """')</script>
		 <meta charset="UTF-8"/>
		 <link rel="stylesheet" href="" type="text/css"/>
	 </head>
	<!-- Jangan Di Ubah (Author By Gator Bks) -->
	<base href="https://ytmp3.cc/">
	<meta charset="UTF-8">
	<link rel="canonical" href="https://gatorberkelas.blogspot.com">
	<link rel="stylesheet" href="/css/a/d.css?_=1600328224">
		 <body>
	<!-- Logo -->
	<center>
	<img src='"""
	
	Bang_Jago6 = Logo
	
	Bang_Jago7 = """' width="300" height="300"
	</img>
	
	<!-- Musik -->
	<a border="10"></a>
	<audio autoplay="autoplay" playback="playback" controls="controls" src='"""
	
	Bang_Jago8 = Musik
	
	Bang_Jago9 = """' type="audio/mpeg"></audio>
	
	<!-- Hacked By -->
	<!-- Jangan Di Ubah Kecuali Teks Hacked By ... (Author By Gator Bks) -->
	<center>
	<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
	<style type="text/css">*{margin:0;padding:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;-ms-box-sizing:border-box;-o-box-sizing:border-box;box-sizing:border-box}body,html{margin:0;padding:0;font:16px/1.4 Lato,sans-serif;color:#fefeff;-webkit-font-smoothing:antialiased;font-smoothing:antialiased;font-family:Comic Sans MS}body{background:#080510;-webkit-touch-callout:none;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}h1{font:2.75em Cinzel,serif;font-weight:400;letter-spacing:.35em;text-shadow:0 0 25px rgba(254,254,255,.85)}h2{font:1.45em Cinzel,serif;font-weight:400;letter-spacing:.5em;text-shadow:0 0 25px rgba(254,254,255,.85);text-transform:lowercase}[class^=letter]{-webkit-transition:opacity 3s ease;-moz-transition:opacity 3s ease;transition:opacity 3s ease}.letter-0{transition-delay:.2s}.letter-1{transition-delay:.4s}.letter-2{transition-delay:.6s}.letter-3{transition-delay:.8s}.letter-4{transition-delay:1s}.letter-5{transition-delay:1.2s}.letter-6{transition-delay:1.4s}.letter-7{transition-delay:1.6s}.letter-8{transition-delay:1.8s}.letter-9{transition-delay:2s}.letter-10{transition-delay:2.2s}.letter-11{transition-delay:2.4s}.letter-12{transition-delay:2.6s}.letter-13{transition-delay:2.8s}.letter-14{transition-delay:3s}h1,h2{visibility:hidden;-webkit-transform:translate3d(0,0,0);-moz-transform:translate3d(0,0,0);transform:translate3d(0,0,0)}h1.transition-in,h2.transition-in{visibility:visible}h1 [class^=letter],h2 [class^=letter]{opacity:0}h1.transition-in [class^=letter],h2.transition-in [class^=letter]{opacity:1}#container{display:table;position:absolute;z-index:20;width:100%;height:100%;text-align:center;cursor:none}#container>div{display:table-cell;vertical-align:middle}#container p{position:absolute;width:100%;left:0;bottom:25px;font-size:.8em;letter-spacing:.1em;font-weight:300;color:#76747a;-webkit-font-smoothing:subpixel-antialiased;font-smoothing:subpixel-antialiased}#container p strong{color:#b3abc5}#container p span{font-size:.75em;padding:0 2px}#canvas{position:absolute;z-index:10;top:0;left:0;width:100%;height:100%;cursor:none}#stats{position:absolute;z-index:10;left:10px;top:10px}.dg.ac{z-index:100!important}.STYLE4{color:#FFF} </style> 
	 <body ondragstart="window.event.returnValue=false" oncontextmenu="window.event.returnValue=false" onselectstart="event.returnValue=false"> <div id="container"> 
	 <div><br><br><br><br> 
	 <script type='text/javascript'> var isCtrl = false; document.onkeyup=function(e) { if(e.which == 17) isCtrl=false; } document.onkeydown=function(e) { if(e.which == 17) isCtrl=true; if((e.which == 85) || (e.which == 67) &amp;&amp; isCtrl == true) { // alert(&#8216;Keyboard shortcuts are cool!&#8217;); return false; } } var isNS = (navigator.appName == "Netscape") ? 1 : 0; if(navigator.appName == "Netscape") document.captureEvents(Event.MOUSEDOWN||Event.MOUSEUP); function mischandler(){ return false; } function mousehandler(e){ var myevent = (isNS) ? e : event; var eventbutton = (isNS) ? myevent.which : myevent.button; if((eventbutton==2)||(eventbutton==3)) return false; } document.oncontextmenu = mischandler; document.onmousedown = mousehandler; document.onmouseup = mousehandler; </script> 
	 <center> 
	 <script> farbbibliothek = new Array(); farbbibliothek[0] = new Array("red","red","silver","black","black","red","red","yellow","yellow","white","white","yellow","yellow","yellow","white","white","silver","yellow","yellow","yellow","silver","silver","yellow","yellow","yellow","white","white","yellow","yellow","yellow"); farbbibliothek[1] = new Array("red","yellow","green","cyan"); farbbibliothek[2] = new Array("red","red","black","black","blue","blue","black","black","yellow","yellow","cyan","cyan","pink","pink","red","red","purple","purple","magenta","magenta","indigo","indigo","black","black","black","silver","white","white","white","red","red","red","red","black","black","black"); farbbibliothek[3] = new Array("cyan","cyan","cyan","cyan","black","black","black","red","red","red","silver","silver","red","cyan","yellow","black","green","green","green","magenta","magenta","pink","pink","pink"); farbbibliothek[4] = new Array("purple","purple","purple","green","green","green","purple","purple","purple","pink","pink","pink","blue","blue","blue","blue","black","black","red","red","red","black","black","green","green","cyan","#yellow","purple","pink","magenta"); farbbibliothek[5] = new Array("cyan","cyan","pink","pink","blue","blue"); farbbibliothek[6] = new Array("purple","purple","purple","black","black","silver"); farbbibliothek[7] = new Array("pink","pink","pink","pink","white","white","white","pink","pink","pink"); farbbibliothek[8] = new Array("yellow","yellow","yellow","white","white","yellow","yellow","yellow","white","white","yellow","yellow","yellow","white","white","yellow","yellow","yellow","white","white","yellow","yellow","yellow","white","white","yellow","yellow","yellow","silver","silver","cyan","cyan","cyan","white","white","cyan","cyan","cyan","cyan","red","blue","yellow","magenta","indigo","lightblue","white","white"); farben = farbbibliothek[4]; function farbschrift() { for(var i=0 ; i<Buchstabe.length; i++) { document.all["a"+i].style.color=farben[i]; } farbverlauf(); } function string2array(text) { Buchstabe = new Array(); while(farben.length<text.length) { farben = farben.concat(farben); } k=0; while(k<=text.length) { Buchstabe[k] = text.charAt(k); k++; } } function divserzeugen() { for(var i=0 ; i<Buchstabe.length; i++) { document.write("<font face='monotype corsiva' size=30><span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span></font>"); } farbschrift(); } var a=1; function farbverlauf() { for(var i=0 ; i<farben.length; i++) { farben[i-1]=farben[i]; } farben[farben.length-1]=farben[-1]; setTimeout("farbschrift()",30); } var farbsatz=1; function farbtauscher() { farben = farbbibliothek[farbsatz]; while(farben.length<text.length) { farben = farben.concat(farben); } farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001)); } setInterval("farbtauscher()",5000);text='HACKED BY """

	Bang_Jago10 = HackedBy
	
	Bang_Jago11 = """'; </script>
	 <span class='newclass'>
	 <script type="text/javascript"> string2array(text); divserzeugen(); </script></span>
	 <script type="text/javascript">
	 <!-- var message="Sorry, right-click has been disabled";function clickIE(){if(document.all){(message);return false;}} function clickNS(e){if(document.layers||(document.getElementById&&!document.all)){if(e.which==2||e.which==3){(message);return false;}}} if(document.layers) {document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;} else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;} document.oncontextmenu=new Function("return false") </script>
	 </center>
	 
	<!-- Quotes -->
	<!-- Jangan Di Ubah Kecuali Warna, Ukuran Dan Quote (Author By Gator Bks) -->
	<center>
	<br><br><br><br><br>
	<font face="Obitron" size="25" font style="text-shadow: 0px 0px 5px red;"<font color="red">Pesan :</font>
	<br>
	<font face="Obitron" size="25" font style="text-shadow: 0px 0px 5px yellow;"<font color="yellow">"""
	
	Bang_Jago12 = Quotes
	
	Bang_Jago13 = """</font></center>
	</br></br>
	
	<!-- Thanks To -->
	<!-- Jangan Di Ubah Kecuali Warna, Ukuran Dan Quote (Author By Gator Bks) -->
	<center>
	<font face="Obitron" size="3" font style="text-shadow: 0px 0px 2px yellow;"<font color="yellow">Thanks To :</font>
	<br>
	<font face="Obitron" size="2" font style="text-shadow: 0px 0px 2px cyan;"<font color="cyan">"""
	
	Bang_Jago14 = ThanksTo
	
	Bang_Jago15 = """</font>
	<br>
	</br></br></br></br>
	
	<!-- Link Medsos -->
	<!-- Jangan Di Ubah Kecuali Link Dan Nama (Author By Gator Bks) -->
	<div id="nav">
	<a  href="https://gatorberkelas.blogspot.com">Blogspot</a>
	<a  href="https://github.com/Gator-Bks">Github</a>
	<a  href="https://www.instagram.com/gator_bks">Instagram</a>
	<a  href="https://twitter.com/gator_bks">Twitter</a>
	<a  href="https://www.youtube.com/channel/UCrzkADYdl1qQOgeURA_m62g">YouTube 1</a>
	<a  href="https://www.youtube.com/channel/UCFy1ZNRvXQGeSLfktmviDLw">YouTube 2</a>
	<a  href=http://wa.me/6281310662343>WhatsApp</a>
	<a  href="http://t.me/gator_bks">Telegram</a>
	</div>
		 </body>
	<style>
	body {cursor:cross;
	background: #000000 url("""
	
	Bang_Jago16 = BgImage
	
	Bang_Jago17 = """) scroll repeat center center;
	</style>
	 </html>"""
	Gator_Bks.write(Bang_Jago1)
	Gator_Bks.write(Bang_Jago2)
	Gator_Bks.write(Bang_Jago3)
	Gator_Bks.write(Bang_Jago4)
	Gator_Bks.write(Bang_Jago5)
	Gator_Bks.write(Bang_Jago6)
	Gator_Bks.write(Bang_Jago7)
	Gator_Bks.write(Bang_Jago8)
	Gator_Bks.write(Bang_Jago9)
	Gator_Bks.write(Bang_Jago10)
	Gator_Bks.write(Bang_Jago11)
	Gator_Bks.write(Bang_Jago12)
	Gator_Bks.write(Bang_Jago13)
	Gator_Bks.write(Bang_Jago14)
	Gator_Bks.write(Bang_Jago15)
	Gator_Bks.write(Bang_Jago16)
	Gator_Bks.write(Bang_Jago17)
	Gator_Bks.close()
	Sukses()


def Balik():
	print("\n")
	print(Author)
	print(Thanks)
	print("\033[37m")
	print("\n")
	txt = input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Memilih Opsi Selanjutnya")
	Lagi()
	

def Lagi():
	os.system(Clears)
	NFZ()
	print("""\033[91m[\033[0m1\033[91m]\033[93m KEMBALI KE PROGRAM SCRIPT DEFACE
\033[91m[\033[0m2\033[91m]\033[93m KEMBALI KE AWAL PROGRAM
\033[91m[\033[0m3\033[91m]\033[91m KELUAR
""")
	print("\033[37m")
	Virgo = input("\033[91m[\033[93m+\033[91m]\033[92m Masukkan Pilihan\033[93m =>\033[0m ")
	if Virgo is "1":
		os.system(Clears)
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
		sleep(5)
		os.system(Clears)
		print("\n")
		txt = input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Memilih Opsi Selanjutnya")
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(5)
		os.system(Clears)
		NFZ()
	elif Virgo is "2":
		os.system(Clears)
		print("\n")
		print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
		sleep(10)
		os.system(Clears)
		print("\n")
		txt = input("\033[91m[\033[93m+\033[91m]\033[93m Tekan Enter Untuk Memilih Opsi Selanjutnya")
		os.system(Clears)
		print("\n")
		print(Author)
		print(Thanks)
		print("\033[37m")
		sleep(5)
		os.system(Clears)
		Mulai()
	elif Virgo == "3":
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


def Sukses():
	os.system(Clears)
	NFZ()
	GatorBks = "mv -f GatorBks.html /sdcard"
	os.system(GatorBks)
	print("\033[91m[\033[93m+\033[91m]\033[93m Script Deface Berhasil Di buat\033[91m!!!")
	print("\033[91m[\033[93m+\033[91m]\033[93m Script Deface Bernama\033[0m GatorBks.html")
	print("\033[91m[\033[93m+\033[91m]\033[93m Tersimpan Di Luar\033[92m Penyimpanan Internal")
	print("\033[37m")
	print("\n")
	Balik()


if __name__ == '__main__':
    NFZ()