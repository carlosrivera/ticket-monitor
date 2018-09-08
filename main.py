import requests

r = requests.post(
    'http://gobiernoenlinea1.jalisco.gob.mx/vehicular/adeudo.jsp',
    data = {
        'placa':'JKG6000',
        'numserie':'02291'
    }
)

print(r)
