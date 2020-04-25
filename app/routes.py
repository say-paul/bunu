from flask import Flask
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


if __name__ == '__main__':
   app.run()
