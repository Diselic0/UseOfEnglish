import re
import utility
import myOpenAi

myOpenAi.init_openchat()

titulo = input('escribe el título\n')
utility.get_wiki_text(titulo)

target_words = utility.create_words_to_remove_list()
found_sentences = utility.search_for_words('output_cleaned.txt', target_words)
utility.present_guess_repeat_routine(target_words,found_sentences)




'''if __name__ == "__main__":
    main()'''