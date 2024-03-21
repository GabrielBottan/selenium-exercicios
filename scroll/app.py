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

# driver.get('https://cursoautomacao.netlify.app')



def iniciar_scroll():
    logger = logging.getLogger(__name__)

    try:
        
        driver.get('https://cursoautomacao.netlify.app/desafios')
        sleep(2)

        #rolar até em baixo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)

        #rolar para o topo
        driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        sleep(2)

        driver.close()

    except Exception as e:
        logger.error(f'Não foi possivel usar a funcao iniciar scroll() \n {type(e).__name__}: {e}')



iniciar_scroll()


# #como scrolar até o fim da página
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(3)

# # #como rolar até o topo da página
# driver.execute_script("window.scrollTo(0, document.body.scrollTop);")


# # #rolar x quantidade em pixel (positivo caso queria descer)
# driver.execute_script("window.scroll(0,1500);")


# # #rolar x quant idade em pixel (negativo caso queria subir)
# driver.execute_script("window.scroll(0,-1500);")


# input('')
# driver.close()