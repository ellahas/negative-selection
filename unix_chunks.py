
filename = "./syscalls/snd-cert/snd-cert"
output_file = "./syscalls/snd-cert/snd-cert-chunk"
file = open(f'{filename}.train', 'r')
lines = file.readlines()
l = 7
is_test = True

chunk_file = open(f'{output_file}.train', 'w')


for line in lines:
    if '\n' in line:
        line = line[:-1]
    for i in range(len(line)-l+1):
        new_line = line[i:l*i+l]
        if len(new_line) == l:
            chunk_file.write(new_line+'\n')