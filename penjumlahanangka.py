def penjumlahan_angka(numbers, target):
    temp = list()
    for first in numbers:
        for second in numbers:
            if (first + second) == target:
                temp.extend([numbers.index(first), numbers.index(second)])
                return temp
    return []


payload = [int(x) for x in input().split()]
target = int(input())
print(penjumlahan_angka(payload, target))
