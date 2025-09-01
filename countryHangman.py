import csv
import random
#function to read
def load_countries_from_csv(filename):
    countries = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming each row has country names in the first column
            if row:  
                countries.append(row[0].strip())
    return countries

def play_game(countries):
    country = random.choice(countries).lower()  # pick random country
    guessed = set()
    wrong_guesses = 0
    max_wrong = 5

    print("Welcome to the Country Guessing Game!")
    print(f"You have {max_wrong} chances. Good luck!\n")

    while wrong_guesses < max_wrong:
        # Display word with guessed letters filled
        display_word = ''.join([letter if letter in guessed else '-' for letter in country])
        print("Current word:", display_word)

        if '-' not in display_word:
            print(" Congratulations! You guessed the country:", country.capitalize())
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed:
            print("⚠You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in country:
            wrong_guesses += 1
            print(f" Wrong guess! ({wrong_guesses}/{max_wrong}) mistakes.")

    print("Game over! The country was:", country.capitalize())


if __name__ == "__main__":
    filename = "countries.csv"  # <-- Put your CSV file name here
    countries = load_countries_from_csv(filename)

    if not countries:
        print("No countries found in the CSV file.")
    else:
        play_game(countries)
