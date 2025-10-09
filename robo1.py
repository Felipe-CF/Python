import xlsxwriter, os, keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoPausaComputador

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

sessaoNavegador = webdriver.Chrome(options=options)

sessaoNavegador.get(url='https://g1.globo.com/economia/noticia/2025/03/21/emprestimo-consignado-a-celetistas-comeca-nesta-sexta-feira-sem-regulamentacao-do-fgts-como-garantia.ghtml')

tempoPausaComputador.sleep(10)

moeda1 = sessaoNavegador.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div[1]/div/div[3]/div[1]/div/div[1]/strong")

print(moeda1.get_attribute('innerHTML'))

moeda1_cotacao = sessaoNavegador.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[1]")

print(moeda1_cotacao.get_attribute('innerHTML'))

nomeCaminhoArquivo = "C:\\Users\\FelipeCF\\Desktop\\Codigos\\Python\\Moedas.xlsx"

planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)

planilha1 = planilhaCriada.add_worksheet()

planilha1.write("B2", moeda1.get_attribute('innerHTML'))
planilha1.write("C2", moeda1_cotacao.get_attribute('innerHTML'))

planilhaCriada.close()

os.startfile(nomeCaminhoArquivo)

tempoPausaComputador.sleep(5)

sessaoNavegador.quit()

