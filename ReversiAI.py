import copy
def minmaxPlayer(position, BoardGameScore, BoardGame, depth, alpha, beta, maximizingPlayer, flag):
    if depth == 0:
        if BoardGameScore[position[0]][position[1]] == 99:
            return 999999
        return BoardGameScore[position[0]][position[1]] + position[2]
    if maximizingPlayer:
        maxEval = float('-inf')
        temp = BoardGame
        position = list(position)
        position[0] += 1
        position[1] += 1
        moveNext(temp, flag, position)
        temp = resetBoard(temp, position, flag)
        if flag == 1:
            flag = 0
        else:
            flag = 1
        listP = hintMove(temp, flag)
        for i in listP:
            a = copy.deepcopy(temp)
            eval = minmaxPlayer(i, BoardGameScore, a, depth - 1, alpha, beta, False, flag)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        temp = BoardGame
        position = list(position)
        position[0] += 1
        position[1] += 1
        moveNext(temp, flag, position)
        temp = resetBoard(temp, position, flag)
        if flag == 1:
            flag = 0
        else:
            flag = 1
        listP = hintMove(temp, flag)
        for i in listP:
            a = copy.deepcopy(temp)
            eval = minmaxPlayer(i, BoardGameScore, a, depth - 1, alpha, beta, True, flag)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval



def BoardGame(arrNow):
    print(" ", end=" ")
    for count in range(8):
        print("  " + str(count + 1), end=" ")
    print("\n  ---------------------------------")
    for i in range(8):
        print(i + 1, end=" ")
        for j in range(8):
            if arrNow[i][j] == 1:
                print("| X", end=" ")
            elif arrNow[i][j] == 0:
                print("| O", end=" ")
            elif arrNow[i][j] == 2:
                print("| '", end=" ")
            elif arrNow[i][j] == -1:
                print("|  ", end=" ")
        print("|")
        print("  ---------------------------------")
"""
Output: Done = 1
        Not Yet = 0
"""
def isFinishGame(BoardNow):
    for i in BoardNow:
        if -1 in i:
            return 0
    return 1

'''
Input:
    BoardNow: Board hiện tại
    move: [x, y] là tọa độ nước đi tiếp theo
'''
def isValidMove(BoardNow, move):
    x = int(move[0]) - 1
    y = int(move[1]) - 1
    if x > 7 or x < 0 or y > 7 or y < 0:
        print("[Loi] Out of zone Board!")
        return 0
    if BoardNow[x][y] != 2:
        print("[Loi] Nuoc di khong hop le!")
        return 0
    if BoardNow[x][y] == 1 or BoardNow[x][y] == 0:
        print("[Loi] O khong trong !")
        return 0
    return 1

def moveNext(BoardNow, flag, move):
    if flag == 0:
        a = "O"
    else:
        a = "X"
    while isValidMove(BoardNow, move) == 0:
        move = input("Next Move " + a + " :")
    x = int(move[0]) - 1
    y = int(move[1]) - 1
    BoardNow[x][y] = flag

def resetBoard(BoardNow, move, flag):
    for i in range(8):
        for j in range(8):
            if BoardNow[i][j] == 2:
                BoardNow[i][j] = -1
    dem = [0,0]
    dem[0] = int(move[0]) - 1
    dem[1] = int(move[1]) - 1
    count = 0
    arr = []
    for f in range(dem[1] + 1, 8):
        if BoardNow[dem[0]][f] == -1:
            break
        else:
            if BoardNow[dem[0]][f] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((dem[0], f))
                count += 1
        
    count = 0
    arr = []
    for f in range(dem[0] + 1, 8):
        if BoardNow[f][dem[1]] == -1:
            break
        else:
            if BoardNow[f][dem[1]] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((f, dem[1]))
                count += 1
        
    f = dem[1] - 1
    count = 0
    arr = []
    while f >= 0:
        if BoardNow[dem[0]][f] == -1:
            break
        else:
            if BoardNow[dem[0]][f] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                count += 1
                arr.append((dem[0], f))
                f -= 1
    f = dem[0] - 1
    count = 0
    arr = []
    while f >= 0:
        if BoardNow[f][dem[1]] == -1:
            break
        else:
            if BoardNow[f][dem[1]] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((f, dem[1]))
                count += 1
                f -= 1
    x = dem[0] + 1
    y = dem[1] + 1
    count = 0
    arr = []
    while x <= 7 and y <= 7:
        if BoardNow[x][y] == -1:
            break
        else:
            if BoardNow[x][y] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                count += 1
                arr.append((x, y))
                x += 1
                y += 1
    x = dem[0] - 1
    y = dem[1] + 1
    count = 0
    arr = []
    while x >= 0 and y <= 7:
        if BoardNow[x][y] == -1:
            break
        else:
            if BoardNow[x][y] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((x, y))
                count += 1
                x -= 1
                y += 1
        
    x = dem[0] - 1
    y = dem[1] - 1
    count = 0
    arr = []
    while x >= 0 and y >= 0:
        if BoardNow[x][y] == -1:
            break
        else:
            if BoardNow[x][y] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((x, y))
                count += 1
                x -= 1
                y -= 1
        
    x = dem[0] + 1
    y = dem[1] - 1
    count = 0
    arr = []
    while x <= 7 and y >= 0:
        if BoardNow[x][y] == -1:
            break
        else:
            if BoardNow[x][y] == flag:
                if count != 0:
                    for i in arr:
                        BoardNow[i[0]][i[1]] = flag
                break
            else:
                arr.append((x, y))
                count += 1
                x += 1
                y -= 1
    return BoardNow

