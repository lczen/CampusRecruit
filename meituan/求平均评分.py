string = input()
string_list = string.split(" ")

a0 = int(string_list[0])
b0 = int(string_list[1])
c0 = int(string_list[2])
d0 = int(string_list[3])
e0 = int(string_list[4])

a = 1*a0
b = 2*b0
c = 3*c0
d = 4*d0
e = 5*e0
score = (a+b+c+d+e)/(a0+b0+c0+d0+e0)
str_num = str(score)
#print("%.1f" % (round(score,1)))
print(float(str_num[:str_num.index('.')+1+1]))