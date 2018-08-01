import re

messages = {
    "replaced": "{} '{}' are replaced with '{}'.",
    "original": "The original content was:\n{}",
    "changed": "The changed content is:\n{}",
    }

def read_file(filename):
    fin = open(filename, 'rt')
    contents = fin.read()
    fin.close()
    return contents

def count_word(word, source):
    word_list = re.findall('\W{}\W'.format(word), source, re.IGNORECASE)
    return len(word_list)

def replace_word(word1, word2, source):
    new_content = re.sub(word1, word2, source, re.IGNORECASE)
    return new_content

def write_file(source, filename):
    fout = open(filename, 'wt')
    fout.write(source)
    fout.close()

content = read_file('45.txt')
number_of_word = count_word('utilize', content)
new_content = replace_word('utilize', 'use', content)
write_file(new_content, '45-1.txt')

print(messages["original"].format(content))
print(messages["changed"].format(read_file('45-1.txt')))
print(messages["replaced"].format(number_of_word, 'utilize', 'use'))