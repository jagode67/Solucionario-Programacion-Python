from flask import Flask

app = Flask(__name__)
@app.route('/provs')
def provs():
    with open('prov.txt','r', encoding='utf-8') as prov:
        provs=prov.read()
    return provs