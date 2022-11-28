#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:28:10 2022

@author: zeroziontopia
"""


#YILBAŞI ÇEKİLİŞİ#

from random import choice 

kisiSayisi = int(input("Kaç kişisiniz"))

sonuc = dict()
kisiler = []

for i in range(kisiSayisi):
    kisi = input("Kişi adını giriniz:")
    kisiler.append(kisi)

for i in range(kisiSayisi):
    while True:
        kime = choice(kisiler)
        if kime!= kisiler[i] and kime not in sonuc.values():
            sonuc[kisiler[i]] = kime
            break
        
for key in sonuc:
    print(key,sonuc[key])
    

