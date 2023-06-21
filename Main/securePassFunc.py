import random, requests
def securePass():
    wordlist = requests.get("https://www.mit.edu/~ecprice/wordlist.10000").text.splitlines()
    wordpass = random.choice(wordlist)

    substitutions = {'a': '@', 'e': '3', 'I': '1', 'S': '$', 'O': '0'}

    rawpass = []
    for char in wordpass:
        if char in substitutions:
            rawpass.append(substitutions[char])
        else:
            rawpass.append(char)

    while len(rawpass) < 12:
        char = chr(random.randint(48, 122))
        rawpass.append(substitutions.get(char, char))

    return "".join(rawpass[:12])