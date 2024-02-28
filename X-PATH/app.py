# como procura um X-PATH??

# //tag[@atributo='valor_da_tag']


#para ver se contém algum elemento
# //*[contains(text(),'valor_do_elemento]... (and e or pode ser usado)


#encontrar qualquer elemento que INICIALIZA COM...
#//*[starts-with(text(),'valor_do_elemento')]



#encontrar qualquer class que INICIALIZA COM...
#//*[starts-with(@class(),'valor_da_class')]


#encontrar qualquer texto
# //t[text()='valor_do_texto']


#Se quiser ser especifico não utilize **, use o valor da tag que está procurando

# para procurar um xpath use o seguinte codigo 
# driver.find_element(By.XPATH, "valor_do_elemento")


#para procurar filhos de uma determinada tag use
#monta o caminho inteiro usando // e o nome do atributo por exemplo : //div//field-set/h4
# para procurar o filho exato abaixo do pai, use apenas uma barra /

#pode especificar a tag se usar a sintaxe para procurar o xpath por expmplo: //div[@id='selec-class']//field-set/h4




#podemos tb procurar por css

#segue a sintaxe:
#tag(section,div,h4,button)
#class (.btn)
#conbinação de class (.btn .bt-sucess)
#Id (#dropDow....)
