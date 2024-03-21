from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
from time import sleep
import random 
from selenium.webdriver.support.select import Select



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,900', '--incognito']
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



         
    

driver.get('https://cursoautomacao.netlify.app')

def digitar():

    try:
        logger = logging.getLogger(__name__)
        
      
        driver.execute_script('window.scrollTo(0,2200);')
        sleep(2)
        
        
        botao_escolher_arquivo = driver.find_element(By.XPATH, '//input[@id="myFile"]')
        sleep(2)
        
        
        botao_escolher_arquivo.send_keys("C:\\Users\\Mary Jc\\OneDrive\\Imagens\\1000_F_305618375_qXPxp46QdMDdbfZ3jOO02eala989Fruv.jpg")
        
        botao_enviar = driver.find_element(By.XPATH, "//input[@value='Enviar Arquivo']")
        botao_enviar.click()
        
        
        
        sleep(3)

        driver.close()



    except Exception as e:
        logger.error(f'Não foi possivel clicar no xbox button: \n {type(e).__name__}: {e}')




digitar()

