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



         
    

driver.get('https://cursoautomacao.netlify.app/desafios')

def digitar():

    try:
        logger = logging.getLogger(__name__)
        
        sleep(2)
        driver.execute_script('window.scrollTo(0,2000);')
        
        sleep(1)
        
        
        paises_select = driver.find_element(By.XPATH, '//select[@id="paisesselect"]')
        sleep(1)
        opcao_paises = Select(paises_select)
        
        opcao_paises.select_by_index(2)
        sleep(1)
        
        opcao_paises.select_by_index(4)
        sleep(1)
        
        opcao_paises.select_by_index(6 )
        sleep(1)
        
            
        
        
        
        # pais_drop = driver.find_element(By.XPATH, "//select[@id='paisselect']")
        # sleep(2)
        # opces_de_paises = Select(pais_drop)
        
        # #acessanddo por indice
        # opces_de_paises.select_by_index(2)
        # sleep(2)
        
        #  #aceessando por value
        # opces_de_paises.select_by_value ('estadosunidos')
        # sleep(2)
        
         
        #  #acessando por texto de exibição
        # opces_de_paises.select_by_visible_text('Brasil')
        # sleep(2)
         
        
        
        
        
        sleep(3)

        driver.close()



    except Exception as e:
        logger.error(f'Não foi possivel clicar no xbox button: \n {type(e).__name__}: {e}')




digitar()

