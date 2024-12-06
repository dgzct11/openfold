import os

alignments_dir = "../../alignments_dir/"

lengths = []
for dir in os.listdir(alignments_dir):
    if os.path.isdir(alignments_dir + dir):
        for file in os.listdir(alignments_dir + dir):
            if file == "msa.sh" or file == "out.tar.gz" or file == "pdb70.m8":
                #delete it
                os.remove(alignments_dir + dir + "/" + file)
            elif file == "uniref.a3m":
                with open(alignments_dir + dir + "/" + file, "r") as f:
                    lines = f.readlines()
                with open(alignments_dir + dir + "/" + file, "w") as f:
                    #rewrite all lines except the last one
                    f.writelines(lines[:-1])
                    lengths.append(len(lines))
            
#display statistics about the lengths of the files, including average, min, max, and standard deviation
print("Average length: " + str(sum(lengths) / len(lengths)))
print("Min length: " + str(min(lengths)))
print("Max length: " + str(max(lengths)))


