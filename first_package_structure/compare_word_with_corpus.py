import os
import pickle
from collections import Counter
from operator import itemgetter

from first_package_structure import create_words_and_values


def compare_directory(words_in, directoryIn):
    """
    
    :param words_in: The list of words to check 
    :param directoryIn: The directory holding the corpus of information
    :return: A tuple of (word, calculated_value) in descending order
    """

    fileshan=[]
    for root, dirs, files in os.walk(directoryIn):
            for file in files:
                if file.endswith(".txt"):
                    l=os.path.join(root,file)
                    fileshan.append(l)

    sorted_values, file_values=compare_file_list(words_in, fileshan)

    return sorted_values


def compare_single_file(words_in, file_in):
    """
    
    :param words_in: The words to compare
    :param file_in: The file to compare
    :return: A list of words and associated values for that file
    """
    results = create_words_and_values(file_in)

    s = sum(results.values())

    overall_value = {}
    for word in words_in:
        k = 100 * results.get(word, 0) / s
        overall_value[word] = overall_value.get(word, 0.0) + k
    return Counter(overall_value)


def compare_file_list(words_in, files_in):
    """
    
    :param words_in: words to compare
    :param files_in: A list of files to compare
    :return: A tuple of word, value and the values for each file as a dict, dict key is the filename, and each entry is a sorted tuple of word, value
    """
    overall_value = Counter({})
    file_values ={}

    for file in files_in:
            values_out=compare_single_file(words_in,file)
            overall_value=overall_value+values_out
            file_values[file] =sorted(values_out.items(), key=itemgetter(1), reverse=True)

    for word in words_in:
        overall_value[word] = overall_value.get(word, 0.0)/len(files_in)

    sorted_values = sorted(overall_value.items(),key=itemgetter(1), reverse=True)
    return sorted_values, file_values


def get_sorted_key_words(file_in):
    """
    Simple subroutine to read in the data
    :param file_in: file to read data from
    :return: a list of sorted words
    """
    x = pickle.load(open(file_in, 'rb'))
    sorted_x = sorted(x.items(), key=itemgetter(1), reverse=True)

    sorted_words = list(map(itemgetter(0), sorted_x))
    return sorted_words

def get_top_values(file_in, n):
    """
    Get the top n values
    :param file_in: file to read values from
    :param n: number of values to get 
    :return: a list of size n holding the top n words in the dataset 
    """

    sorted_words = get_sorted_key_words(file_in)

    return sorted_words[0:n]


def main():

   # file_in = input("Please input the file to load the dataset from")
    file_in='test.pickle'
   # number = eval(input("Please input the number of words to use"))
    number = 5

    values = get_top_values(file_in, number)

    files = ['script.txt','transcript_1.txt', 'transcript_2.txt', 'transcript_3.txt']

    val , file_val= compare_file_list(values, files)
    for file in files:
        print(file,file_val.get(file))
    print(val)

    print(val)

    val2 =compare_directory(values, ".")
    print(val2)

if __name__ == "__main__":
    main()
