synonyms = {} 
word = input()
letter = input() 
filename = word + ".txt"  

try:
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            if words: 
                
                first_letter = words[0][0]
                if first_letter not in synonyms:
                    synonyms[first_letter] = []
                synonyms[first_letter].extend(words)

    if letter in synonyms:
        for synonym in synonyms[letter]:
            print(synonym)
    else:
        print(f"No synonyms for {word} begin with {letter}")
            
except FileNotFoundError:
    print(f"Error: Could not find file {filename}")
