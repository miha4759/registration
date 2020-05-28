import json

import requests
from hyper.contrib import HTTP20Adapter
from requests import Timeout
from requests.exceptions import ProxyError


class Registration(object):
    session = None
    phone = None

    def __init__(self, phone, session: requests.Session = requests.Session()):
        self.session = session
        self.phone = phone

    def try_register_phone(self):
        request = None
        try:
            self.session.mount('https://api.grab.com', HTTP20Adapter())
            request = self.session.post('https://api.grab.com/grabid/v1/phone/otp', timeout=20, headers={
                "User-Agent": "Grab/5.95.1 (Android 9; Build 15313556)",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": None,
                "Connection": None,
                "Accept-Encoding": "gzip",
                "Accept-Language": "en-US;q=1.0, en;q=0.9",
            }, data={
                'method': 'SMS',
                'countryCode': 'RU',
                'phoneNumber': self.phone,
                'templateId': 'pax_android_production',
                'numDigits': 6,
            })
        except Timeout:
            raise ProxyError()
        except json.JSONDecodeError:
            raise ValueError('unexpected answer: %d' % request.status_code)

        return request
