fin = open("list_eval_partition.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
    fout.write(line.replace('media', '/media'))

fin.close()
fout.close()