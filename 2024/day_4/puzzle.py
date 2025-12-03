
pattern = 'XMAS'
input = []
ptrn_cnt = 0

with open('./input.txt', 'r') as f:
    for line in f:
        input.append(line.replace('\n', ''))

# Row counter
def row_counter(input, ptrn_cnt):
    for row in input:
        temp_word = ''
        for char in row:
            temp_word += char
            if pattern in temp_word:
                ptrn_cnt += 1
                temp_word = ''
        temp_word = ''
        for char in row[::-1]:
            temp_word += char
            if pattern in temp_word:
                ptrn_cnt += 1
                temp_word = ''
    return ptrn_cnt

# Column counter
def column_counter(input, ptrn_cnt):
    columns = []
    for row in input:
        for index, char in enumerate(row):
            try:
                columns[index] += char
            except IndexError:
                columns.append(char)
    ptrn_cnt = row_counter(columns, ptrn_cnt)
    return ptrn_cnt

# Diaganol counter
def diag_counter(input, ptrn_cnt):
    diags = [[], []]
    for row in input:
        for char in row:
            pass

    return ptrn_cnt


row_cnt = row_counter(input, ptrn_cnt)
print('row count:', row_cnt)
col_cnt = column_counter(input, ptrn_cnt)
print('col count:', col_cnt)

print('total count:', row_cnt+col_cnt )