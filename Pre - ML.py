import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
from email.message import EmailMessage
import ssl
import smtplib
from prefect import task, Flow

# Extraer info
@task
def get_price():
    # Info de la pag
    r = requests.get("https://listado.mercadolibre.com.mx/tenis-nike#D[A:tenis%20nike]")
    s = BeautifulSoup(r.content, 'html.parser')
    d = etree.HTML(str(s))
    # Ir entre los divs hasta llegar al precio
    p = d.xpath('//li[@class="ui-search-layout__item"]//div[@class="ui-search-result__content-wrapper shops__result-content-wrapper"]//div[@class="ui-search-item__group ui-search-item__group--price shops__items-group"]/div[1]/div[1]/div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag-amount"]/span[2]')
    print("Precio =", p[0].text)
    # Elegir el precio del producto que queramos
    precio = p[0].text
    return precio

# Comparar el precio para saber cuando se ajuste a tu presupuesto
@task
def comp_precio(precio):
    precio = re.sub(",", "", precio)
    p = int(precio)
    if(p <= 1500):
        return "Te alcanza"
    else:
        return "No te alcanza"

# Enviar un correo para saber si ya se ajustó a tu presupuesto
@task
def s_email(m):
    # Datos de los correos
    em_corr = 'pruebasalv0.01@gmail.com'
    em_cont = 'juddotgguqlabduy'
    rec = 'pruebasalv0.1@gmail.com'
    # Usar instancia de EmailMessage 
    em = EmailMessage()
    em['From'] = em_corr
    em['To'] = rec
    em.set_content(m)
    cont = ssl.create_default_context()
    # Definir servidor y puerto para enviar el correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=cont) as smtp:
        smtp.login(em_corr, em_cont)    # Login para enviar correo
        smtp.sendmail(em_cont, rec, em.as_string()) # Enviar correo

@Flow
def f_Flow():
    pr = get_price()
    m = comp_precio(pr)
    s_email(m)

f_Flow()


