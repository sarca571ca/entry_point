"""
1. Read the target file and use file to generate a random word
2. prompt the user for a guess word - check that the word is valid
3. To check if it valid by checking the all_words file
4. Check the guess word vs the traget word and score the guess (5 chars long)
5. If no match you will give a score of 0 for that char
6. if found but not in the correct position of the word give a score of 1
7. If found in the correct position give a score of 2
8. Continue the guessing x5 iterations
9. eg. If the target word is hello and guess word is hello give '22222'
10. eg. If target word is hello and guess word is 'hemnk' then display 22000.
11. eg. If traget word is hello and guess word is lower you will get multiple hits on the 'l'
    a. Can just double that match ie 01111
    b. Better would be to count the letters and recognize that the 2nd 'l' is not a match ie 01101
"""
if __name__ == "__main__":
    print("hi")
else:
    print("Not an entrypoint")
