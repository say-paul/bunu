from flask import Flask
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
    b = "sum of 5 and 7 is:" + str(addition(5, 7))
    print (b)
    return b

    

if __name__ == '__main__':
   app.run()
