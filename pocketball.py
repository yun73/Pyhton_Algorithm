import pygame
import math

# 초기화
pygame.init()

# 화면 크기 및 색상 설정
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (0, 0, 0)
ball_color = (255, 255, 255)

# 게임 루프 변수
running = True

# 현재 공의 위치 및 속도 설정
ball_x, ball_y = 100, 200
ball_radius = 10
ball_speed = 5
ball_direction = math.radians(45)  # 45도 각도로 시작

# 목적구 위치 설정
target_x, target_y = 700, 200
target_radius = 15

# 쿠션 경계 설정
cushion_x, cushion_y, cushion_width, cushion_height = 50, 50, 700, 300

# 게임 루프
clock = pygame.time.Clock()  # 게임 루프의 속도 제어를 위한 Clock 객체 생성
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 공의 새로운 위치 계산
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)

    # 쿠션과의 충돌 처리
    if ball_x - ball_radius < cushion_x or ball_x + ball_radius > cushion_x + cushion_width:
        ball_direction = math.pi - ball_direction  # 수평 벽에 부딪히면 방향 반전
    if ball_y - ball_radius < cushion_y or ball_y + ball_radius > cushion_y + cushion_height:
        ball_direction = -ball_direction  # 수직 벽에 부딪히면 방향 반전

    # 화면 지우기
    screen.fill(background_color)

    # 공 그리기
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # 목적구 그리기
    pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), target_radius)

    # 화면 업데이트
    pygame.display.flip()

    # 목적구에 공이 도달하면 게임 종료
    if math.sqrt((ball_x - target_x) ** 2 + (ball_y - target_y) ** 2) <= ball_radius + target_radius:
        print("목적구를 넣었습니다. 게임 종료.")
        running = False

    # 게임 루프의 속도를 제어
    clock.tick(60)  # 초당 60프레임을 유지

# 게임 종료
pygame.quit()
