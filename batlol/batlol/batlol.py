from pyautogui import *
import pyautogui
from time import sleep
import pywhatkit as kt



def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def send_email(receiver_email):
    if len(receiver_email) == 0:
        return

def check_screen():
    button_pos = pyautogui.locateOnScreen('fila.png', confidence=0.7)
            
    if button_pos != None:
        #print(f'Found {button_pos}')
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main():
    receiver_email = input('Pressione para começar ').strip()
    queue_counter = 0

    print('Estou de olho na fila...', end="\n\n")
    
    
    
    while True:
        if check_screen():
            queue_counter += 1
            print(f'Filas aceitas: {queue_counter}')
            sleep (2)
            kt.sendwhatmsg_instantly 
            ("+5511963346442", "partida aceita gay")


            sleep(6)
            #break


main()            
