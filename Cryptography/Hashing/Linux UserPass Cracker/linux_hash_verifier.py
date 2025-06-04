import crypt

target_hash = "$y$j9T$l5JDJNoc/Zw5j4W2zJFii/$V8tmryUgvUMS2D64yOge7Tg56B2vTyEtvRCmDaex9nC"

wordlist_path = "wordlists/rockyou.txt"

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        password = line.strip()
        if not password:
            continue

        hashed = crypt.crypt(password, target_hash)

        if hashed == target_hash:
            print(f"[+] Password matched with: {password}")
            break
    else:
        print("[-] Password not found in wordlist.")