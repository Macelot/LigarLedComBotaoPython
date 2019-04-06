#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Botão liga LED                                           #
#  Quando o botão do pino 16 é pressionado                  #
#  o LED do pino 12 liga                                    #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO
from gpiozero import LED, Button
#Importação da biblioteca time para utilizar o método sleep
from time import sleep
#Importação da biblioteca random para utilizar o método uniform
from random import uniform
#Note que não será utilizada a GPIO.BOARD, desta forma o
# setimo pino é a GPIO 4
led = LED(18) #12 pino real
ligaDesliga = Button(23)  #16 pino real
led.off()

def clica():
    led.on()
    print('Ligado!')
    
def solta():
    led.off()
    print('Apagado!')

try:     
	while(True):
		ligaDesliga.when_pressed = clica
		sleep(0.1)
		ligaDesliga.when_released = solta
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()		
#Fonte: Raspberry pi Fundation
