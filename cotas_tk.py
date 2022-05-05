import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_df = requisicao.json()

    cotacao_dolar = requisicao_df['USDBRL']['bid']
    cotacao_euro = requisicao_df['EURBRL']['bid']
    cotacao_bitcoin = requisicao_df['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_bitcoin}
    '''
    texto_cotacoes['text'] = texto

janela = Tk()
janela.title('Cotação Atual Dólar/Euro/Bitcoin')

instrucao = Label(janela, text='Clique no botão para receber as cotações atualizadas.')
instrucao.grid(row=0, column=0, padx=5, pady=5)

botao = Button(janela, text='Buscar cotações: Dólar/Euro/Bitcoin', command=pegar_cotacoes)
botao.grid(row=1, column=0, padx=5, pady=5)

texto_cotacoes = Label(janela, text='...')
texto_cotacoes.grid(row=2, column=0, padx=5, pady=5)

janela.mainloop()