from flask import Flask, jsonify, render_template, send_file, request
from flask_cors import CORS, cross_origin
import json
import requests





app = Flask(__name__)
cors = CORS(app)


app.config['CORS_HEADERS'] = "Content-Type"



@app.route('/download', methods=['GET','POST'])
def hello():
   if request.method == 'POST':
      data = request.get_json()
      print(data)
      r = requests.get(data, stream=True)
      fileName='./videos/'+data[31:35]+'.mp4'
      print('downloading...')
      with open(fileName, 'wb') as f:
         for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
               f.write(chunk)

      print('done')
      data=jsonify(data)
      return data
    


# Running/Starting the server
if __name__ ==  '__main__':
  app.run(debug=True)
 