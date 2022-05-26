# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(f'{filename}.txt', 'r') as f:
        lines = f.read()
        f.close()
        print(f'\n{lines} \n')
    return lines


def count_words(name):
    text = read_file_content(name)
    # [assignment] Add your code here
    """Method 1
        disadvatage with this method is that it prints the result with the "Count" function still attached
    """
    x = Counter(text.split(" "))
    return print(x)

    """method 2
        Disadvantage with this method that i dont know how to solve is how to arrange the dictionary to be
        printed in descending order
    """
    # count = {}
    # for word in text :
    #     if word in count :
    #         count[word] += 1
    #     else:
    #         count[word] = 1
    # return print(count)

name = str(input("\nHello, what's the name of the file you want to open:  "))

read_file_content(name)
count_words(name)

