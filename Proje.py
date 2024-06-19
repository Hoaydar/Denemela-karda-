from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
import os
import string




service = Service
driver = webdriver.Chrome()
driver.get("https://tckimlik.nvi.gov.tr/Modul/TcKimlikNoDogrula")
time.sleep(5)
def TC():
        Tc = int(input("Lütfen tc giriniz "))
        TC = driver.find_element(By.XPATH, "//*[@id='requestTCKimlikNo']")
        TC.click()
        TC.send_keys(Tc)
TC()

def ad():
        ad = str(input("Lütfen Ad giriniz"))
        soyad = str(input("Lütfen soyad giriniz"))
        Ad = driver.find_element(By.XPATH, "//*[@id='requestAd']")
        Ad.click()
        Ad.send_keys(ad)
        Soyad = driver.find_element(By.XPATH, "//*[@id='requestSoyad']")
        Soyad.click()
        Soyad.send_keys(soyad)
ad()

def tarih():
        Dogumgun = input("Lütfen doğüm gününüzü giriniz (sadece gün)")
        Dogumay = input("Lütfen doğduğunuz ayı giriniz (sadece ay)")
        DogumYil = input("Lütfen doğuğunuz yılı giriniz (sadece yıl)")
        DogumGun = driver.find_element(By.XPATH, "//*[@id='requestDogumGun']")
        DogumGun.click()
        DogumGun.send_keys(Dogumgun)
        Dogumay = driver.find_element(By.XPATH, "//*[@id='requestDogumAy']")
        Dogumay.click()
        Dogumay.send_keys(Dogumay)
        Dogumyil = driver.find_element(By.XPATH, "//*[@id='requestDogumYil']")
        Dogumyil.click()
        Dogumyil.send_keys(DogumYil)
tarih()

def serino():
    cevap = str(input("eski kimlik kartı mı? (Evet/Hayır)"))

    if cevap == "Evet":
        eskiSerino = input("Lütfen seri no giriniz ")
        yeniSerino = input("Lütfen seri no giriniz ")
        eskiSeriNo = driver.find_element(By.XPATH, "//*[@id='requestCuzdanSeriNo']")
        eskiSeriNo.click()
        eskiSeriNo.send_keys(eskiSerino)
        GeciciKimlikBelgeno = input("Lütfen Geçici kimlik belge numarasını giriniz ")
        GeciciKimlikBelgeNo = driver.find_element(By.XPATH, "//*[@id='requestGeciciKimlikNo']")
        GeciciKimlikBelgeNo.click()
        GeciciKimlikBelgeNo.send_keys(GeciciKimlikBelgeno)
    else:
        yeniSeriNo = driver.find_element(By.XPATH, "//*[@id='requestTckkSeriNo']")
        yeniSeriNo.click()
        yeniSeriNo.send_keys(yeniSerino)
serino()


def capctha():
    capctha = driver.find_element(By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")
    capctha.click()

    button = driver.find_element(By.XPATH, "/html/body/div[1]/master/div[3]/tckimliknodogrula/div/div[2]/div/div[2]/div[3]/button")
    button.click()
    time.sleep(1)
    button2 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[10]/button[1]")
    if button2 == None:
          print("Bu kimlikte birisi mevut")
    else:
          print("Maalesef aradığınız kişiyi bulamadık")
   
