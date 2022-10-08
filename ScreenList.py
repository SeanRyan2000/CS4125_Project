from Screen import Screen

class ScreenList:
    def __init__(self, numScreens):
        self.screenList = self.setUpScreens(numScreens)

    def setUpScreens(self, numScreens):
        screenList = []
        for x in range(numScreens):
            s = Screen(x + 1)
            screenList.append(s)
        
        return screenList

    def printScreenList(self):
        for s in self.screenList:
            print("Screen " + str(s.screenNum))