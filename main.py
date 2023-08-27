import os
import utility
import myOpenAi
import Text

def main():

    #generate the wiki files:
    utility.generateWikiFiles()

    #select the text option

    opt = 1
    '''while opt != 1:
        opt = input('Elige la opción de texto:\n'
                    '-op 1: wikipedia text\n'
                    '-op 2: you r gay\n')
'''
    if opt == 1:

        #generate the text objects:
        text0 = Text.Text('0wikiText.txt', os.path.dirname('0wikiText.txt'), True)
        text1 = Text.Text('1wikiText.txt', os.path.dirname('1wikiText.txt'), True)
        text2 = Text.Text('2wikiText.txt', os.path.dirname('2wikiText.txt'), True)
        text3 = Text.Text('3wikiText.txt', os.path.dirname('3wikiText.txt'), True)
        text4 = Text.Text('4wikiText.txt', os.path.dirname('4wikiText.txt'), True)
        text5 = Text.Text('5wikiText.txt', os.path.dirname('5wikiText.txt'), True)
        text6 = Text.Text('6wikiText.txt', os.path.dirname('6wikiText.txt'), True)
        text7 = Text.Text('7wikiText.txt', os.path.dirname('7wikiText.txt'), True)
        text8 = Text.Text('8wikiText.txt', os.path.dirname('8wikiText.txt'), True)
        text9 = Text.Text('9wikiText.txt', os.path.dirname('9wikiText.txt'), True)

        textList = []
        textList[text0, text1, text2, text3, text4, text5, text6, text7, text8, text9]


main()





