def process_food_file(filename):
    try:
        with open(filename, 'r') as file:

            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) == 4:
                    category, name, description, availability = parts
                    if availability == 'Available':
                        print(f"{name} ({category}) -- {description}")
                        
    except FileNotFoundError:
        print(f"Error: Could not open {filename}")

def main():
    filename = input()
    process_food_file(filename)

if __name__ == '__main__':
    main()