from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Several quotes")
    print("4. Add quote")
    print("5. Exit")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-4): ")
        
        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)

        elif choice == "3":
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
            
        elif choice == "4":
            add_quote(quotes,"quotes.txt")
        elif choice == "5":
            print("Good bye...")
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()