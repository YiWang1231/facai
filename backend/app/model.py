class Essential(object):

    def data2dict(self):
        dict = {}
        for name, value in vars(self).items():
            dict[name] = value
        return dict


class UserPositon(Essential):
    def __init__(self, instrumentId, tradingOn, amount, qty, pnlRatio):
        self.instrumentId = instrumentId  # 仓位描述
        self.tradingOn = tradingOn  # 仓位货币
        self.amount = amount  # 货币数量
        self.qty = qty  # 张数
        self.pnlRatio = pnlRatio  # 持有比例变化


# 构造UserPosition
def create_position(data):
    return UserPositon(
        data["instrumentId"],
        data["tradingOn"],
        data["amount"],
        data["qty"],
        data["pnlRatio"]
    )


class UserDealRecord(Essential):
    def __init__(self, content, label, exch, unit, labelSub, sym, informTime):
        self.content = content
        self.label = label
        self.exch = exch
        self.unit = unit
        self.labelSub = labelSub
        self.sym = sym
        self.informTime = informTime


# 构造UserDealRecord
def create_record(data):
    return UserDealRecord(
        data["content"],
        data["label"],
        data["exch"],
        data["unit"],
        data["labelSub"][0],
        data['sym'],
        data['informTime']
    )


class UserPositionStatus(Essential):
    fields = ['ratio', 'symbol']

    def __init__(self, ratio, symbol):
        self.ratio = ratio
        self.symbol = symbol


def create_status(data):
    return UserPositionStatus(
        data['ratio'],
        data['symbol']
    )


if __name__ == "__main__":
    data = {
        'ration': 0.6,
        'symbol': 'BTC'
    }
    print(data['ration'])
    ps = UserPositionStatus(data)
    print(ps.data2dict())
