import pyautogui as spam
import time

def enviar_mensagens(limite, mensagem):
    i = 0
    time.sleep(2)

    while i < limite:
        spam.typewrite(mensagem)
        spam.press("enter")
        i += 1

def main():
    limite_mesg = int(input("Número de mensagens: "))
    if limite_mesg <= 0:
        print("Número inválido de mensagens.")
        return

    msg = input("Qual mensagem você irá enviar?: ")
    if not msg:
        print("Mensagem vazia. Digite uma mensagem válida.")
        return

    enviar_mensagens(limite_mesg, msg)

if __name__ == "__main__":
    main()
