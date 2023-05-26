import random

def load_quotes(filename):
    quotes = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            quotes.append(line)
    return quotes

def random_quote(quotes):
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print(quote)

def view_quotes(quotes):
    for quote in quotes:
        print_quote(quote)

def display_quotes(quotes, count):
    if count >= len(quotes):
        print("All Quotes:")
        view_quotes(quotes)
    else:
        print(f"First {count} Quotes:")
        for i in range(count):
            print_quote(quotes[i])


def add_quote(quotes, filename):
    new_quote = input("Enter a new quote: ")
    quotes.append(new_quote)
    
    with open(filename, 'a') as file:
        file.write("\n"+new_quote)


