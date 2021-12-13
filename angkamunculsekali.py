payload = input()
output = list()
for e in set(payload):
    if list(payload).count(e) == 1:
        output.append(e)
print(sorted(output, reverse=True))
