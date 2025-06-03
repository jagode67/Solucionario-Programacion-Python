from flask import Flask,jsonify

app = Flask(__name__)
@app.route('/provs')
def provs():
    resultado=[];
    with open('prov.txt','r', encoding='utf-8') as prov:
        for reg in prov:
            codigo,provincia = reg.strip().split(',')
            resultado.append({
                "codigo": codigo,
                "provincia": provincia
            })
    return jsonify(resultado)