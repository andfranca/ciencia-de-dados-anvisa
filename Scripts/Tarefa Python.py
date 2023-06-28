#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import datetime

def criar_arquivo_csv():
    # Obter a data e hora atual
    data_hora_atual = datetime.datetime.now().strftime('%Y%m%d%H%M')

    # Definir o nome do arquivo com base na data e hora atual
    nome_arquivo = f'C:/Users/ander/OneDrive/Área de Trabalho/ciencia-de-dados-anvisa/Scripts/arquivo_{data_hora_atual}.csv'

    # Criar o arquivo CSV
    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['Coluna 1', 'Coluna 2', 'Coluna 3'])
        # Adicionar linhas adicionais ao arquivo, se necessário

    print(f'Criado arquivo: {nome_arquivo}')

# Chamar a função criar_arquivo_csv para criar um novo arquivo CSV
criar_arquivo_csv()


# In[ ]:




