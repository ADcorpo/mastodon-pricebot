import krakenex
from mastodon import Mastodon

from exceptions import *


kraken = krakenex.API()
xmr_price = kraken.query_public('Ticker',
                           {
                               'pair': 'XXMRZEUR, XXMRZUSD'
                           })

if xmr_price['error'] != []:
    raise KrakenError(xmr_price['error'])

mastodon = Mastodon(client_id="apptoken.cfg",
                    access_token="usertoken.cfg",
                    api_base_url="https://mastodon.hackerlab.fr")

mastodon.toot("Latest Monero price according to kraken: \n {0} USD \n {1} EUR".format(
    xmr_price["result"]["XXMRZUSD"]["a"][0],
    xmr_price["result"]["XXMRZEUR"]["a"][0]))
