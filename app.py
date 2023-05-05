from flask import Flask, request, jsonify
from waitress import serve

import time
from urllib.request import ProxyHandler, build_opener, install_opener, Request, urlopen

from stem import Signal
from stem.control import Controller

import os

# setup tor handler

class TorHandler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

    def open_url(self, url):
        # communicate with TOR via a local proxy (privoxy)
        def _set_url_proxy():
            proxy_support = ProxyHandler({'http': '127.0.0.1:8118'})
            opener = build_opener(proxy_support)
            install_opener(opener)

        _set_url_proxy()
        request = Request(url, None, self.headers)
        return urlopen(request).read().decode('utf-8')

    @staticmethod
    def renew_connection():
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='my_password')
            controller.signal(Signal.NEWNYM)
            controller.close()

tor_handler = TorHandler()

def chip():
    tor_handler.renew_connection()
    ip = tor_handler.open_url('http://icanhazip.com/')
    return ip

# setup api
app = Flask(__name__)

@app.route('/changeip', methods=['GET'])
def change_ip():
    try:
        res = chip()
        return jsonify({'new_ip': res})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    cmd = '/etc/init.d/tor start&&/etc/init.d/privoxy start'
    os.system(cmd)
    
    serve(app, host="0.0.0.0", port=5000)