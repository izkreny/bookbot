def number_of_words_in(text):
    words = text.split()

    return len(words)

def characters_occurrence_in(text):
    character_occurrence = {}
    lowered_text_without_newlines_and_BOM = text.replace('\n', '').replace('\ufeff', '').lower()
    
    for character in lowered_text_without_newlines_and_BOM:
        if character in character_occurrence:
            character_occurrence[character] += 1
        else:
            character_occurrence[character] = 1

    return character_occurrence

def sort_characters_occurrence_descending(dictionary):
    sorted_characters = []
    def sort_on(items):
        return items["num"]

    for character in dictionary:
        sorted_characters.append({"char": character, "num": dictionary[character]})

    sorted_characters.sort(reverse=True, key=sort_on)
    
    return sorted_characters
