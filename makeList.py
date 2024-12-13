abz = """


"""


abz = abz.split("\n")
idx = 0
for ab in abz:
    if idx % 4 == 0 and idx > 0:
        print(ab)
    idx+=1