from flask import Flask

app = Flask(__name__)


@app.route('/flask-intro')
def hello_world():  # put application's code here
    return 'Hello.vue World!'


if __name__ == '__main__':
    app.run()
