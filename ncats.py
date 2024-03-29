### Practice

# **You have 100 cats.**

# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.

# Optional: Make function that can calculate hat with any amount of rounds and cats.

# Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt. 

print('Enter circles: ')
circles = int(input())
print('Enter cats: ')
cats = int(input())

def ncats(circles: int, cats: int) -> list:
    step = 1
    cats = [False] * (cats + 1)

    for circle in range(0, circles):
        for idx in range(0, len(cats), step):
            if idx != 0:
                cats[idx] = not cats[idx]
        step += 1
    
    return cats

def takeIdxs(source: list) -> list:
    idxs = []

    for cat in range(0, len(source)):
        if source[cat] is True:
            idxs.append(cat)

    return idxs

print(takeIdxs(ncats(circles, cats)))
