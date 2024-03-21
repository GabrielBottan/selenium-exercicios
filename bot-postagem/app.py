from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
from time import sleep
import random 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys 


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,1200', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()



         
    

driver.get('https://facebook.com')

def postagem():

    try:
        logger = logging.getLogger(__name__)
        
        
       
        sleep(2)
        
        #Logando no facebook
        campo_email = driver.find_element(By.ID,'email')
        sleep(1)
        
        campo_email.send_keys('gabreilbottan02@gmail.com')
        sleep(2)
        
        campo_senha = driver.find_element(By.ID,'pass')
        sleep(2)
        
        campo_senha.send_keys('Biel1407@')
        sleep(2)
        
        campo_senha.send_keys(Keys.ENTER)
        sleep(7)
        
        #Postando
        campo_de_postar = driver.find_element(By.XPATH," //div[@class='x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
        campo_de_postar.click()
        sleep(5)
        
        
        campo_de_postar.send_keys(' Ola pessoal, boa tarde')
        sleep(4)
        
        
        campo_de_avancar = driver.find_element(By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
        sleep(1)

        campo_de_avancar.click()
        sleep(4)

        campo_de_publicar = driver.find_element(By.XPATH,'//*[text()="Publicar"]')
        sleep(1)
        campo_de_publicar.click()
        sleep(4)
        
        
        
        
        sleep(3)

        driver.close()



    except Exception as e:
        logger.error(f'Não foi possivel postar: \n {type(e).__name__}: {e}')




postagem()

