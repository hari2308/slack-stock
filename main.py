from send_msg import send
from nsetools import Nse
import json


@send
def hello(nse):
    a = {k:v for k,v in json.loads(nse.get_quote("tcs", as_json=True)).items() if v is not None}
    print(a)
    return a

def main():
    nse = Nse()
    hello(nse)


if __name__ == "__main__":
    main()
