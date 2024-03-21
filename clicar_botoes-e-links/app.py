# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep
# import logging


# def iniciar_driver():
#     chrome_options = Options()
#     arguments = ['--lang=pt-BR', '--window-size=1000,900', '--incognito']
#     for argument in arguments:
#         chrome_options.add_argument(argument)

#     chrome_options.add_experimental_option('prefs', {
#         'download.prompt_for_download': False,
#         'profile.default_content_setting_values.notifications': 2,
#         'profile.default_content_setting_values.automatic_downloads': 1,

#     })
#     driver = webdriver.Chrome(service=ChromeService(
#         ChromeDriverManager().install()), options=chrome_options)

#     return driver


# driver = iniciar_driver()


# def efetuar_login():
#     logger = logging.getLogger(__name__)

#     try:
#         #abrir a página
#         driver.get('https://cursoautomacao.netlify.app/desafios')
#         sleep(2)

#         #encontrar o campo e digitar o nome
#         campo_de_nome = driver.find_element(By.ID, 'dadosusuario')
#         sleep(1)
#         campo_de_nome.send_keys('Gabriel Bottan')
#         sleep(2)

#         #achar e clicar no botao de login
#         botao_login = driver.find_element(By.ID,'desafio2')
#         sleep(1)
#         botao_login.click()
        

#         sleep(10)

#         # #achar e clicar no botão de login
#         # botao_de_login =  driver.find_element(By.LINK_TEXT,'Login')
#         # botao_de_login.click()
#         # sleep(2)


#         # #achar o campo de email e digitar(para digitar use send_keys )
#         # campo_de_email = driver.find_element(By.NAME,'email')
#         # campo_de_email.send_keys('gabrielbottan@gmail.com')
#         # sleep(1)
#         # #achar o campo de senha e digitar
#         # campo_de_senha = driver.find_element(By.NAME,'campoSenha')
#         # campo_de_senha.send_keys('12345')
#         # sleep(1)
     
#         # #encontrar e clicar no botao de enviar 
#         # botao_de_enviar = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
#         # botao_de_enviar.click()

#         # sleep(3)


#         driver.close()

#     except Exception as e:
#         logger.error(f'Não foi possivel efetuar o login: \n {type(e).__name__}: {e}')



# efetuar_login()









# 1. Exiba alguma mensagem de apresentação, que apresenta seu programa para o usuário
# 2. O jogo deverá iniciar somente após o jogador(a) apertar “enter” no teclado (dica de como fazer isso
# aqui)
# 3. O número gerado não deve ser exibido para o jogador(a).
# 4. O jogador(a) deve ser capaz de chutar quantas vezes necessário.
# 5. Seu código deve tratar as possíveis exceções que possam ser geradas pelo jogador(a).
# 6. Caso o jogador(a) erre o chute, dê dicas se ele(a) deve chutar mais alto ou mais baixo.
# 7. Ao acertar o chute, ofereça ao jogador(a) a opção de jogar novamente.


#1 precisar gerar um numero de um a 100
#2 o programa deve permitir que o usuario chute quantas vezes forem necessário ate´acertar

#3 o programa deve dar dicas de o quão próximo ele está, se passou muito, se está longe

# import random


# #Gernando um numero aleátorio
# def gerar_numero():
#     return random.randint(1,100)

# #Obetendo o chut e do usuario para comparar com o numero aleatorio depois
# def obter_chute_usuario():
#     while True:
#         try:
#             chute = int(input('Chute um número de 1 a 100: '))
#             return chute
#         except ValueError:
#             print('Digite apenas números')

       
# def comparar_chute(chute, numero_sorteado):
#     if numero_sorteado == chute:
#         return 'Parábens você acertou o número'
#     elif chute < numero_sorteado:
#         return 'Chute um número menor '
#     else:
#         return 'Chute um número maior'
    

# def main():
#     numero_sorteado = gerar_numero()
#     tentativas = 0

#     while True:
#         tentativas += 1
#         chute = obter_chute_usuario()
#         resultado = comparar_chute(numero_sorteado, chute)

#         print(resultado)

#         if resultado == "Parábens você acertou o número":
#             print(f'Você precisou apenas de {tentativas} tentativas')
#             continuar = input('Você deseja continuar? s para sim e n para não')
#             if continuar == 's':
#                 continue
#             else:
#                 break
            

# if __name__ == '__main__':
#     main()


    


        



