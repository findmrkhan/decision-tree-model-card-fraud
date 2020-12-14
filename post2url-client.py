import requests
import base64
from PIL import Image
from io import BytesIO


#set the target domain name. for same machine use '0.0.0.0' or 'localhost'
targeturl = '0.0.0.0'

PORT = 5005

#Choose the style SK Learn or the DtreeViz library
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

        #Base 64 decoder to deserialise the image data stream
        im = Image.open(BytesIO(base64.b64decode(res.json()['img'])))
        im.save(fname, 'PNG')

        #open the image in the default image viewer
        img = Image.open(fname)
        img.show()

    else:
        print (f"ERROR: status.code = {res.status_code}")


if __name__ == '__main__':
    post2url()

