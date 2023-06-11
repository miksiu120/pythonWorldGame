

class LogPanel:

    def __init__(self, logArray):
        self.logArray = logArray

    def writeLogs(self):
        for log in self.logArray:
            print(log)

