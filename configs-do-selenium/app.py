from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#como pode adicionar opções de incialização dentro do webdriver

chrome_options = Options()
#--start-maximized = Inicia maximizado
#--lang=pt-BR = define o idioma de inicialização
#--incognito =  usa o modo anonimo
#--window-size=800,800 = define a resulução da janela em largura e altura
#--headless = roda em segundo plano com a janela fechada
#--disable-notifications = desabilita notificações
#--disable-gpu = desabilita renderização com o GPU

arguments = ['--lang=pt-BR','--window-size=500,500','--incognito']
for args in arguments:
    chrome_options.add_argument(args)


#uso de configurações experimentais (opcional de acordo com cada automação)
chrome_options.add_experimental_option('prefs',{
    #alterar o local de donwload de arquivos
    # 'download.default_directory': 'D.... caminho do diretorio'
    
    #notificar o google da alteração de download
    'download.directory_upgrade': True,
    
    #desabilitar confirmação de download
    'download.prompt_for_download': False,
    
    #desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    
    #permitir multiplos downloads
    'profile.default_content_settings_values_automatic_downloads': 1,
})




#incializar o webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)


#navegar até um site
driver.get('https://facebook.com')
input('aperta ai ')