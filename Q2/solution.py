n = int(input())
input_data = []
for i in range(n):
    tmp_input = input()
    input_data.append(tmp_input)


allValid = True
erorCodes = []
for i in input_data:
    tmp_data = i.split()
    if tmp_data[1] == 'false':
        allValid = False
        erorCodes.append(tmp_data[2])

if allValid:
    print('Yes')
else:
    print('No')
    print(' '.join(erorCodes))
