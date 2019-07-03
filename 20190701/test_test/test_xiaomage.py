for i in range(1, 10):
    s = ""
    for j in range(1, 10):
        if i >= j:
            s += str(j) + "*" + str(i) + "=" + str(i*j) + " "
    print(s)