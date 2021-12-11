# c = ["A","B","C","D","E","F","G","H","I"]
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#
import enchant

def save():
    with open("Transpositionkey.txt", "a+") as tfile:

        for i in range(0, 18):
            for j in range(i, 19):
                for k in range(j, 20):
                    for l in range(k, 21):
                        for m in range(l, 22):
                            for n in range(m, 23):
                                for o in range(n, 24):
                                    for p in range(o, 25):
                                        for q in range(p, 26):
                                            # c = [hi, j, k, l, m, n, o, p, q]


                                                s = f"{c[j]}{c[m]}{c[o]}{c[l]}{c[n]}{c[p]}{c[i]}{c[k]}{c[q]} \n"
                                                # print(s)
                                                # print(sum((map(s.lower().count, "aeiou"))))
                                                # print(*map(s.lower().count, "aeiou"))

                                                if (sum((map(s.lower().count, "aeiou"))) >= 3) and (
                                                        sum((map(s.lower().count, "aeiou"))) < 5) and (
                                                        max((map(s.lower().count, "abcdefghijklmnopqrstuvwxyz"))) < 4):
                                                    #print(s)
                                                    tfile.write(s)
            print(s)
                                                # 1,4,6,3,5,7,0,2,8

    print("done")


def load():
    print("Loading, and analysing")
    with open("Transpositionkey.txt", "r+") as tfile:
        c = 0
        for line in tfile:
            c += 1
            x = line.rstrip("\n")
            d = enchant.Dict("en_GB")
            if d.check(x):
                print(line)
                print("FOUND SUCCESSFULLLY")
                break

            elif c % 10000 ==0:
                print(c)
        print("failed")


if __name__ == '__main__':
    load()
input()
