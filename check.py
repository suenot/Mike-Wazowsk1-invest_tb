import keyring
from tinkoff.invest import CandleInterval, Client

from tinkoff.invest import Client
import logging

from stats.stats_data import Stats

logger = logging.getLogger(__name__)

figi = "BBG004730N88"
TOKEN = keyring.get_password('TOKEN', 'INVEST')
SANDBOX_TOKEN = keyring.get_password('TOKEN', 'SANDBOX')
sandbox_account_id = keyring.get_password('ACCOUNT_ID', 'SANDBOX')


def select_strategy():
    pass





def main():
    with Client(token=TOKEN) as client:
        # select strategy for current user and figi
        strategy = select_strategy()

        stats = Stats(client)
        historical_data = stats.get_historical_candles(figi=figi, interval=CandleInterval(5), period='mon')
        features = stats.make_features(df=historical_data,ma_window=5,ema_window=30)
        print(features)

if __name__ == "__main__":
    main()
