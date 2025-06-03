from flask import Flask

app = Flask(__name__)
@app.route('/provs/<cod>')
def provs(cod):
    with open('prov.txt','r', encoding='utf-8') as prov:
        for reg in prov:
            codigo,provincia = reg.strip().split(',')
            if cod==codigo:
                return provincia
    return 'No encontrado'