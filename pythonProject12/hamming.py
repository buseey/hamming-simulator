# hamming.py

def calculate_hamming_code(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    hamming = ['0'] * (m + r + 1)

    j = 0
    for i in range(1, len(hamming)):
        if (i & (i - 1)) != 0:
            hamming[i] = data_bits[j]
            j += 1

    for i in range(r):
        parity = 0
        for j in range(1, len(hamming)):
            if j & (2 ** i):
                parity ^= int(hamming[j])
        hamming[2 ** i] = str(parity)

    return ''.join(hamming[1:])  # remove dummy 0th index


def introduce_error(code, index=None):
    if index is None:
        import random
        index = random.randint(0, len(code) - 1)

    error_bit = '1' if code[index] == '0' else '0'
    corrupted = code[:index] + error_bit + code[index+1:]
    return corrupted, index


def detect_and_correct(code):
    n = len(code)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1

    code = '0' + code  # 1-based index
    syndrome = 0

    for i in range(r):
        parity = 0
        for j in range(1, n + 1):
            if j & (2 ** i):
                parity ^= int(code[j])
        if parity != 0:
            syndrome += 2 ** i

    if syndrome != 0:
        corrected = list(code)
        corrected[syndrome] = '1' if corrected[syndrome] == '0' else '0'
        return ''.join(corrected[1:]), syndrome - 1
    else:
        return code[1:], -1
