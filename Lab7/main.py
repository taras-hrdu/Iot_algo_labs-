def read_data(file):
    with open(file, 'r') as input_file:
        search_string = input_file.readline()
        sub_string = input_file.readline()
    return sub_string, search_string


def find(sub_string):
    p_array = [0]*len(sub_string)
    j = 0
    i = 1

    while i < len(sub_string):
        if sub_string[j] == sub_string[i]:
            p_array[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                p_array[i] = 0
                i += 1
            else:
                j = p_array[j-1]

    return(p_array)


def kmp(sub_string, search_string=""):
    m = len(sub_string)
    n = len(search_string)
    result = []

    p_array = find(sub_string)

    i = 0
    j = 0
    while i < n:
        if search_string[i] == sub_string[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i-m)
                print("found at:", i-m)
                j = 0
        else:
            if j > 0:
                j = p_array[j-1]
            else:
                i += 1

    return result

if __name__ == '__main__':
    kmp_data = read_data("kmp.in")
    kmp_result = kmp(*kmp_data)
    print(f"{kmp_result}")
