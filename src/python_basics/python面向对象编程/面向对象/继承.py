class FA(object):
    def show(self):
        print("FA Show Run...")

class FB(object):
    def show(self):
        print("FB Show Run...")

class S(FB, FA):
    def s_show(self):
        print("S Show Run...")


s = S()
s.s_show()
s.show()
