import hashlib

target = "c09145ad46b058fba82e4218169c7121"

for i in range(1000):
    passw = str(i)
    passw_hash = hashlib.new("md5", passw).hexdigest()

    if passw_hash == target:
        print(f"Password matched!!, the password is: {passw}")

    else:
        print("password is not in the range of 0-999")