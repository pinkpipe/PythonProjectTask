# Надо написать таблицу умножения, на вход программы подается 4 числа (a, b, c,d)
# Программа должна вывести таблицу умножения, где все числа в отрезке от a до b
# умножаются на числа от c до b.

# Пример: 7 10 5 6
# 	  5	    6
# 7   35	42
# 8	  40	48
# 9	  45	54
# 10  50	60

a, b, c, d = map(int, input().split())
n=0
if (a, b, c, d < 10) or (a <= b) or (c <= d):
    print("", end="\t")
    for i in range(c, d+1):
        print(i, end="\t")
    print("")
    for j in range(a,b+1):
        print(j, end="\t")
        for i in range(c,d+1):
            print(j*i, end="\t")
        print("")

#___________

