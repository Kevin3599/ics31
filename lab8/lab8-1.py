def process_file(filename, lower_bound, upper_bound):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines:
                word = line.strip()
                if lower_bound <= word <= upper_bound:
                    print(f"{word} - in range")
                else:
                    print(f"{word} - not in range")
                    
    except FileNotFoundError:
        print(f"Error: Could not open {filename}")

def main():
    filename = input()
    lower_bound = input()
    upper_bound = input()
    
    process_file(filename, lower_bound, upper_bound)

if __name__ == '__main__':
    main()
