
from flask import Flask, request, make_response, jsonify
from dtreevizgraph import *
from sklearngraph import *
import json


model = None
#initialise Flask app
app = Flask(__name__)

#add a route just for testing
@app.route('/')
def home_endpoint():
    return 'Model is ready to predict. Use the /getCardFraudDtree verb!'

#add a route just for getting the decision tree images through the REST web service
@app.route('/getCardFraudDtree', methods=['POST'])
def getCardFraudDTree():
    # Works only for a single sample.
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        stat = None
        in_json = json.dumps(data)
        y = json.loads(in_json)
        output = {}
        # For invalid input send error
        if y['style'] is None :
            output['status'] = 'error'
            output['img'] = ''
            return json.dumps(output)

        barray = None
        # If old SK Learn style is needed. Else new DtreeViz style tree will be created and served
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
        #return the response in the JSON API format
        return make_response(jsonify(output))


if __name__ == '__main__':
    #listen on port 5005
    app.run(host='0.0.0.0', port=5005)

