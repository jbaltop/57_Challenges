messages = {
    "total": "Total of {} names",
    }

def file_to_list(filename):
    fin = open(filename, 'rt')
    names = fin.readlines()
    fin.close()
    return names

def order_name(names):
    return names.sort()

def list_to_file(names):
    fout = open('41-1.txt', 'wt')
    print('\n' + messages["total"].format(len(names)))
    print('-'*17)
    for name in names:
        print(name, file=fout, end='')
    fout.close()

def read_file(filename):
    content = ''
    fin = open(filename, 'rt')
    for line in fin:
        content += line
    fin.close()
    return content

names = file_to_list('41.txt')
order_name(names)
list_to_file(names)

print(read_file('41-1.txt'))
