f = open("bill.txt", "r")
fw = open("bill.txt.bak", "a")

for line in f:
    line = line.strip()
    if line.split(",")[4] == "test":
        continue
    fw.write(line)
    fw.write("\n")

f.close()
fw.close()