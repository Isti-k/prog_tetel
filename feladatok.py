import random
import math

"""
Írj eljárást, mely a paraméterben kap két egész számot ezen
két egész szám közötti páros számok összegét számolja ki az eljárás
"""

def feladat1(a:int,j:int):
    i:int=a
    osszeg=0
    while i<j:
        if i%2==0:
            print(i)
            osszeg +=1
        i += 1

    return osszeg

def feladat2(a:int,j:int):
    #i:int=a
    osszeg:int=0
    for i in range(i,j,1):
        if i%2==0:
            print(i)
            osszeg +=i
        #i += 1

    return osszeg

"""
Írj függvényt, amely generál 20 db véletlen számot
-10 és 10 között
Számold meg hány negatív szám van közötte
A visszatérési érték a negatív számok száma
"""


def negativ():
    i:int=0
    db:int=0
    while i<20:
        szam:int=math.floor(random.random()*(10-(-10))+(-10))
        print(szam)
        if szam < 0:
            db +=1
        i +=1

    return db

def negativ2():
    #i:int=0
    db:int=0
    for i in range(0,20,1):
        szam:int=math.floor(random.random()*(10-(-10))+(-10))
        print(szam)
        if szam < 0:
            db +=1
        i +=1
    return db


def veletlen():
    osszeg:int=0
    for i in range(0,10,1):
        szam:int=math.floor(random.random()*(10-12)+-10)
        osszeg += szam

    return osszeg

def veletlen2():
    nagyszam:int=0
    for i in range(0,8,1):
        szam:int=math.floor(random.random()*30+20)
        if szam>nagyszam:
            nagyszam=szam
    return nagyszam


def egesz_beker():
    osszeg:int=0
    for i in range(0,3,1):
        szam:int=int(input(f"Kérem az {i+1}. égesz számot!"))
        osszeg += szam
    return osszeg/3


def nulla_szam():
    osszeg:int=0
    db:int=1
    i:int=0
    szam:int=int(input(f"Kérem az {i+1}. égesz számot!"))
    while szam!=0:
        osszeg += szam
        db += 1
        i += 1
        szam:int=int(input(f"Kérem az {i+1}. égesz számot!"))

    return osszeg / (db-1)









