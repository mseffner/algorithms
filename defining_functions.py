# This program attempts to produce a short target sentence by randomly generating strings
# and checking them against the target. Time required is 27^n

import random
import string


LETTERS = string.ascii_lowercase + " "


def main():
    target = "methinks it is like a weasel"
    best = ""
    best_score = 0
    target_length = len(target)
    for i in range(500000):
        attempt = random_string(size=target_length)
        score = score_string(attempt, target)
        if score > best_score:
            best_score, best = score, attempt
            print(best, best_score)


def score_string(attempt, target):
    """Returns the number of matching chars between attempt and target"""
    return sum([1 for a, b in zip(attempt, target) if a == b])


def random_string(size):
    """Returns a randomly generated string of length size"""
    slist = []
    for _ in range(size):
        r = random.randint(0, 26)
        slist.append(LETTERS[r])
    return "".join(slist)


if __name__ == "__main__":
    main()