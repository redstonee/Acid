from bottle import *
def makeup(x,y):
    line = '{}<br/>'.format('🍋'*x)
    shape = '<h1>Good game!</h1>'+line
    if y == 1:
        return shape

    else:
        for shit in range(1,y):
            shape += line

        return shape

@route('/:x/:y')
def index(x,y):
    return makeup(int(x),int(y))

@route('/')
def hello():
    return "<b>What's your problem?</b>"

run(host = '0.0.0.0',port=80)
