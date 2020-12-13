import requests
import base64
from PIL import Image
from io import BytesIO


targeturl = '0.0.0.0'

PORT = 5005

#style = 'sklearn'
style = 'dtreeviz'

endpoint = 'getCardFraudDtree'

def post2url():
    url = f'http://{targeturl}:{PORT}/{endpoint}'
    print (f'\nurl :{url}\n')
    fname =  'outfilename.png'
    headers = { 'Accept': 'application/json', 'Content-Type': 'application/json'}
    inReq = f"{{      \"style\" : \"{style}\" }}"
    print ("Contacting server .... ")
    res = None
    try:
        res = requests.post(url, data= inReq, headers=headers)
    except ConnectionError:
        print ('Error connecting to the URL endpoint')

    if res.status_code == 200 :
        print('Response image: ', res.json()['img'])

        im = Image.open(BytesIO(base64.b64decode(res.json()['img'])))
        im.save(fname, 'PNG')
        #img = Image.open(fname)
        #img.show()

    else:
        print (f"ERROR: status.code = {res.status_code}")


if __name__ == '__main__':
    post2url()

