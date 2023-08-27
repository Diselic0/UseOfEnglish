
import wikipedia

#Creates a list wehit the words the user wants to practice with
import myOpenAi
import random


def create_words_to_remove_list():
    words_to_remove = []
    print("Introduce las palabras a practicar (Presiona enter para terminar la lista) : ")
    while True:
        word = input("")
        if not word:
            break
        words_to_remove.append(word.lower())
    return words_to_remove

#Looks for the words the user wants to practice in the designated file
def search_for_words(file_name, target_word_list):
    try:
        with open(file_name,'r', encoding='utf-8') as fil:
            content = fil.read()
            sentences = content.lower().split('.')


            found_sentences = []
            for one_sentence in sentences:
                for target_word in target_word_list:
                    if target_word in one_sentence:
                        found_sentences.append(one_sentence.strip())
            found_sentences = list(set(found_sentences)) #set deletes the duplicated stings in the list

            fil.close()
    except FileNotFoundError as e:
        print("Error", e)
    return found_sentences




#Obtains an article from wikipedia, filters it content and saves it into a file
def get_wiki_text(titulo):
    wiki = wikipedia.search(titulo, 10, False)
    page = wikipedia.page(wiki[0])

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.writelines(page.content)
        file.close()

    #filter wiki text:
    dirty_lines = page.content.split('. ')
    new_str = ''
    for one_line in dirty_lines:
        if "==" in one_line:
            continue
        new_str += one_line.lower()

    new_str = new_str.replace("\n", "")

    with open('output_cleaned.txt', 'w', encoding='utf-8') as filelile:
        for line in new_str:
            filelile.write(line)
        filelile.close()



#checks for the correct answer
def chek_correct_answer(target_word, answer):
    return target_word == answer.lower

#returns a random phrase whit a target word
def present_phrase_to_guess(target_word_list, found_sentences, pos):
    num_sentences = len(found_sentences)
    for target_word in target_word_list:
        if target_word in found_sentences[pos]:
            return [found_sentences[pos].replace(target_word, '_____'), target_word_list] #we already know this phrases contain ar least one target word


def wrong_answer_subroutine(prepared_sentence, original_sentence, asked_word):

    with open('output_cleaned.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        sentences = content.lower().split('.')
        file.close()
     #this just joines the previos, the sentence we failed to answer correctly with the word replaced by ____ and the next sentence.
     #this provides the full context so that the AI can generate a proper response.
    sentences_for_query = []
    cont = 0
    for one_sentence in sentences:
        if one_sentence == original_sentence:

            if cont > 0:
                sentences_for_query.append(sentences[cont-1])

            sentences_for_query.append(prepared_sentence)

            if cont < len(sentences)-1:
                sentences_for_query.append(sentences[cont + 1])
            break
        cont = cont +1



    option = input("Quieres saber por que no es la respuesta correcta? \nIntroduce 1 para saberlo, cualquier coasa para no\n")

    if option == 1:
        myOpenAi.gpt_querry(sentences_for_query, asked_word)





def present_guess_repeat_routine(tartget_word_list, found_sentences):

    cont = 0

    while cont < len(found_sentences):
        questionANDanswer = present_phrase_to_guess(tartget_word_list, found_sentences, cont)
        print (f"{questionANDanswer[0]}\n")

        if chek_correct_answer(questionANDanswer[1],input('Escribe la solución: \n')):
            print('Respuesta correcta\n')
        else:
            wrong_answer_subroutine(questionANDanswer[0],found_sentences[cont],questionANDanswer[1])

        cont = cont + 1



#New shiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiit

def generateWikiFiles():

    index = 0
    wikiTitles = wikipedia.random(10)

    for title in wikiTitles:
        getWikiText(f'{index}wikiText.txt', title)
        index = index +1




def getWikiText(fileId, title):

    while True:
        try:
            wiki = wikipedia.search(title, 1, False)
            page = wikipedia.page(wiki[0])

        except wikipedia.DisambiguationError as e:
            newTitle = random.choice(e.options)
            title = newTitle

        except wikipedia.PageError as e2:
            newTitle = wikipedia.random(1)
            title = newTitle

        else:
            break

    try:
        with open('rawWiki.txt', 'w', encoding='utf-8') as file:
            file.write('') #empty the content of the file
            file.writelines(page.content)
            file.close()

        # filter wiki text:
        dirty_lines = page.content.split('. ')
        new_str = ''
        for one_line in dirty_lines:
            if "==" in one_line:
                continue
            new_str += one_line

        new_str = new_str.replace("\n", "")

        with open(fileId, 'w', encoding='utf-8') as filelile:
            for line in new_str:
                filelile.write(line)
            filelile.close()
    except FileNotFoundError as e:
        print(f'file {fileId} not found\n')






