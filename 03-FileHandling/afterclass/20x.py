file_r = open('../students.txt', 'r')
for line in file_r:
    if int(line)%2==0:
        file_w.write(f"{line}")
file_r.close()