import os
import json
import re
import requests
import scrapy
from munch import Munch
from tinydb import TinyDB, Query

data_file = '../data/db.json'

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
    tickets = []

    docs = db.all()

    for q in docs:
        q = Munch(q)
        ticket = Munch(get_tickets(q.plate, q.serial))

        if ticket and ticket.status == 0 and ticket.adeudo:
            if len(ticket.adeudo) != q.ticketcount:
                q.notified = False

            if not notified and q.update:
                for bill in ticket.adeudo:
                    bill = Munch(bill)

                    #{'baselegal': , 'cantidad': 1, 'concepto': 44229, 'descripcion': , 'periodo': 2018, 'porcentaje': 100.0, 'idrow': 1, 'fechavenc': '', 'Folio': '113|272542007', 'Fecha': 1528952400000, 'numReq': 0, 'Tipo': 'M', 'ImpBase': 806.0, 'Beneficiario': 71947, 'Importe': 806.0, 'FotoInf': ''}
                    tickets.append({
                        'description': bill.descripcion,
                        'percentage': bill.porcentaje,
                        'number': bill.Folio,
                        'type': bill.Tipo,
                        'tax': bill.ImpBase,
                        'due': bill.Importe
                    })

                from sparkpost import SparkPost

                sparky = SparkPost(os.environ['SPARKPOST_API_KEY'])

                response = sparky.transmissions.send(
                    use_sandbox = True,
                    recipients = [q.email],
                    html = '<html><body><p>Se encontraron nuevas multas, puedes consultarlas en la página oficial de la Secretaría de Movilidad.</p></body></html>',
                    from_email = 'testing@sparkpostbox.com',
                    subject = 'Se ha encontrado una nueva multa'
                )

                q.notified = True
                q.ticketcount = len(ticket.adeudo)

    db.write_back(docs)

    return tickets

def get_user_tickets(plate = 'JKG6000', serial = '02291'):
    tickets = []

    if plate and serial:
        ticket = Munch(get_tickets(plate, serial))

        if ticket and ticket.status == 0 and ticket.adeudo:
            for bill in ticket.adeudo:
                bill = Munch(bill)

                #{'baselegal': , 'cantidad': 1, 'concepto': 44229, 'descripcion': , 'periodo': 2018, 'porcentaje': 100.0, 'idrow': 1, 'fechavenc': '', 'Folio': '113|272542007', 'Fecha': 1528952400000, 'numReq': 0, 'Tipo': 'M', 'ImpBase': 806.0, 'Beneficiario': 71947, 'Importe': 806.0, 'FotoInf': ''}
                tickets.append({
                    'description': bill.descripcion,
                    'percentage': bill.porcentaje,
                    'number': bill.Folio,
                    'type': bill.Tipo,
                    'tax': bill.ImpBase,
                    'due': bill.Importe
                })

    return tickets

def save_user(plate, serial, email, update):
    db = TinyDB(data_file)

    q = Query()

    if not db.search((q.plate == plate) & (q.serial == serial)):
        db.insert({
            'plate': plate,
            'serial': serial,
            'email': email,
            'update': update,
            'notified': False,
            'ticketcount': 0
        })
