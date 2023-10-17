import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    # We'll append strings into this list for output.
    output = []
    template = random.choice(templates)
    noun = random.choice(nouns)
    verb = random.choice (verbs)
    index = 0
    while index < len(template):
        if template[index:index+8] == "{{noun}}":
            output.append(noun)
            index+=8
        elif template[index:index+8] == "{{verb}}":
            output.append(verb)
            index+=8
        else:
            output.append(template[index])
            index+=1
    return "".join(output)

# To see the results, we need to call the funtion and print what it returns:
print(silly_string(words.nouns, words.verbs,
        words.templates))
