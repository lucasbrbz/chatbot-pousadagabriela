import re
from bot import wppbot
import messages

bot = wppbot('Pousada Gabriela')

bot.iniciar()

ultimo_texto = ''
saudacao = False

while True:
    texto = bot.escuta()
    if ultimo_texto == '' and saudacao is False:
        bot.responde(messages.saudacao)
        saudacao = True
        continue
    elif texto != ultimo_texto and re.match(r'\d', texto):
        ultimo_texto = texto
        texto = texto.lower()
        bot.responde(texto)
    else:
        bot.responde('Não entendi!')
