alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter a message\n").upper()
str_out = ""

n = len(str_in)

for i in range (n):
    c = str_in[i]
    loc = alpha.find(c)
    print (i, c, loc)
    new_loc = (loc + 3)%26
    str_out += alpha[new_loc]
    print (new_loc, str_out)

print ("Obfuscated Version: ", str_out)
