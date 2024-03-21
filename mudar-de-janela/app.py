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



         
    

driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(3)

def mudar_de_janela():

    try:
        logger = logging.getLogger(__name__)
        
        janala_atual = driver.current_window_handle
        
        driver.execute_script('window.scrollTo(9,2100);')
        
        
        
        botao_de_abrir = driver.find_element(By.XPATH, '//button[text()="Abrir nova janela"]')
        sleep(1)
        botao_de_abrir.click()
        sleep(4)
        
        janelas = driver.window_handles
        
        for janela in janelas:
            if janela not in janala_atual:
                sleep(1)
                driver.switch_to.window(janela)
                sleep(1)
                
                opniao = driver.find_element(By.ID, 'opiniao_sobre_curso')
                sleep(1)
                opniao.click()
                sleep(1)
                
                opniao.send_keys("Esse curso é melhor que haxixe")
                sleep(2)
                
                botao_pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
                sleep(1)
                botao_pesquisar.click()
                sleep(1)
                driver.close()
                
                
       
        driver.switch_to.window(janala_atual)
        sleep(2)
        
        campo_desafio = driver.find_element(By.ID, 'campo_desafio7')
        campo_desafio.click()
        sleep(2)
        campo_desafio.send_keys('FODAAAAAAAAAAAAAAAA')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #    #salvando a janela atual
    #     janela_inicial = driver.current_window_handle
        
    #     #abrindo uma nova janela
    #     driver.execute_script('window.scrollTo(0,600)')  
    #     sleep(2)
        
    #     abrir_janela = driver.find_element(By.XPATH, '//*[text()="Abrir Janela"]')
    #     sleep(1)
    #     abrir_janela.click()
        
        
    #     #quais janelas estão abertas
    #     janelas = driver.window_handles  
    #     for janela in janelas:
    #         print(janela)
        
    #         #mudando para a segunda janela       
    #         if janela not in janela_inicial:
    #             driver.switch_to.window(janela)
    #             campo_pesquisa = driver.find_element(By.ID, 'campo_pesquisa')
    #             sleep(2)
    #             campo_pesquisa.send_keys("Teste campo pesquisa, olá")
    #             sleep(2)
    #             botao_pesquisa = driver.find_element(By.ID, 'fazer_pesquisa')
    #             sleep(1)
    #             botao_pesquisa.click()
    #             sleep(4)
    #             driver.close()
        
    #     #voltando para a janela inicial
    #     driver.switch_to.window(janela_inicial)
        
        
        
        
        
        
        sleep(3)
        driver.close()



    except Exception as e:
        logger.error(f'Não foi possivel, erro: \n {type(e).__name__}: {e}')




mudar_de_janela()

