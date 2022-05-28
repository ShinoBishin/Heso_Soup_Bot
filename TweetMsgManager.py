import random


pushStrList = ["ﾌﾟｼｯ!", "ﾌﾟｼｭﾌﾟｼｭ!!", "ﾌﾟｼｭｳｳｩｩｩ",
               "push!", "ﾌﾟｼｯ‼ﾌﾟｼﾌﾟｼ!!", "ﾌﾟｼｬｱｱｱｧｧｧ…", "ﾌﾟｼｭ!!ﾌﾟｼｭﾌﾟｼｭ!!!!"]


class CTweetMessageManager:

    baseStr = []

    def __init__(self):
        for base in pushStrList:
            self.baseStr.append(base)

    def createMsg(self):
        return random.choice(self.baseStr) + random.choice(self.baseStr)
