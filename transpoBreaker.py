from collections import Counter

primeFactor = {
    "a":2,
    "b":3,
    "c":5,
    "d":7,
    "e":11,
    "f":13,
    "g":17,
    "h":19,
    "i":23,
    "j":29,
    "k":31,
    "l":37,
    "m":41,
    "n":43,
    "o":47,
    "p":53,
    "q":59,
    "r":61,
    "s":67,
    "t":71,
    "u":73,
    "v":79,
    "w":83,
    "x":89,
    "y":97,
    "z":101
}
letterFrequencies = {
    "a":0.0812,
    "b":0.0149,
    "c":0.0271,
    "d":0.0432,
    "e":0.1202,
    "f":0.0230,
    "g":0.0203,
    "h":0.0592,
    "i":0.0731,
    "j":0.0010,
    "k":0.0069,
    "l":0.0398,
    "m":0.0261,
    "n":0.0695,
    "o":0.0768,
    "p":0.0182,
    "q":0.0011,
    "r":0.0602,
    "s":0.0628,
    "t":0.0910,
    "u":0.0288,
    "v":0.0111,
    "w":0.0209,
    "x":0.0017,
    "y":0.0211,
    "z":0.0070
}
pairFrequencies = {
    "th":0.0388,
    "he":0.0368,
    "in":0.0228,
    "er":0.0217,
    "an":0.0214,
    "re":0.0174,
    "nd":0.0157,
    "on":0.0141,
    "en":0.0138,
    "at":0.0133,
    "ou":0.0128,
    "ed":0.0127,
    "ha":0.0127,
    "to":0.0116,
    "or":0.0115,
    "it":0.0113,
    "is":0.0110,
    "hi":0.0109,
    "es":0.0109,
    "ng":0.0105
}

class transpoBreaker(object):

    # constructor
    def __init__(self):
        pass

    # determine if input is a transposition
    def isTranspo(input):
        # calculate the frequency of each letter in the cipher text
        letterFrequency = Counter(input)
        # total number of letters in the cipher text
        totalLetters = sum(letterFrequency.values())
        # calculate the frequency of each letter as a percentage of the total letters
        for letter in letterFrequency:
            letterFrequency[letter] = letterFrequency[letter] / totalLetters
        # compare the letter frequency in the ciphertext with the expected English frequency distribution
        deviationCounter = 0
        expected = 0.000
        observed = 0.000
        for letter in letterFrequencies:
            # print(f"{letter}: expected frequency: {letterFrequencies[letter]*100:.2f}%, observed frequency: {letterFrequency[letter]*100:.2f}%")
            expected = letterFrequencies[letter]*100
            observed = letterFrequency[letter]*100
            if ((observed != 0.00) and ((observed - expected) > 2)):
                deviationCounter += 1
        # print(f"Accuracy Counter: {deviationCounter}")
        if (deviationCounter > 5):
            return False
        else:
            return True

    # attack an anagram
    def attackAnagram(input):
        # load the dictionary
        with open("dictionary.txt") as read:
            wordDictionary = read.readlines()
        i = 0
        # clean up the dictionary with new lines
        for x in wordDictionary:
            wordDictionary[i] = wordDictionary[i].rstrip("\n")
            i += 1
        # brute force the anagram
        results = []
        for w in wordDictionary:
            if (sorted(w) == sorted(input)):
                results.append(w)
        # return the resulting anagram(s)
        return results

    # attack a columnar
    def attackColumnar(input):
        pass
