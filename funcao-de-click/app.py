from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import logging


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
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


def clicar_no_botao_drop():
    logger = logging.getLogger(__name__)

    try:
        driver.get('https://cursoautomacao.netlify.app')
        sleep(2)

        #encontrar o botao de drop 
        botao_dropdown = driver.find_element(By.ID, 'dropdownMenuButton')
        sleep(1)

        #clicar no botão(existem duas formas de clicar no site, e tem sites que uma dá e a outra não, teste as duas) 1 forma:
        # botao_dropdown.click()

        #segunda forma:
        driver.execute_script('arguments[0].click()', botao_dropdown)


        sleep(5)



        driver.close()

    except Exception as e:
        logger.error(f'Não foi possivel encontrar o botão de drop: \n {type(e).__name__}: {e}')



clicar_no_botao_drop()