import joblib
import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify, request
import sys
import random

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = NpEncoder
modelo = None

# Função para gerar uma lista de valores aleatórios
def generate_random_list(size, lower=-1.0, upper=1.0):
    return [random.uniform(lower, upper) for _ in range(size)]


@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER IS RUNNING! \n" + json.dumps({
        "args": str(sys.argv),
    })

@app.route("/predict", methods=['GET', 'POST'])
def call_predict(request = request):
    print(request.values)

    json_ = request.json
    campos = pd.DataFrame(json_)

    if campos.shape[0] == 0:
        return "Dados de chamada da API estão incorretos.", 400

    # Gerar uma lista de 4 valores aleatórios
    random_list = generate_random_list(4)
    random_list

    ret = {'prediction': random_list}

    return app.response_class(response=json.dumps(ret, cls=NpEncoder), mimetype='application/json')

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        args.append('./models/model2.joblib')
    if len(args) < 2:
        args.append('8080')

    print(args)

    # app.run(port=8080, host='0.0.0.0')
    app.run(port=args[1], host='0.0.0.0')
    pass

