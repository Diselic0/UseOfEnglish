class sentence:

    def __init__(self,index, content):

        self.index = index
        self.targetWordsInSen = []
        self.content = content


    def getIndex(self):
        return self.index

    def getTargetWordsInSen(self):
        return self.targetWordsInSen

    def getContent(self):
        return self.content

    def _lookForTargetWords(self, targetWordsList):


        for targetWord in targetWordsList:
            if targetWord in self.content:
                self.targetWordsInSen.append(targetWord)



