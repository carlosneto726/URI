s = input().split()
s1 = [int(s[0]), int(s[1]), int(s[2])]
s1.sort()
s2 = [s[0], s[1], s[2]]
for c in range(0, 3):
    print(s1[c])
print(f"\n{s2[0]}\n{s2[1]}\n{s2[2]}")