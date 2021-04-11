#!/usr/bin/env python3
# encoding: UTF-8


import sys
import os


Clears = "clear"


os.system(Clears)
print("""\033[91m	╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[0m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
\033[93m		   🄸🄿 🄶🄴🄾🄻🄾🄲🄰🅃🄸🄾🄽
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

__author__ = 'Gator Bks'


class IpGeoLocation:
    def __init__(self, query, jsonData = None):
        self.Query = query
        self.ASN = '-'
        self.City = '-'
        self.Country = '-'
        self.CountryCode = '-'
        self.ISP = '-'
        self.Latitude = 0.0
        self.Longtitude = 0.0
        self.Organization = '-'
        self.IP = '0.0.0.0'
        self.Region = '-'
        self.RegionName = '-'
        self.Status = '-'
        self.Timezone = '-'
        self.Zip = '-'
        self.GoogleMapsLink = ''
        
        if jsonData != None:
            if type(jsonData) is dict:
                if 'as' in jsonData: 
                    self.ASN = jsonData['as']
                
                if 'city' in jsonData:
                    self.City = jsonData['city']
                 
                if 'country' in jsonData:
                    self.Country = jsonData['country']
                   
                if 'countryCode' in jsonData:
                    self.CountryCode = jsonData['countryCode']
                   
                if 'isp' in jsonData:
                    self.ISP = jsonData['isp']
                   
                if 'lat' in jsonData:
                    self.Latitude = jsonData['lat']
                  
                if 'lon' in jsonData:
                    self.Longtitude = jsonData['lon']
                  
                if 'org' in jsonData:
                    self.Organization = jsonData['org']
                   
                if 'query' in jsonData:
                    self.IP = jsonData['query']
                  
                if 'region' in jsonData:
                    self.Region = jsonData['region']
                  
                if 'regionName' in jsonData:
                    self.RegionName = jsonData['regionName']
                  
                if 'status' in jsonData:
                    self.Status = jsonData['status']
                   
                if 'timezone' in jsonData:
                    self.Timezone = jsonData['timezone']
                   
                if 'zip' in jsonData:
                    self.Zip = jsonData['zip']
                
                if type(self.Latitude) == float and type(self.Longtitude) == float: 
                    self.GoogleMapsLink = 'http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(self.Latitude, self.Longtitude)
                    
                    
    def ToDict(self):
        #self.__dict__.
        return {'Target':self.Query, 'IP':self.IP, 'ASN':self.ASN, 'Kota':self.City, 
                    'Negara':self.Country, 'Kode Negara':self.CountryCode, 'ISP':self.ISP, 
                    'Garis Lintang':str(self.Latitude), 'Garis Bujur':str(self.Longtitude), 
                    'Organisasi':self.Organization, 'Wilayah':self.Region, 
                    'Nama Wilayah':self.RegionName, 'Zona Waktu':self.Timezone, 
                    'Kode Zip':self.Zip, 'Google Maps':self.GoogleMapsLink
                }