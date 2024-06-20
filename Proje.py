from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from urllib.parse import urlparse, urlsplit, urlunsplit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
from pydub import AudioSegment
from tools import colorprint
import time
import requests
import time



driver = webdriver.Chrome(ChromeDriverManager().install())

service = Service
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
        Ad = driver.find_element(By.XPATH, "//*[@id='requestA d']")
        Ad.click()
        Ad.send_keys(ad)
        Soyad = driver.find_element(By.XPATH, "//*[@id='requestSoyad']")
        Soyad.click()
        Soyad.send_keys(soyad)
ad()

def tarih():
        Dogumgun = str(input("Lütfen doğüm gününüzü giriniz (sadece gün)"))
        DogumAy = str(input("Lütfen doğduğunuz ayı giriniz (sadece ay)"))
        DogumYil = str(input("Lütfen doğuğunuz yılı giriniz (sadece yıl)"))
        DogumGun = driver.find_element(By.XPATH, "//*[@id='requestDogumGun']")
        DogumGun.click()
        DogumGun.send_keys(Dogumgun)
        Dogumay = driver.find_element(By.XPATH, "//*[@id='requestDogumAy']")
        Dogumay.click()
        Dogumay.send_keys(DogumAy)

        Dogumyil = driver.find_element(By.XPATH, "//*[@id='requestDogumYil']")
        Dogumyil.click()
        Dogumyil.send_keys(DogumYil)
tarih()

def serino():
    cevap = str(input("eski kimlik kartı mı? (Evet/Hayır)"))

    if cevap == "Evet":
        eskiSerino = input("Lütfen seri no giriniz ")
        
        eskiSeriNo = driver.find_element(By.XPATH, "//*[@id='requestCuzdanSeriNo']")
        eskiSeriNo.click()
        eskiSeriNo.send_keys(eskiSerino)
        GeciciKimlikBelgeno = input("Lütfen Geçici kimlik belge numarasını giriniz ")
        GeciciKimlikBelgeNo = driver.find_element(By.XPATH, "//*[@id='requestGeciciKimlikNo']")
        GeciciKimlikBelgeNo.click()
        GeciciKimlikBelgeNo.send_keys(GeciciKimlikBelgeno)
    else:
        yeniSerino = input("Lütfen seri no giriniz ")
        yeniSeriNo = driver.find_element(By.XPATH, "//*[@id='requestTckkSeriNo']")
        yeniSeriNo.click()
        yeniSeriNo.send_keys(yeniSerino)
serino()

def download_captcha(url):
    filename = "captcha.mp3"
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    sound = AudioSegment.from_mp3(filename)
    sound.export("captcha.wav", format="wav")

def solve_captcha():
    r = sr.Recognizer()
    with sr.WavFile("captcha.wav") as source:
        audio = r.record(source)  
    text = r.recognize_google(audio, language='en-US')
    return text


def captcha_elements(driver):
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    driver.switch_to.frame(iframe)

    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border")))
    checkbox.click()
    time.sleep(2)
    driver.switch_to.default_content()
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")
    driver.switch_to.frame(iframe)
    audio_button = driver.find_element(By.CSS_SELECTOR, ".rc-button.goog-inline-block.rc-button-audio").click()
    
    time.sleep(0.3)
    url = driver.find_element(By.CLASS_NAME, "rc-audiochallenge-tdownload-link").get_attribute('href')
    download_captcha(url)
    result = solve_captcha()
    driver.find_element(By.ID, "audio-response").send_keys(result)
    driver.find_element(By.ID, "recaptcha-verify-button").click()
    
    driver.switch_to.default_content()


def aramamotoru():
    try:
        driver = webdriver.Chrome()
    except:
        try:
            geckodriver_autoinstaller.install()
            driver = webdriver.Chrome()
        except:
            try:
                driver = webdriver.Chrome()
            except:
                chromedriver_autoinstaller.install()
                driver = webdriver.Chrome()
    driver.get("https://google.com/recaptcha/api2/demo")
    time.sleep(0.5)
    captcha_elements(driver)
aramamotoru()

button2 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[10]/button[1]")
if button2 == None:
        print("Bu kimlikte birisi mevut")
else:
        print("Maalesef aradığınız kişiyi bulamadık")
   
