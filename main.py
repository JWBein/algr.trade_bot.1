import backtrader
import datetime
from strategies import TestStrategy

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(10000)

data = backtrader.feeds.YahooFinanceCSVData(
        dataname='csv.data',

        fromdate=datetime.datetime(2017, 1, 1),

        todate=datetime.datetime(2020, 12, 31),

        reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()