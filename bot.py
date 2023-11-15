import os
import time

from chatterbot import ChatBot
from selenium import webdriver


class wppbot:
    dir_path = os.getcwd()

    def __init__(self, nome_bot):
        self.bot = ChatBot(nome_bot)
        self.bot.set_trainer(ListTrainer)
        self.chrome = self.dir_path + '\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir=" + self.dir_path + "\profile\wpp")
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def iniciar(self):
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)
        self.caixa_de_pesquisa = self.driver.find_element_by_class_name('jN-F5')
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2S1VP')
        self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')

    def buscaContato(self, nome_contato):
        self.caixa_de_pesquisa.send_keys(nome_contato)
        time.sleep(2)
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
        self.contato.click()
        time.sleep(2)

    def responde(self, mensagem):
        for frase in mensagem:
            self.caixa_de_mensagem.send_keys(frase)
            time.sleep(1)
            self.botao_enviar.click()
            time.sleep(1)

    def escuta(self):
        # Vamos setar todos as mensagens no grupo.
        post = self.driver.find_elements_by_class_name('_3_7SH')
        # Vamos pegar o índice da última conversa.
        ultimo = len(post) - 1
        # Vamos pegar o  texto da última conversa e retornar.
        texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto

