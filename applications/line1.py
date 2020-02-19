file = open("teams.txt","r")
outfile = ""
for line in range(5):
    if line == 0:
        file.readline()
        outfile += "This is a new line \n"
    outfile += file.readline()

file.close()

file = open("teamsedit", "w")
file.write(outfile)






