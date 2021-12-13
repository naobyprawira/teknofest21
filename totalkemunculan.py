import collections

List = list(map(str, input().split()))


def TotalKemunculan(List):
    counting = collections.Counter(List)
    sorted_dict = {}
    sorted_keys = sorted(counting, key=counting.get)
    for w in sorted_keys:
        sorted_dict[w] = counting[w]
    return sorted_dict


dipisah = TotalKemunculan(List)
for i in dipisah:
    print(i, ":", dipisah[i])
