import urllib3
from flask import Flask,render_template,jsonify, request,redirect, url_for, make_response
from flask_cors import CORS
import json
from io import StringIO
app = Flask(__name__) #数据库配置

CORS(app)

@app.route('/',methods=['POST','GET'])
def main ():
    return render_template('index.html')
@app.route('/t', methods=['POST', 'GET'])
def t ():
    data={'messages':0}
    print('00000000000000')
    return jsonify(data),200

@app.route('/ledon',methods=['POST','GET'])
def ledon ():
    f = open('./files/led.txt', 'wb+')
    d = 1
    print('ledon')
    data = json.dumps((d)).encode('utf8')
    f.write(data)
    f.close()
    response={
        'data':1
    }
    return jsonify(response),200
@app.route('/ledoff',methods=['POST','GET'])
def ledoff():
    f = open('./files/led.txt', 'wb+')
    d = 0
    data = json.dumps((d)).encode('utf8')
    f.write(data)
    f.close()
    response={
        'data':0
    }
    return jsonify(response),200

@app.route('/pwmoff',methods=['POST','GET'])
def fengoff():
    f = open('./files/feng.txt', 'wb+')
    d =0
    print('pwmof')
    data = json.dumps((d)).encode('utf8')
    f.write(data)
    f.close()
    response={
        'data':0
    }
    return jsonify(response),200

@app.route('/pwmon',methods=['POST','GET'])
def fengon ():
    f = open('./files/feng.txt', 'wb+')
    d = request.values.get('fre')
    d=int(d)
    print('pwmon')
    print(d)
    data = json.dumps((d)).encode('utf8')
    f.write(data)
    f.close()
    response={
        'data':d
    }
    return jsonify(response),200

@app.route('/text',methods=['POST','GET'])
def send ():
    led = request.values.get('led')
    pwm = request.values.get('pwm')
    fre= request.values.get('fre')
    led=int(led)
    pwm=int(pwm)
    fre = int(fre)

    f = open('./files/led.txt', 'wb+')
    led = json.dumps((led)).encode('utf8')
    f.write(led)
    print(led)
    f.close()

    print(type(pwm))
    if(pwm==0):
        fre=0
    f = open('./files/feng.txt', 'wb+')
    fre = json.dumps((fre)).encode('utf8')
    f.write(fre)
    f.close()
    response={
        'yes':1001
    }
    return jsonify(response),200

@app.route('/client_pwm',methods=['POST','GET'])
def client_pwm ():
    f = open('./files/feng.txt', 'r')
    pwm=f.read()
    f.close()
    print(pwm)
    response={
        'pwm':pwm
    }
    print('pwmpwm')
    return jsonify(response),200


@app.route('/client_led',methods=['POST','GET'])
def client_led ():
    f = open('./files/feng.txt', 'r')
    pwm=f.read()
    f.close()
    print(pwm)

    f = open('./files/led.txt', 'r')
    led=f.read()
    f.close()
    print(led)
    led=pwm+led
    print(led)
    response={
        'led':led,
    }
    print('ledled')
    return jsonify(response),200

# @app.route('/client_led',methods=['POST','GET'])
# def client_led ():
#     f = open('./files/feng.txt', 'r')
#     pwm=f.read()
#     f.close()
#     print(pwm)
#
#     f = open('./files/led.txt', 'r')
#     led=f.read()
#     f.close()
#     print(led)
#
#     response={
#         'led':led,
#         'pwm': pwm
#     }
#     print('ledled')
#     return jsonify(response),200

@app.route('/update',methods=['POST','GET'])
def update ():
    f = open('./files/led.txt', 'r')
    led=f.read()
    f.close()

    f = open('./files/feng.txt', 'r')
    fre=f.read()
    f.close()

    print(type(led))
    print(type(fre))
    response={
        'led':led,
        'fre':fre
    }
    return jsonify(response),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    #app.run(host='127.0.0.1', port=5000, debug=True)