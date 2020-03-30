def lenLWord(s : str):
    s = s.strip()
    s = s.split(" ")
    print(len(s[-1]))
lenLWord("Hello Wor ")