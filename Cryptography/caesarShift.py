alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter a message\n").upper()
shift = int(input("How much you want to shift the value\n"))

str_out = ""

n = len(str_in)

for i in range (n):
    c = str_in[i]
    loc = alpha.find(c)
    new_loc = (loc + shift)%26
    str_out += alpha[new_loc]

print("Obfuscated Version: ", str_out)