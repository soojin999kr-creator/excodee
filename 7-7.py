scores = {
    "Kim": [80, 90, 70],
    "Lee": [100, 90, 85],
    "Park": [95, 85, 100]
}

averages = {}
names = []

for name, score_list in scores.items():
    avg = sum(score_list) / len(score_list)
    averages[name] = avg
    if avg >= 90:
        names.append(name)

print("averages:", averages)
print("names (>=90):", names)
