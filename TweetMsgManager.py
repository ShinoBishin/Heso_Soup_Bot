import random


pushStrList = ["ﾌﾟｼｯ!", "ﾌﾟｼｭﾌﾟｼｭ!!", "ﾌﾟｼｭｳｳｩｩｩ",
               "push!", "ﾌﾟｼｯ‼ﾌﾟｼﾌﾟｼ!!", "ﾌﾟｼｬｱｱｱｧｧｧ…", "ﾌﾟｼｭ!!ﾌﾟｼｭﾌﾟｼｭ!!!!", "ﾊﾞｼｭｳｳｩｩ…", "ﾌﾟｼｨｨｨｨｨｨ", "ﾌﾟｼｭ..."]


class CTweetMessageManager:

    baseStr = []
    checkDuplicateBuf = []

    def __init__(self):
        for base in pushStrList:
            self.baseStr.append(base)

    def checkDuplicate(self, msg):

        if(len(self.checkDuplicateBuf) > 10):
            del self.checkDuplicateBuf[0]

        if msg in self.checkDuplicateBuf:
            return False

        return True

    def createMsg(self):
        msg = random.choice(
            self.baseStr) + random.choice(self.baseStr) + random.choice(self.baseStr)

        while(False == self.checkDuplicate(msg)):
            msg = random.choice(
                self.baseStr) + random.choice(self.baseStr) + random.choice(self.baseStr)

        return msg
