def win(hand):
    unit = 0
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        unit = 1
    value = {}
    for i in range(0,5):
        if hand[i][0] == 'T':
            value[10] = value.get(10,0)+1
        elif hand[i][0] == 'J':
            value[11] = value.get(11,0)+1
        elif hand[i][0] == 'Q':
            value[12] = value.get(12,0)+1
        elif hand[i][0] == 'K':
            value[13] = value.get(13,0)+1
        elif hand[i][0] == 'A':
            value[14] = value.get(14,0)+1              
        else:
            value[int(hand[i][0])] = value.get(int(hand[i][0]),0)+1       
    value = sorted(value.iteritems(),key=lambda d:(d[1],d[0]),reverse=True)
    if value[0][1] == 4:
        p = 8
    elif value[0][1] == 3 and value[1][1] == 2:
        p = 7
    elif value[0][1] == 3 and value[1][1] == 1:
        p = 4
    elif value[0][1] == 2 and value[1][1] == 2:
        p = 3
    elif value[0][1] == 2 and value[1][1] == 1:
        p = 2
    else:
        if value[0][0]-1 == value[1][0] and value[1][0]-1 == value[2][0] and value[2][0]-1 == value[3][0] and value[3][0]-1 == value[4][0]:
            if unit == 1:
                p = 9
            else:
                p = 5
        else:
            if unit == 1:
                p = 6
            else:
                p = 1
    if len(value) < 4:
        result = [p]
        for i in range(0,len(value)):
            result.append(value[i][0])
        for j in range(0,4-len(value)):
            result.append(0)
    else:
        result = [p, value[0][0], value[1][0], value[2][0], value[3][0]]
    return result

input_file = open('poker.txt')
count = 0
for line in input_file:
    words = line.rstrip().split()
    player1 = [words[0],words[1],words[2],words[3],words[4]]
    player2 = [words[5],words[6],words[7],words[8],words[9]]
    if win(player1)[0] > win(player2)[0]:
        count += 1 
    elif win(player1)[0] == win(player2)[0]:
        if win(player1)[1] > win(player2)[1]:
            count += 1
        elif win(player1)[1] == win(player2)[1]:
            if win(player1)[2] > win(player2)[2]:
                count += 1
            elif win(player1)[2] == win(player2)[2]:
                if win(player1)[3] > win(player2)[3]:
                    count += 1
                elif win(player1)[3] == win(player2)[3]:
                    if win(player1)[4] > win(player2)[4]:
                        count += 1
print count


#test = ['KC', 'QS', 'KH', 'JD', 'JC']        
#print win(test)   
    
