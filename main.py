import random
import string

path = r"words.txt"
used_words = []

def check(word : str,letter: str,used_words: list[str]) -> bool:
    """
    Args:
        word (str): word to check
        letter (str): letter from which the word should start
        used_words (list[str]): words used by the player and ai

    Returns:
        bool: True if the word is valid, False otherwise
    """

    if word in used_words:
        return False
    if word[0] != letter:
        return False
    if word.isalpha():
        if " " in word:
            return False
        for p in string.punctuation:
            if p in word:
                return False
        for n in string.digits:
            if n in word:
                return False
        return True
    else:
        return False

def main():

    global letter

    print("Welcome to the word game!")
    print("Enter a word that starts with the last letter of the previous word")
    print("Enter 'q' to quit")

    letter = "a"

    while (inp:=input("Enter a word: ").lower()) != "q":

        if check(inp,letter,used_words):

            used_words.append(inp)
            letter = inp[-1]

            with open(path, "r") as f:

                l = [i.strip('\n') for i in f.readlines()]

                words = [w for w in l if (check(w,letter,used_words))]

                if len(words) > 0:
                    word = random.choice(words)
                    print(word)
                    letter = word[-1]
                    used_words.append(word)
                else:
                    print("No more words")
                    print("You win!")
                    break
        else:
            print("Enter another word.")
            continue

    if inp.lower() == "q":
        print("AI won")

if __name__ == "__main__":
    main()