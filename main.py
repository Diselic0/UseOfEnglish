import sys

import wikipedia


def create_words_to_remove_list():
    words_to_remove = []
    print("Introduce las palabras a practicar (Presiona enter para terminar la lista) : ")
    while True:
        word = input("")
        if not word:
            break
        words_to_remove.append(word.lower())
    return words_to_remove

def search_for_words(file_name, target_word_list):
    try:
        with open(file_name,'r', encoding='utf-8') as fil:
            content = fil.read()
            sentences = content.split('.')

            found_sentences = []

            for sentence in sentences:
                for target_word in target_word_list:
                    if target_word in one_sentence:
                        found_sentences.append(one_sentence.strip())
            found_sentences = list(set(found_sentences)) #set deletes the duplicated stings in the list

            if found_sentences:
                print(f"Frases con la paabra '{target_word}' :")
                for index, sentences in enumerate(found_sentences, start=0):
                    print(f"{index}.  {sentence}\n")
            else:
                print("No hay frases con esa palabra")
    except FileNotFoundError as e:
        print("Error", e)



# obtención del contenido de un artículo de wikipedia
def get_wiki_text(titulo):

    wiki = wikipedia.search(titulo, 10, False)
    page = wikipedia.page(wiki[0])

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.writelines(page.content)
        file.close()

    #filter wiki text:

    dirty_lines = page.content.split('. ')





def chek_correct_answer(target_word, answer):
    return target_word == answer
def present_phrase_to_guess(target_word_list):

    with open('output_cleaned.txt', 'r', encoding = 'utf-8') as file:
        sentences = file.read().split(".")
        file.close()
    for line in sentences:
        for target_word in target_word_list:
            if target_word in line:
                line = line.replace(target_word, '____')
                print(line)






titulo = input('escribe el título\n')
get_wiki_text(titulo)
target_words = create_words_to_remove_list()
search_for_words('output_cleaned.txt', target_words)
present_phrase_to_guess(target_words)
