
board=[[c+f*3 for c in range(1,4)] for f in range(3)]
board = str(board)
print(board)
for n in range(1, 15):
    if str(n) in board:
        print(n, "si está")
    else:
        continue
        print(n,"no está")