def moveByPlayer(BoardNow, flag):
    a = hintMove(BoardNow, flag)
    BoardGame(BoardNow)
    if flag == 0:
        a = "O"
    else:
        a = "X"
    move = input("Next Move " + a + " :")
    moveNext(BoardNow, flag, move)
    if flag == 0:
        return 1, resetBoard(BoardNow, move, flag)
    else:
        return 0, resetBoard(BoardNow, move, flag)

def moveAI(BoardNow, flag, move):
    moveNext(BoardNow, flag, move)
    if flag == 0:
        return 1, resetBoard(BoardNow, move, flag)
    else:
        return 0, resetBoard(BoardNow, move, flag)

def hintMove(BoardNow, flag):
    arrHint = []
    if flag == 0:
        target = 0
        flag = 1
    else:
        target = 1
        flag = 0
    for i in range(8):
        for j in range(8):
            if flag == BoardNow[i][j]:
                listE = []
                try:
                    if BoardNow[i-1][j-1] == -1:
                        listE.append((i-1,j-1))
                except:
                    pass
                try:
                    if BoardNow[i-1][j] == -1:
                        listE.append((i-1, j))
                except:
                    pass
                try:
                    if BoardNow[i-1][j+1] == -1:
                        listE.append((i-1, j+1))
                except:
                    pass
                try:
                    if BoardNow[i][j-1] == -1:
                        listE.append((i, j-1))
                except:
                    pass
                try:
                    if BoardNow[i+1][j-1] == -1:
                        listE.append((i+1, j-1))
                except:
                    pass
                try:
                    if BoardNow[i][j+1] == -1:
                        listE.append((i, j+1))
                except:
                    pass
                try:
                    if BoardNow[i+1][j+1] == -1:
                        listE.append((i+1, j+1))
                except:
                    pass
                try:
                    if BoardNow[i+1][j] == -1:
                        listE.append((i+1, j))
                except:
                    pass
                for dem in listE:
                    count = 0
                    arr = []
                    diem = 0
                    for f in range(dem[1] + 1, 8):
                        if BoardNow[dem[0]][f] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[dem[0]][f])
                            if BoardNow[dem[0]][f] == flag:
                                diem += boardScore[dem[0]][f]
                            count += 1
                        
                    count = 0
                    arr = []
                    
                    for f in range(dem[0] + 1, 8):
                        if BoardNow[f][dem[1]] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[f][dem[1]])
                            if BoardNow[f][dem[1]] == flag:
                                diem += boardScore[f][dem[1]]
                            count += 1
                        
                    f = dem[1] - 1
                    count = 0
                    arr = []
                    
                    while f >= 0:
                        if BoardNow[dem[0]][f] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            count += 1
                            arr.append(BoardNow[dem[0]][f])
                            if BoardNow[dem[0]][f] == flag:
                                diem += boardScore[dem[0]][f]
                            f -= 1
                    f = dem[0] - 1
                    count = 0
                    arr = []
                    
                    while f >= 0:
                        if BoardNow[f][dem[1]] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[f][dem[1]])
                            if BoardNow[f][dem[1]] == flag:
                                diem += boardScore[f][dem[1]]
                            count += 1
                            f -= 1
                    x = dem[0] + 1
                    y = dem[1] + 1
                    count = 0
                    arr = []
                    
                    while x <= 7 and y <= 7:
                        if BoardNow[x][y] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            count += 1
                            arr.append(BoardNow[x][y])
                            if BoardNow[x][y]:
                                diem += boardScore[x][y]
                            x += 1
                            y += 1
                    x = dem[0] - 1
                    y = dem[1] + 1
                    count = 0
                    arr = []
                    
                    while x >= 0 and y <= 7:
                        if BoardNow[x][y] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[x][y])
                            count += 1
                            if BoardNow[x][y] == flag:
                                diem += boardScore[x][y]
                            x -= 1
                            y += 1
                        
                    x = dem[0] - 1
                    y = dem[1] - 1
                    count = 0
                    arr = []
                    
                    while x >= 0 and y >= 0:
                        if BoardNow[x][y] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[x][y])
                            count += 1
                            if BoardNow[x][y] == flag:
                                diem += boardScore[x][y]
                            x -= 1
                            y -= 1
                        
                    x = dem[0] + 1
                    y = dem[1] - 1
                    count = 0
                    arr = []
                    
                    while x <= 7 and y >= 0:
                        if BoardNow[x][y] == target:
                            if count != 0:
                                if (-1 not in arr) and (flag in arr) and (2 not in arr) and ((dem[0], dem[1]) not in arrHint):
                                    BoardNow[dem[0]][dem[1]] = 2
                                    arrHint.append((dem[0], dem[1], diem))
                            break
                        else:
                            arr.append(BoardNow[x][y])
                            count += 1
                            if BoardNow[x][y] == flag:
                                diem += boardScore[x][y]
                            x += 1
                            y -= 1
    out = []
    for i in arrHint:
        i = list(i)
        if (i[0] >= 0 and i[0] <= 7) and (i[1] >= 0 and i[1] <= 7):
            out.append(tuple(i))
    return out
