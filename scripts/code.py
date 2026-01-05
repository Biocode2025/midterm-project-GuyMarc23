f = open("data/extreme_organism_proteins.txt", "r")
lines = f.readlines()
f.close()

names = []
sequences = []
seq = ""
name = ""

for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line[0] == ">":
        if seq != "":
            sequences.append(seq)
            seq = ""
        if "OS=" in line:
            os_index = line.find("OS=") + 3
            rest = line[os_index:]
            end_index = len(rest)
            for marker in [" GN=", " PE=", " SV="]:
                idx = rest.find(marker)
                if idx != -1:
                    end_index = min(end_index, idx)
            name = rest[:end_index].strip()
        else:
            name = line[1:].strip()
        names.append(name)
    else:
        seq = seq + line

if seq != "":
    sequences.append(seq)

amino_acids = "ACDEFGHIKLMNPQRSTVWY"


out = open("results/amino_acid_results.txt", "w")

i = 0
while i < len(names):
    s = sequences[i]
    total = len(s)
    out.write("Organism: " + names[i] + "\n")
    j = 0
    while j < len(amino_acids):
        aa = amino_acids[j]
        count = s.count(aa)
        percent = (count / total) * 100
        out.write(aa + ": " + "%.2f" % percent + "%\n")
        j = j + 1
    out.write("\n")
    i = i + 1

out.close()