import requests
import pygame

import config
import app_settings

pygame.init()

screen = pygame.display.set_mode(app_settings.WND_SIZE)
pygame.display.set_caption(app_settings.WND_NAME)

current_image = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    image_id = int(input())  # todo input from app (not from terminal)

    r_json = {'id': image_id}
    response = requests.post(config.SERVER_URL, json=r_json)
    if response.status_code == 200:
        with open('received_image.png', 'wb') as f:
            f.write(response.content)
        print('Image received and saved.')
        current_image = pygame.image.load('received_image.png')
        current_image = pygame.transform.scale(
            current_image,
            app_settings.WND_SIZE
        )
    else:
        print('Error:', response.json())

    if current_image:
        screen.blit(current_image, (0, 0))
        pygame.display.flip()
pygame.quit()
