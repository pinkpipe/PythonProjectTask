const_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы

str_ = 'Day, mice. "Year" is a mistake!'
list_ = []
list_symbols = ['.', '"', ',', '!']

sum_ = ''
list_.extend(str_.split())

count = 0
for i in list_:
    count_al = 0
    for k in i:
        if k.isalpha():
            count_al += 1
    for j in i:

        if j.isupper():
            find_ = const_upper_en.find(j)
            if (find_ + count_al) >= len(const_lower_en):
                sum_ += const_upper_en[abs(len(const_lower_en) - (find_ + count_al))]
            else:
                sum_ += const_upper_en[find_ + count_al]
            count += 1
        elif j.islower():
            find_ = const_lower_en.find(j)
            if (find_ + count_al) >= len(const_lower_en):
                sum_ += const_lower_en[abs(len(const_lower_en) - (find_ + count_al))]
            else:
                sum_ += const_lower_en[find_ + count_al]
            count += 1
        elif j in list_symbols:
            sum_ += j
    if count == count_al:
        sum_ += ' '
        count = 0

print(sum_)

# list_2 = []
# sum_2 = ''
#
# for i in list_:
#     for j in i:
#         len_ = len(i)
#         if j.isupper():
#             find_ = const_upper_en.find(j)
#             if (find_ + len_) >= len(const_lower_en):
#                 sum_2 += const_upper_en[abs(len(const_lower_en) - (find_ + len_))]
#             else:
#                 sum_2 += const_upper_en[find_ + len_]
#         elif j.islower():
#             find_ = const_lower_en.find(j)
#             if (find_ + len_) >= len(const_lower_en):
#                 sum_2 += const_lower_en[abs(len(const_lower_en) - (find_ + len_))]
#             else:
#                 sum_2 += const_lower_en[find_ + len_]




