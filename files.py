file = open("test.txt", "r")

outfile = ""

for line in range(10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("Test2.txt", "w")
file.write(outfile)
file.close()