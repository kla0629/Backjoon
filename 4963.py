"""
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

while True:
    w, h = map(int, input().split())
    if not w:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    check = [[False]*w for _ in range(h)]

    def dfs(x, y):
        check[x][y] = True
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if a[nx][ny] == 1 and check[nx][ny] is False:
                dfs(nx, ny)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and check[i][j] is False:
                dfs(i, j)
                cnt += 1
    print(cnt)