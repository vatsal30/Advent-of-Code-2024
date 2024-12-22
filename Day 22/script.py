'''
- Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
- Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
- Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

- To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
- To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
'''
from itertools import product
from collections import defaultdict

def mix_and_prune(secret, value):
    secret ^= value
    secret %= 16777216
    return secret

def part_1():
    ans = 0
    for num in data:
        for _ in range(2000):
            num = mix_and_prune(num, num * 64)
            num = mix_and_prune(num, num // 32)
            num = mix_and_prune(num, num * 2048)
        ans += num
    return ans

def gen_secrets(secret):
    secrets = []
    for _ in range(2000):
        secret = mix_and_prune(secret, secret * 64)
        secret = mix_and_prune(secret, secret // 32)
        secret = mix_and_prune(secret, secret * 2048)
        secrets.append(secret)
    return secrets

def part_2():
    results = []
    for secret in data:
        secrets = gen_secrets(secret)
        prices = list(map(lambda secret: secret % 10, secrets))
        changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        results.append((prices, changes))
    
    max_bananas = 0
    best_seq= None
    banana_seq = defaultdict(int)
    for prices, changes in results:
        seen_sequences = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i + 4])
            if seq in seen_sequences:
                continue
            seen_sequences.add(seq)
            banana_seq[seq] += prices[i + 4]

    for seq, bananas in banana_seq.items():
        if bananas > max_bananas:
            max_bananas = bananas
            best_seq = seq
    return max_bananas, best_seq

data = []
with open('./inputs.txt', 'r') as f:
    for line in f:
        data.append(int(line.strip()))
print(data)
print(part_1())
print(part_2())