## HAY QUE INSTALAR FLASK PARA QUE ESTO FUNCIONE
## se instala con esto: $ sudo pip install flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'World'
    return 'Hello, {greeting}!'

if __name__ == "__main__":
    app.run()