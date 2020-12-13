
from flask import Flask, request, make_response, jsonify
from dtreevizgraph import *
from sklearngraph import *
import json


model = None
app = Flask(__name__)


@app.route('/')
def home_endpoint():
    return 'Model is ready to predict. Use the /getCardFraudDtree verb!'


@app.route('/getCardFraudDtree', methods=['POST'])
def getCardFraudDTree():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        stat = None
        in_json = json.dumps(data)
        y = json.loads(in_json)
        output = {}

        if y['style'] is None :
            output['status'] = 'error'
            output['img'] = ''
            return json.dumps(output)

        barray = None
        if y['style'] == 'sklearn':
            barray = getSKLearnImg()
        elif y['style'] == 'dtreeviz':
            barray = getDtreeVizImg()
        else:
            barray = None

        if barray is None:
            stat = 'error'
        else:
            stat = 'success'

        output = {
            'img' : barray,
            'status' : stat
        }

        return make_response(jsonify(output))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

