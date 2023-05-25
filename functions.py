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