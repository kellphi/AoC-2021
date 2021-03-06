
with open(r'D:\Users\Philip\OneDrive\Documents\AoC 2021\Inputs\Day2.txt') as f:
    data = f.read()

data = data.splitlines()

hor = 0
depth1 = 0
depth2 = 0
aim = 0

for i in data:

    cmd,amt = i.split(" ")
    amt = int(amt)

    if cmd == "forward":
        hor += amt
        depth2 += amt*aim

    if cmd == "down":
        depth1 += amt
        aim += amt

    if cmd == "up":
        depth1 -= amt
        aim -= amt

answer1 = hor*depth1
answer2 = hor*depth2

print("Part 1:", answer1)
print("Part 2:", answer2)
