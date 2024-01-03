from flask import Flask

app = Flask(__name__)

@app.route('/post_email', methods=['POST'])
def post_email():
    return 'Server received the POST request.'

if __name__ == '__main__':
    app.run
