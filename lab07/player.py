import pygame
import os


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Music Player")


font = pygame.font.Font(None, 36)


music_directory = "lab07\music"
songs = os.listdir(music_directory)
current_song_index = 0


current_song = pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))


def play_song():
    pygame.mixer.music.play()


def stop_song():
    pygame.mixer.music.stop()


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))
    play_song()


def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_directory, songs[current_song_index]))
    play_song()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_song()
                else:
                    play_song()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()


    screen.fill(WHITE)

 
    text = font.render("Press SPACE to Play/Pause, LEFT/RIGHT arrows for Previous/Next Song", True, BLACK)
    screen.blit(text, (50, 50))


    pygame.display.flip()


pygame.quit()
