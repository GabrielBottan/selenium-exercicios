from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
from time import sleep




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

def clicar_em_radiobutton():

    try:
        logger = logging.getLogger(__name__)
        
        
        # all_check_box = driver.find_elements(By.XPATH, '//*[starts-with(@id, "acessoNivel")]')
        # sleep(2)
        
        # all_check_box[2].click()
        
        driver.execute_script("window.scrollTo(0,400);")
        sleep(2)
        
        chech_box1 = driver.find_element(By.ID, 'conversivelcheckbox')
        chech_box2 = driver.find_element(By.ID, 'offroadcheckbox')
        
        chech_box1.click()
        sleep(1)
        chech_box2.click()
        
       
        # primeiro_check_box = driver.find_element(By.ID, 'acessoNivel1Checkbox')
        # segundo_check_box = driver.find_element(By.ID, 'acessoNivel2Checkbox')
        # terceiro_check_box = driver.find_element(By.ID, 'acessoNivel3Checkbox')
        
        
        # primeiro_check_box.click()
        # sleep(1)
        # segundo_check_box.click()
        # sleep(1)
        # terceiro_check_box.click()
        # sleep(1)
        
        
        
        
        
        sleep(3)

        driver.close()



    except Exception as e:
        logger.error(f'Não foi possivel clicar no xbox button: \n {type(e).__name__}: {e}')




clicar_em_radiobutton()

