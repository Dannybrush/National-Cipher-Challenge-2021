import enchant

with open("Tester.txt", "r+") as tfile:
    for line in tfile:
        x = line.rstrip("\n")
        d = enchant.Dict("en_GB")

        print(d.check(x))
        print(line)
        if d.check(x):
            print(line)
            print("Found")
        else:
            print(d.suggest(line))
    print("failed")
