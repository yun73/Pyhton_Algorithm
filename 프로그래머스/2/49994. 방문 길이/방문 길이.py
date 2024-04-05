def solution(dirs):
    
    command = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0),}
    visited = set()
    
    ## 시작 위치이자 현재 위치
    x,y = 0,0
    for cmd in dirs:
        nx,ny = x+command[cmd][0], y+command[cmd][1]
        
        # 현재 가려는 곳이 좌표 경계 밖이면 건너뛰기
        if not ( -5<= nx <=5 and -5<= ny <= 5):
            continue
        
      
        if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited: 
            visited.add((x,y,nx,ny))
            
        x,y = nx,ny
    return len(list(visited))