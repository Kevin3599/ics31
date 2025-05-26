def print_menu():
    print('\nMENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')


def get_num_of_non_WS_characters(text):
    return len([c for c in text if not c.isspace()])


def get_num_of_words(text):
    return len(text.split())


def fix_capitalization(text):
    result = ''
    capitalize_next = True
    count = 0

    for c in text:
        if capitalize_next and c.isalpha():
            result += c.upper()
            count += 1
            capitalize_next = False
        else:
            result += c
        if c in '.!?':
            capitalize_next = True

    return result, count


def replace_punctuation(text, exclamation_count=0, semicolon_count=0):
    exclamation_count = text.count('!')
    semicolon_count = text.count(';')
    new_text = text.replace('!', '.').replace(';', ',')
    print('Punctuation replaced')
    print(f'exclamation_count: {exclamation_count}')
    print(f'semicolon_count: {semicolon_count}')
    return new_text


def shorten_space(text):
    import re
    return re.sub(r'\s{2,}', ' ', text)


def execute_menu(option, text):
    if option == 'c':
        print(f'Number of non-whitespace characters: {get_num_of_non_WS_characters(text)}')
    elif option == 'w':
        print(f'Number of words: {get_num_of_words(text)}')
    elif option == 'f':
        fixed_text, count = fix_capitalization(text)
        print(f'Number of letters capitalized: {count}')
        print(f'Edited text: {fixed_text}')
        text = fixed_text
    elif option == 'r':
        text = replace_punctuation(text)
        print(f'Edited text: {text}')
    elif option == 's':
        text = shorten_space(text)
        print(f'Edited text: {text}')
    return text


if __name__ == '__main__':
    sample_text = input("Enter a sample text:\n")
    print("\nYou entered:", sample_text)

    while True:
        print_menu()
        choice = input("\nChoose an option:\n").strip().lower()
        while choice not in ['c', 'w', 'f', 'r', 's', 'q']:
            choice = input("Choose an option:\n").strip().lower()
        if choice == 'q':
            break
        sample_text = execute_menu(choice, sample_text)
