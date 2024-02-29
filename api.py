import random 
import json
from flask import Flask, request, jsonify




app = Flask(__name__)

@app.route('/consume_json', methods=['GET'])
def consume_json():

    semilla =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    conjuntoLetras = [ 'ba', 'ca', 'da', 'fa']


    def generar_nombre():
        
        letras = []
        for i in range(0,random.randint(2, 10)):

            letras.append(random.choice(semilla))
        
        name = "".join(letras)

        return name


    def generar_correo():
        
        letrasCorreo = []
        for i in range(0,4):

            letrasCorreo.append(random.choice(semilla))
        
        letrasCorreo.append("@")
        
        for i in range(0,6):

            letrasCorreo.append(random.choice(conjuntoLetras))
        
        letrasCorreo.append(".com")
        
        correo = "".join(letrasCorreo)

        return correo

    def generar_password():
        letrasPassword = []

        for i in range(0,random.randint(4, 15)):

            letrasPassword.append(random.choice(semilla))
        
        password = "".join(letrasPassword)

        return password

    # Aquí genero el json con los 500.000 elementos cada uno con su nombre, correo y password. 
    jsonLista = []

    for i in range(0,500000):
        element = {}
        element["Name"] = generar_nombre()
        element["Email"] = generar_correo()
        element["Password"] = generar_password()
        jsonLista.append(element)

    jsonFile = json.dumps(jsonLista)


    # Tomo el json grande, lo cargo, ingreso los datos en una lista para luego colocarlos en las graficas
    jsonFile = json.loads(jsonFile)

    jsonSalidaLista = []
    jsonSalidaDict = {}
    conteoPass = 0
    listaDominios = []

    for elemento in jsonFile:
        
        if len(elemento['Password']) > 8:
            conteoPass += 1
        correo = elemento['Email'].split("@")
        listaDominios.append(correo[1])


    DominiosDistintos = len(set(listaDominios))


    jsonSalidaDict['conteoPasswordChar'] = conteoPass
    jsonSalidaDict['dominiosDiferentes'] = DominiosDistintos

    jsonSalidaLista.append(jsonSalidaDict)


    return jsonify(jsonSalidaLista)

if __name__ == '__main__':
    app.run(debug=True)




