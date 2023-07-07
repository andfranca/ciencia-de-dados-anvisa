#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('-icognito')
option.add_argument('--headless')

navegador = webdriver.Chrome(options=option)

navegador.get('https://forms.gle/12M8rdtJeVLK6JHk6')
campos = navegador.find_elements(By.CLASS_NAME,'whsOnd')
campos[0].send_keys('Anderson2')
campos[1].send_keys('31')
campos[2].send_keys('São Paulo2')
enviar = navegador.find_elements(By.CLASS_NAME,'NPEfkd')
enviar[0].click()
navegador.close()

