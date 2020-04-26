from flask import jsonify
def json(func,b):
    c=jsonify({'description':func,
                'output':b})
    return c