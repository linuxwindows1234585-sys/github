import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Engeller ve Noktalar - Dokunmatik')

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Oyun karakteri ve noktalar
player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_velocity = 5
point_radius = 10
points = []

# Engellerin parametreleri
obstacle_width, obstacle_height = 100, 20
obstacle_count = 5
obstacles = []

# FPS
FPS = 60
clock = pygame.time.Clock()

# Dokunmatik kontrol değişkenleri
dragging = False
offset_x, offset_y = 0, 0

# Oyun döngüsü
running = True
while running:
    screen.fill(WHITE)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Parmağı ekrana basma (veya mouse tıklama)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if player_rect.collidepoint(mouse_x, mouse_y):
                dragging = True
                offset_x = player_x - mouse_x
                offset_y = player_y - mouse_y

        # Parmağı sürükleme (veya mouse sürükleme)
        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            player_x = mouse_x + offset_x
            player_y = mouse_y + offset_y

        # Parmağı bırakma (veya mouse bırakma)
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    # Engelleri oluştur
    if not obstacles:
        for i in range(obstacle_count):
            x = random.randint(0, WIDTH - obstacle_width)
            y = random.randint(0, HEIGHT - obstacle_height)
            obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

    # Noktaları oluştur
    if not points:
        for _ in range(3):  # 3 nokta
            x = random.randint(0, WIDTH - point_radius * 2)
            y = random.randint(0, HEIGHT - point_radius * 2)
            points.append(pygame.Rect(x, y, point_radius * 2, point_radius * 2))

    # Engelleri çiz
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

    # Noktaları çiz
    for point in points:
        pygame.draw.circle(screen, GREEN, point.center, point_radius)

    # Oyuncuyu çiz
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Nokta ile çarpışmayı kontrol et
    for point in points[:]:
        if player_rect.colliderect(point):
            points.remove(point)

    # Engeller ile çarpışmayı kontrol et
    for obs in obstacles:
        if player_rect.colliderect(obs):
            running = False  # Çarpışma olursa oyunu bitir

    # Ekranı güncelle
    pygame.display.update()

    # FPS ayarla
    clock.tick(FPS)

pygame.quit()
