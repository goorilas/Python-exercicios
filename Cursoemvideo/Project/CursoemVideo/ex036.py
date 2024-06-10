# usar pyautogui para fazer automação dos programas elaborados.
import pyautogui
from time import sleep
pyautogui.PAUSE = 0.5 #pausa entre comandos
#pyautogui.hotkey('ctrol' , ''shift') usado para combinações de teclas
#pyautogui.click >>> clicar em algum lugar da tela
pyautogui.press('win') #pressionar uma tecla do teclado
pyautogui.write('chrome') # escrever um texto
pyautogui.press('enter')
link = ('https://www.primevideo.com')
pyautogui.write(link)
pyautogui.press('enter')
sleep(3)
pyautogui.click(x=1196, y=136)
pyautogui.write('The big bang theory')
sleep(0.5)
pyautogui.press('enter')
sleep(1)
pyautogui.click(x=224, y=429)
sleep(2)
pyautogui.hscroll(-500)
pyautogui.click(x=136, y=324)
pyautogui.click(x=134, y=704)
sleep(2)
pyautogui.hscroll(-500)
pyautogui.click(x=534, y=753)
sleep(1.5)
pyautogui.click(x=1728, y=181)