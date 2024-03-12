from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging

#Função de iniciar o  driver e fazendo configurações necessárias
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



#Iniciando o drive
driver = iniciar_driver()


#Abrindo a URL
driver.get('https://cursoautomacao.netlify.app/desafios')


#Função para verificar se os botões do desafio estão habilitados
def elemento_habilitado():
    logger = logging.getLogger(__name__)

    try: 


        #busca os elementos pelo elemento pai
        botoes = driver.find_elements(By.XPATH,'//section[@class="jumbotron desafios1"]/button')
        
        #itera sobre os elementos filhos
        for botao in botoes:
            if botao.is_enabled():
                print(f'O {botao.text} está habilitado')
            else:
                print(f'O {botao.text} está desabilitado')

        #Fecha o navegador
        driver.close()
        


    except Exception as e:
        logger.error(f' Ao tentar verificar elementos habilitados \n {type(e).__name__}: {str(e)}')





elemento_habilitado()
  



   
    