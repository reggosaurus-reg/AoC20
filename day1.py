data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

print("A: ")
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])
            break

print("B: ")
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
                break
