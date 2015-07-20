y = list()
a = 12
while a < 99:
    x = list()
    x.append(0)
    if a%10 != 0:
        x.append(a%10)
        if ((a-a%10)/10) not in x:
            x.append((a-a%10)/10)
            b = 123
            while b < 988:
                x = list()
                x.append(0)
                x.append(a%10)
                x.append((a-a%10)/10)
                if b%10 not in x:
                    x.append(b%10)
                    if (b%100-b%10)/10 not in x:
                        x.append((b%100-b%10)/10)
                        if (b%1000-b%100)/100 not in x:
                            x.append((b%1000-b%100)/100)
                            c =  a*b
                            if c < 9877:
                                if c%10 not in x:
                                    x.append(c%10)
                                    if (c%100-c%10)/10 not in x:
                                        x.append((c%100-c%10)/10)
                                        if (c%1000-c%100)/100 not in x:
                                            x.append((c%1000-c%100)/100)
                                            if (c%10000-c%1000)/1000 not in x and c not in y:
                                                y.append(c)
                b += 1
    a += 1

a = 2
while a < 5:
    b = 1234
    while b < 6543:
        x = list()
        x.append(0)
        x.append(a)
        if b%10 not in x:
            x.append(b%10)
            if (b%100-b%10)/10 not in x:
                x.append((b%100-b%10)/10)
                if (b%1000-b%100)/100 not in x:
                    x.append((b%1000-b%100)/100)
                    if (b%10000-b%1000)/1000 not in x:
                        x.append((b%10000-b%1000)/1000)
                        c = a*b
                        if c < 9877:
                            if c%10 not in x:
                                x.append(c%10)
                                if (c%100-c%10)/10 not in x:
                                    x.append((c%100-c%10)/10)
                                    if (c%1000-c%100)/100 not in x:
                                        x.append((c%1000-c%100)/100)
                                        if (c%10000-c%1000)/1000 not in x and c not in y:
                                            y.append(c)
        b += 1
    a += 1
print sum(y)
