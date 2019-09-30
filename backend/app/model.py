class UserPositon(object):
    def __init__(self, instrumentId, tradingOn, amount, qty, pnlRatio):
        self.instrumentId = instrumentId  # 仓位描述
        self.tradingOn = tradingOn  # 仓位货币
        self.amount = amount  # 货币数量
        self.qty = qty  # 张数
        self.pnlRatio = pnlRatio  # 持有比例变化

    def position2dict(self):
        return {
            'instrumentId': self.instrumentId,
            'tradingOn': self.tradingOn,
            'amount': self.amount,
            'qty': self.qty,
            'pnlRatio': self.pnlRatio
        }


# 构造UserPosition
def create_position(data):
    return UserPositon(
        data["instrumentId"],
        data["tradingOn"],
        data["amount"],
        data["qty"],
        data["pnlRatio"]
    )


class UserDealRecord(object):
    def __init__(self, content, label, exch, unit, labelSub, sym, informTime):
        self.content = content
        self.label = label
        self.exch = exch
        self.unit = unit
        self.labelSub = labelSub
        self.sym = sym
        self.informTime = informTime

    def record2dict(self):
        return {
            'content': self.content,
            'label': self.label,
            'exch': self.exch,
            'unit': self.unit,
            'labelSub': self.labelSub,
            'sym': self.sym,
            'informTime': self.informTime
        }


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


class UserPositionStatus(object):

    def __init__(self, ratio, symbol):
        self.ratio = ratio
        self.symbol = symbol

    def status2dict(self):
        return {
            'ratio': self.ratio,
            'symbol': self.symbol
        }


def create_status(data):
    return UserPositionStatus(
        data['ratio'],
        data['symbol']
    )