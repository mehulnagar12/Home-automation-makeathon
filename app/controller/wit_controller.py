from wit import Wit
import os

client = Wit(os.environ["API_WIT"])

def test(message):
    resp = client.message(message)
    print(str(resp))