arrNow = [  [-1]*8,
            [-1]*8,
            [-1]*8,
            [-1]*8,
            [-1]*8,
            [-1]*8,
            [-1]*8,
            [-1]*8 ]

boardScore = [  [45, 32, 19, 18, 31, 24, 44, 43],
                [46, 36, 9, 11, 16, 15, 42, 56],
                [17, 8, 3, 4, 10, 22, 38, 51],
                [20, 13, 5, 1, 1, 6, 23, 40],
                [21, 14, 7, 1, 1, 1, 39, 41,],
                [34, 30, 12, 2, 28, 29, 53, 52], 
                [35, 47, 33, 26, 25, 37, 59, 55],
                [50, 49, 48, 27, 54, 60, 58, 57]]

boardMove = [
                [99,  -8,  8,  6,  6,  8,  -8, 99],
                [-8, -24, -4, -3, -3, -4, -24, -8],
                [8,  -4,  7,  4,  4,  7,  -4,  8],
                [6,  -3,  4,  0,  0,  4,  -3,  6],
                [ 6,  -3,  4,  0,  0,  4,  -3,  6],
            [ 8,  -4,  7,  4,  4,  7,  -4,  8],
            [-8, -24, -4, -3, -3, -4, -24, -8],
            [99,  -8,  8,  6,  6,  8,  -8, 99]
            ]
arrNow[4][4] = 0
arrNow[3][3] = 0
arrNow[3][4] = 1
arrNow[4][3] = 1
BoardGame(arrNow)
flag = 0 if input("Choose team (X or O): ") == "O" else 1
while isFinishGame(arrNow) == 0:
    #flag, arrNow = moveByPlayer(arrNow, flag)
    hint = hintMove(arrNow, flag)
    pointList = []
    for i in hint:
        #minmaxPlayer(position, BoardGameScore, BoardGame, depth, alpha, beta, maximizingPlayer, flag)
        temp = copy.deepcopy(arrNow)
        pointList.append(minmaxPlayer(i, boardMove, temp, 7, float('-inf'), float('inf'), True, flag))
    index = pointList.index(max(pointList))
    hint[index] = list(hint[index])
    hint[index][0] += 1
    hint[index][1] += 1
    flag, arrNow = moveAI(arrNow, flag, hint[index])
    print("Move: " + str(hint[index]))
    flag, arrNow = moveByPlayer(arrNow, flag)
countP1 = 0
countP2 = 0
for i in range(8):
    for j in range(8):
        if arrNow == 0:
            countP1 += 1
        else:
            countP2 += 1
if countP1 > countP2:
    print("Nguoi chien thang la O")
elif countP1 < countP2:
    print("Nguoi chien thang la X")
else:
    print("Hoa!")