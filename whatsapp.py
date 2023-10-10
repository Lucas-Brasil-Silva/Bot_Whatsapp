import pyautogui
import keyboard
import webbrowser
from time import sleep

def main():
    # Extraindo informações do arquivo com os contatos:
    with open('contatos.txt','r') as arquivo:
        lista_contatos = [linha.split('\n')[0] for linha in arquivo]

    # For que irá manda a mensagem para todos os contatos da lista:
    for contato in lista_contatos:
        if contato != '':
            # Abre uma nova guia no navegador com whatsapp direto na janela de conversa com o contato da vez:
            webbrowser.open(f'https://api.whatsapp.com/send?phone={contato}')
            sleep(3)
            # Irá clicar para iniciar a conversa e em seguida escolher o Whatsapp Web:
            pyautogui.click(2318, 353, duration=2)
            sleep(2)
            pyautogui.click(2310, 427, duration=2)
            sleep(30)
            # Será inserido a mensagem e enviada:
            keyboard.write('Olá, Tudo bem?')
            sleep(2)
            pyautogui.press('enter')
            sleep(1)
            # A janela será fechada:
            pyautogui.hotkey('ctrl','w')
            # Após o tempo de 300 segundos, fara todo o processo novamente como próximo contato: 
            sleep(300)

if __name__ == '__main__':
    main()