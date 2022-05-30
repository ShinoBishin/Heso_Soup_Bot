import random


pushStrList = ["ﾌﾟｼｯ!", "ﾌﾟｼｭﾌﾟｼｭ!!", "ﾌﾟｼｭｳｳｩｩｩ",
               "push!", "ﾌﾟｼｯ‼ﾌﾟｼﾌﾟｼ!!", "ﾌﾟｼｬｱｱｱｧｧｧ…", "ﾌﾟｼｭ!!ﾌﾟｼｭﾌﾟｼｭ!!!!", "ﾊﾞｼｭｳｳｩｩ…", "ﾁｮﾛﾛﾛﾛ…", "ﾁｮﾛ..."]


class CTweetMessageManager:

    baseStr = []

    def __init__(self):
        for base in pushStrList:
            self.baseStr.append(base)

    def createMsg(self):
        # TODO: msg生成処理の拡張
        return str(random.randint(self.baseStr)) + random.choice(self.baseStr) + random.choise(self.baseStr)


# ツイート重複回避(暫定)
# duplicateList = checkDuplicate(message, info)
# while(duplicateList.count(message) > 0):
#     message = msgManager.createMsg()
#     duplicateList = checkDuplicate(message, info)
