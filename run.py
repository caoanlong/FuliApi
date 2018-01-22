
from flask import Flask

app = Flask(__name__)


@app.route('/aaa')
def fuck():
    return 'nimade'

app.run()

