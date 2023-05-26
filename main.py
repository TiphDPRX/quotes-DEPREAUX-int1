from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("random : Random quote")
    print("display : Display quotes")
    print("add : Add a new quote")
    print("all : Display all quotes")
    print("exit : Exit the program")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input(">> ")
        
        if choice == "random":
            print_quote(random_quote(quotes))
        elif choice == "display":
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
        elif choice == "add":
            add_quote(quotes, "quotes.txt")
        elif choice == "all":
            view_quotes(quotes)
        elif choice == "exit":
            print("Good bye...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()