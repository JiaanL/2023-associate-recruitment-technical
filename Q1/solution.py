N = int(input())
avaliable = input()
M = int(input())
request = input()

def sort_size(input_str):
    size = ['S', 'M', 'L']
    data_dict = {'S':[], 'M':[], 'L':[]}
    for i in input_str.split():
        for j in size:
            if j in i:
                # count X
                count = i.count('X')
                data_dict[j].append([count, i])
    for key, value in data_dict.items():
        data_dict[key] = sorted(value, key=lambda x: x[0], reverse=False)
    return_list = []
    for key in size:
        for size_i in data_dict[key]:
            return_list.append(size_i[1])
    return return_list

def check_availability(avaliable, request):
    size = {'S':0, 'M':1, 'L':2}
    avaliable = sort_size(avaliable)
    request = sort_size(request)

    # print(request, avaliable)
    j = 0
    j_data = avaliable[0]
    for i, i_data in enumerate(request):
        while size[i_data[-1]] > size[j_data[-1]]:
            j += 1
            j_data = avaliable[j]
            if j >= len(avaliable): return False
        if i_data[-1] == j_data[-1]:
            while i_data.count('X') > j_data.count('X'):
                j += 1
                j_data = avaliable[j]
                if j >= len(avaliable): return False
        
        # print(f'match: {i_data} and {j_data} ({i} - {j})')
        
        j += 1
        if j == len(avaliable) and i != len(request)-1:
            return False
        elif j == len(avaliable) and i == len(request)-1: 
            break
        j_data = avaliable[j]
    return True

if check_availability(avaliable, request):
    print('Yes')
else:
    print('No')
