from flask import Flask, request, jsonify
from werkzeug.serving import WSGIRequestHandler
import base64
from cartoongan import cartoonize

app = Flask(__name__)

# https://stackoverflow.com/questions/63765727/unhandled-exception-connection-closed-while-receiving-data
@app.route('/image/convert', methods = ['POST'])
def convert():
    data = request.get_json()#json 데이터를 받아옴
    model_path = './cartoongan/saved_models'
    imgdata = base64.b64decode(data['123'])
    cartoon_img_data = cartoonize.cartoonize2(imgdata, model_path)

    # 받아온 데이터를 다시 전송
    return base64.b64encode(cartoon_img_data), 200

@app.route("/")
def helloWorld():
    return "hello world"

if __name__ == "__main__":
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=False,host='0.0.0.0',port=5000)