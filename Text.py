class Text:

    def __init__(self, name, directory, wikitext):
        self.name = name
        self.directory = directory
        self.sentenceList = []
        self.wikitext = wikitext

        self._fillSentenceList()




    def getName(self):
        return self.name

    def getDirectory(self):
        return self.directory

    def _fillSentenceList(self):

        try:
            with open(self.name, 'r', encoding='utf=8') as file:

                content = file.read()
                self.sentenceList = content.split('.')
                file.close()

        except FileNotFoundError as e:
            print("Error", e)







