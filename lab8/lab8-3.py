def movie_info(filename):
    try:
        with open(filename, 'r') as file:
            current_title = ""
            current_rating = ""
            times = []
            
            for line in file:

                showtime, title, rating = line.strip().split(',')

                if title != current_title and current_title:

                    display_title = current_title[:44]

                    print(f'{display_title:<44} |{current_rating:>6} | {" ".join(times)}')
                    times = []

                current_title = title
                current_rating = rating
                times.append(showtime)
    
            if current_title:
                display_title = current_title[:44]
                print(f'{display_title:<44} |{current_rating:>6} | {" ".join(times)}')
                    
    except FileNotFoundError:
        print(f"Error: Could not open {filename}")

def main():
    filename = input().strip()
    movie_info(filename)

if __name__ == '__main__':
    main()