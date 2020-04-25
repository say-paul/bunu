from flask import Flask,request
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
    b = "sum of " + val1 + " and " + val2 + " is: " + str(addition(val1, val2))
    return b

    

if __name__ == '__main__':
   app.run()
