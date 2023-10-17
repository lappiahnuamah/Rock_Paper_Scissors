rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]
import string
# def check_line(line):
#     rude_count = 0
#     words = line.lower().split(" ")
#     for word in words:
#         for rude in rude_words:
#             if rude in word:
#                 rude_count += 1
#                 print(f"Found rude word: {word}")
#     return rude_count
def bleeper(word):
    pos = 0 
    for character in word:
        if character not in string.punctuation:
            character = "*"
        word = word.replace(word[pos], character) 
        pos += 1
    return word


def check_line(line):
    rude_count = 0

    #We'll need the position of the current word in the list
    word_index = 0
    words = line.lower().split(" ")
    for word in words:
        stripped_word = word.strip(string.punctuation)
        if  stripped_word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")

            #Find the current word in the words list and replace it 
            #with a bleeped version. Notice we use word rather than 
            #stripped_word, in order to keep the puctuation. 
            words[word_index] = bleeper(word)
        word_index += 1 #Moving to the next word
    line = " ".join(words)
    #We will now return both the count and the line itself, 
    #so we can write the line to the file
    return line, rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0

        #If the file has multiple lines, we will need
        #to collect them all for the final output
        lines = []

        for line in myfile:
            # Get the (potentially bleeped) line and 
            # the number of rude words in that line
            line, rude_subtotal = check_line(line)
            #Add to the total rude  lines found in the file
            rude_count += rude_subtotal

            #Add the current line tot he lines list
            lines.append(line)
        

    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")
    else:
        # If rude words were found, write them to a new file
        # # and inform the user.
        with open("bleeped_copy.txt", "w") as bleeped_copy:
            bleeped_copy.write("\n".join(lines))
        print(f"Found {rude_count} rude words in your file. See bleeped_copy.txt for a censored copy of your file.")


if __name__ == '__main__':
    check_file("my_other_story.txt")