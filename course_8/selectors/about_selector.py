import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Elementele dintr-un site web sunt indentificabile  prin intermediul unui link
exemple de tag-uri
- id
-spam
- a( ancora)
- td(table data)
- tr(table row)
- ul(unorder list)
-ol( order list)
- li(list)
- input
-h (h1, h2, h3, h4, h5, h6, )-> h vine de la header( titlu),
    h1 vine de la cel mai mare si h6 de la cel mai mic
-div (divide)
-p ( paragraph)
- etc - o sa le invatati cand aveti nevoie
"""

### hai sa identifica niste elemente ###
# ca sa putem lucra cu browser-ul vom folosi pyton cu selenium
# ca sa putem lucra cu browserul trbuie sa ii dam o comanda sa se deschida

chrome = webdriver.Chrome()
chrome.get("https://www.tutorialspoint.com/index.htm")
# maximizam fereastra
chrome.maximize_window()
time.sleep(2)
