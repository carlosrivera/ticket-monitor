import json
import re
import requests
import scrapy
from munch import Munch
from tinydb import TinyDB, Query

data_file = 'data/db.json'

def get_tickets(plate = 'JKG6000', serial = '02291'):
    regex = r"var adeudo = '(.*?)';"

    response = requests.post(
        'http://gobiernoenlinea1.jalisco.gob.mx/vehicular/adeudo.jsp',
        data = {
            'placa': plate,
            'numserie': serial
        },
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
    )

    selector = scrapy.Selector(text=response.text)

    for script in selector.xpath('//script/text()').extract():
        matches = re.finditer(regex, script, re.MULTILINE)

        for i, match in enumerate(matches):
            for group in range(0, len(match.groups())):
                return json.loads(match.group(group + 1))

    return None

def get_users_tickets():
    db = TinyDB(data_file)

    for q in db.all():
        q = Munch(q)
        ticket = Munch(get_tickets(q.plate, q.serial))

        if ticket.adeudo:
            tickets = []
            for bill in ticket.adeudo:
                bill = Munch(bill)

                #{'baselegal': , 'cantidad': 1, 'concepto': 44229, 'descripcion': , 'periodo': 2018, 'porcentaje': 100.0, 'idrow': 1, 'fechavenc': '', 'Folio': '113|272542007', 'Fecha': 1528952400000, 'numReq': 0, 'Tipo': 'M', 'ImpBase': 806.0, 'Beneficiario': 71947, 'Importe': 806.0, 'FotoInf': ''}
                tickets.append({
                    'description': bill.descripcion,
                    'percentage': bill.porcentaje,
                    'number': bill.folio,
                    'type': bill.tipo,
                    'tax': bill.impuesto,
                    'due': bill.importe
                })

            print(tickets)

def save_user(plate, serial, email):
    db = TinyDB(data_file)

    q = Query()

    if not db.search((q.plate == plate) & (q.serial == serial)):
        db.insert({
            'plate': plate,
            'serial': serial,
            'email': email,
            'notified': False,
        })

save_user('JKG6000', '02291', 'me@example.im')
get_users_tickets()
