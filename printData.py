def write_into_file(path, x):
    with open(path, "ab") as f:
        f.write(str(x).encode("utf-8"))

def reset_file(path):  
    f = open(path, "w")
    f.write("")    
    f.close            

def print_file_info(path):
    f = open(path, 'r',encoding="utf-8")
    content = f.read()
    f.close()
    return(content)

reset_file("result.txt")
reset_file("percent.txt")
reset_file("match.txt")
reset_file("odds.txt")
reset_file("league.txt")

for i in range(1,6):
    matches = print_file_info(f"txtFiles/match{i}.txt").split("\n")
    results = print_file_info(f"txtFiles/result{i}.txt").split("\n")
    odds = print_file_info(f"txtFiles/odds{i}.txt").split("\n")
    percent = print_file_info(f"txtFiles/percent{i}.txt").split("\n")
    name = print_file_info(f"txtFiles/league{i}.txt").split("\n")
    for m in matches:
        print(m)
        write_into_file("match.txt", m + "\n")

    for m in results:
        print(m)
        write_into_file("result.txt",m+"\n")

    for m in odds:
        print(m)
        write_into_file("odds.txt",m+"\n")

    for m in percent:
        print(m)
        write_into_file("percent.txt",m+"\n")

    for m in name:
        print(m)
        write_into_file("league.txt",m+"\n")



# print(matches)
# print(results)
# print(odds)
# print(percent)