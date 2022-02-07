from flask import Flask
from threading import Thread
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask('')
@app.route('/')
def main():
    return ('<p style="text-align: center;"><strong>YouTube:</strong> Zardex 1337<br /><strong>Discord:</strong> Zardex?#1337</p><p style="text-align: center;">&nbsp;</p>')
def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

    