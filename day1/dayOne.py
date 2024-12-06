from collections import Counter

input = open("day1/input.txt", "r").read().split("\n")

list1 = []
list2 = []
for i in input:
    first, second = i.split("   ")
    list1.append(int(first))
    list2.append(int(second))
list1.sort()
list2.sort()

ranges = []
for each in range(len(list1)):
    ranges.append(abs(list1[each] - list2[each]))

sum = sum(ranges)
print(f"Sum of the ranges: {sum}")

similarity_score = []
test = Counter(list2)
print("Hi")
    
