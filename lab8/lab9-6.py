import csv
from collections import Counter

def count_words(filename):

        with open(filename, 'r') as file:

            reader = csv.reader(file)
            
            for row in reader:

                word_counts = Counter(row)
                

                seen = set()
                for word in row:
                    if word not in seen:
                        print(f"{word} - {word_counts[word]}")
                        seen.add(word)

def main():
    filename = input()
    count_words(filename)

if __name__ == "__main__":
    main()