from flask import Flask
app=Flask(__name__)

@app.route('/helloworld')
def helloworld():
    return 'Hello world!\nThis is demo application. Goodbye :) '

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, %s!' % name

@app.route('/count/<int:number>')
def count(number):
    return 'Just display the number, %d!' % number



if __name__ == "__main__":
    app.debug = True
    app.run()