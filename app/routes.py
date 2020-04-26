from flask import Flask,request,jsonify
from basic_func.prime import prime
from basic_func.func1 import addition
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<!DOCTYPE html > \
    <html > \
    <body > \
    <h1> Test line 1 </h1> \
    <p> My first paragraph. </p> \
    </body> \
    </html>'   


@app.route('/sum')
def sumofnumbers():
    val1 = request.args.get('a',type = str)
    val2 = request.args.get('b', type=str)
    b = (addition(val1, val2))
    d=jsonify({'description':'sum calculate',
                'output':b})
    return d
@app.route('/prime')
def checkprime():
    num=request.args.get('a',type=str)
 #   b="the " + num+ " is" + str(prime(num)) + " number."
#    return b
    b=prime(num)  
    c=jsonify({'description':'prime calculation',
               'output':b})
    return c
if __name__ == '__main__':
    app.run()
