def process_photo_names(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                photo_name = line.strip()
                if photo_name.endswith('_photo.jpg'):
                    info_name = photo_name.replace('_photo.jpg', '_info.txt')
                    print(info_name)
                    
    except FileNotFoundError:
        print(f"Error: Could not open {filename}")

def main():
    filename = input().strip()
    process_photo_names(filename)

if __name__ == '__main__':
    main()