# 6. Έστω μία σκακίερα στην οποία τοποθετούμε πάνω της, σε τυχαίες θέσεις, έναν λευκό πύργο και αξιωματικό και μια μαύρη
# βασίλισσα. Ο κάθε παίκτης παίρνει ως δυο βαθμούς σε κάθε γύρο ανάλογα με το αν τρώει κομμάτι του αντιπάλου. Έτσι,
# ο λευκός μπορεί να πάρει 2 βαθμούς αν ο πύργος τρώει τη βασίλισσα και το ίδιο κάνει και ο αξιωματικός του. Αν μόνο
# ένα από τα κομμάτια του τρώει τη βασίλισσα τότε παίρνει ένα βαθμό. Αντίστοιχα, ο μαύρος παίρνει δύο βαθμούς αν η
# βασίλισσά του μπορεί να φάει και τα δύο κομμάτια του λευκού ή ένα αν μπορεί να φάει μόνο ένα. Μετά από 100 παιχνίδια,
# εμφανίστε τους βαθμούς των δύο παικτών.

import random
Player1Wins = 0
Player2Wins = 0
Draws = 0
#I think that A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8
for x in range(1,101):
    Xx = [i for i in range(1, 9)]
    Yy = [i for i in range(1, 9)]
    Pin = []
#I put it random and I choose the first 3.
    for i in Xx:
        for j in Yy:
            Pin.append([i,j])
    random.shuffle(Pin)

    PinWhiteRook=[]
    PinWhiteBishop=[]
    PinBlackQueen=[]
    PinWhiteRook.append(Pin.pop())
    PinWhiteBishop.append(Pin.pop())
    PinBlackQueen.append(Pin.pop())

    print("A White Rook is in place:",PinWhiteRook)
    print("A White Bishop is in place:",PinWhiteBishop)
    print("A Black Queen is in place:",PinBlackQueen)
#conversion to natural number
    Rook=PinWhiteRook[0][0]*10+PinWhiteRook[0][1]
    Bishop=PinWhiteBishop[0][0]*10+PinWhiteBishop[0][1]
    Queen=PinBlackQueen[0][0]*10+PinBlackQueen[0][1]
    print(Rook,Bishop,Queen)

    Player1=0
    Player2=0
    #print(Rook//10,Bishop//10,Queen//10)
    #print(Rook%10,Bishop%10,Queen%10)

    #searching in lines
    if Rook//10==Queen//10:
        if Rook//10==Bishop//10:
            if Rook%10>Bishop%10 and Bishop%10>Queen%10:
                Player2 +=1
            elif Rook%10<Bishop%10 and Bishop%10<Queen%10:
                Player2 +=1
            elif Rook%10>Queen%10 and Queen%10>Bishop%10:
                Player1 += 1
                Player2 += 2
            elif Rook%10<Queen%10 and Queen%10<Bishop%10:
                Player1 += 1
                Player2 += 2
        else:
            Player1 += 1
            Player2 += 1
    elif Queen//10==Bishop//10   and Rook//10!=Queen//10:
        Player1 += 0
        Player2 += 1


    if Rook%10==Queen%10:
        if Rook%10==Bishop%10:
            if Rook//10>Bishop//10 and Bishop//10>Queen//10:
                Player2 += 1
            elif Rook//10<Bishop//10 and Bishop//10<Queen//10:
                Player2 += 1
            elif Rook//10 > Queen//10 and Queen//10>Bishop//10:
                Player1 += 1
                Player2 += 2
            elif Rook//10 < Queen//10 and Queen//10<Bishop//10:
                Player1 += 1
                Player2 += 2
        else:
            Player1 += 1
            Player2 += 1
    elif Queen%10==Bishop%10   and Rook%10!=Queen%10:
        Player1 += 0
        Player2 += 1

    # searching in diagonals
    n = Bishop
    m = Bishop
    k = Bishop
    l = Bishop
    ValidPinBishop = []
    a=min((8-Bishop%10),(8-Bishop//10))+1
    for i in range(1,a):
        m = m + i * 11
        if m <= 88 and m >= 11:
            ValidPinBishop.append(m)
            m = Bishop
    b=min((Bishop%10) -1, (8 - Bishop // 10))+1
    for i in range(1,b):
        k =k + i * 9
        if k<=88 and k>=11:
            ValidPinBishop.append(k)
            k = Bishop
    c= min((Bishop // 10) - 1, (Bishop % 10)-1)+1
    for i in range(1, c):
        l = l +i*(-11)
        if l <= 88 and l >= 11:
            ValidPinBishop.append(l)
            l = Bishop
    d=min((Bishop // 10) - 1,8- (Bishop % 10) )+1
    for i in range(1,d):
        n = n + i * (-9)
        if n <= 88 and n >= 11:
            ValidPinBishop.append(n)
            n=Bishop
    #print(ValidPinBishop)

    n = Queen
    m = Queen
    k = Queen
    l = Queen
    ValidPinQueen = []
    a = min((8 - Queen % 10), (8 - Queen // 10)) + 1
    for i in range(1, a):
        m = m + i * 11
        if m <= 88 and m >= 11:
            ValidPinQueen.append(m)
            m = Queen
    b = min((Queen % 10) - 1, (8 - Queen // 10)) + 1
    for i in range(1, b):
        k = k + i * 9
        if k <= 88 and k >= 11:
            ValidPinQueen.append(k)
            k = Queen
    c = min((Queen // 10) - 1, (Queen % 10) - 1) + 1
    for i in range(1, c):
        l = l + i * (-11)
        if l <= 88 and l >= 11:
            ValidPinQueen.append(l)
            l = Queen
    d = min((Queen // 10) - 1, 8 - (Queen % 10)) + 1
    for i in range(1, d):
        n = n + i * (-9)
        if n <= 88 and n >= 11:
            ValidPinQueen.append(n)
            n = Queen
    #print(ValidPinQueen)

    Common = []
    for element in ValidPinQueen:
        if element in ValidPinBishop:
            Common.append(element)
    #print(Common)

    if (Bishop in ValidPinQueen) and (Queen in ValidPinBishop):
        if Rook not in Common:
            Player1 += 1
            Player2 += 1
        else:
            Player1 += 0
            Player2 += 1
    if Rook in ValidPinQueen:
        Player1 += 0
        Player2 += 1

    print("Player1=",Player1," Vs Player2=",Player2)
    if Player2 > Player1:
        Player2Wins += 1
        print("Player2 win!")
    if Player2 == Player1:
        Draws += 1
        print("Draw")
    if Player2 < Player1:
        Player1Wins += 1
        print("Player2 win!")


print("Player1 wins in ",Player1Wins,'%')
print("Player2 wins in ",Player2Wins,'%')
print("and",Draws,"are Draws")