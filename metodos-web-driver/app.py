#METODOS MAIS COMUNSO DO WEBDRIVER


# driver.get('www....') # serve para navegar até um site
# driver.maximize_window() #serve para maximizar a janela
# driver.refresh() #recarregar página atual
# driver.get(driver.current_url) ##tb recarrega pagina atual, navega pro mesmo endeerço que está atualmente
# driver.back() # volta a página anterior
# driver.forward() # navega 1 vez para frente
# print(driver.title) #obtém o titulo da pagina
# print(driver.current_url) #obtém o URL atual
# print(driver.page_source) #obtém o código fonte da pagina atual


# print(driver.find_element(By.XPATH,'//a[@class='navbar-brand']').text) #obtem em texto o que foi passado como xpath
# print(driver.find_element(By.XPATH,'//a[@class='navbar-brand']').get_atribute('href')) #obtem exatamente o atributo que for passado

# driver.close()# fecha a janeça atual