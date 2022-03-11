import matplotlib.pyplot as plt
import numpy as np
import hashlib
import random
import string
import hmac

e = 2**52
#salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
salt = "0xf22bacd2045342de47fcaf1532fcfe8d591fe5293b68e098d715c0daa1bd715e"


def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()

game_hash = '0bc6237df0bffc62bee4949e483012deead3bb9dd2f64cee2b994f224c47ff93' # Update to latest game's hash for more results
#first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"
first_game = "a0c7b0e5f6dc711923f5cd38fb137dd8ff8bf774a4a5dbecd8361cb0fe03d79d"

results = []
count = 0
while game_hash != first_game:
    count += 1
    results.append(get_result(game_hash))
    game_hash = get_prev_game(game_hash)

results.reverse()

print(count)
print(results[0])
print(results[1])

with open("generated.csv","w") as f:
     f.write("\n".join(str(x) for x in results))
