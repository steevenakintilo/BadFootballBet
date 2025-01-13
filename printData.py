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


matches = print_file_info("match.txt").split("\n")
matches = sorted(matches)
results = print_file_info("result.txt").split("\n")
results = sorted(results)
odds = print_file_info("odds.txt").split("\n")
odds = sorted(odds)
percent = print_file_info("percent.txt").split("\n")
percent = sorted(percent)
name = print_file_info("league.txt").split("\n")
name = sorted(name)

reset_file("result.txt")
reset_file("percent.txt")
reset_file("match.txt")
reset_file("odds.txt")
reset_file("league.txt")

for m in matches:
    if len(m) > 1 and " " in m:
        m = m.split(" ",1)
        print(m[1])
        write_into_file("match.txt", m[1] + "\n")

for m in results:
    if len(m) > 1 and " " in m:
        m = m.split(" ",1)
        print(m[1])
        write_into_file("result.txt",m[1]+"\n")

for m in odds:
    if len(m) > 1 and " " in m:
        m = m.split(" ",1)
        print(m[1])
        write_into_file("odds.txt",m[1]+"\n")

for m in percent:
    if len(m) > 1 and " " in m:
        m = m.split(" ",1)
        print(m[1])
        write_into_file("percent.txt",m[1]+"\n")

for m in name:
    if len(m) > 1 and " " in m:
        m = m.split(" ",1)
        print(m[1])
        write_into_file("league.txt",m[1]+"\n")



# print(matches)
# print(results)
# print(odds)
# print(percent)