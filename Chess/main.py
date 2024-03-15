import pygame
pygame.init()
screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("Chess")
timer = pygame.time.Clock()
fps = 60


# variables
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

valid_moves = []
turn_steps = 0
selection = 10


# pieces
black_king = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/king.png'), (50, 50)).convert_alpha()
black_king_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/king.png'), (60, 60)).convert_alpha()
black_queen = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/queen.png'), (50, 50)).convert_alpha()
black_queen_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/queen.png'), (60, 60)).convert_alpha()
black_bishop = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/bishop.png'), (50, 50)).convert_alpha()
black_bishop_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/bishop.png'), (60, 60)).convert_alpha()
black_rook = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/rook.png'), (50, 50)).convert_alpha()
black_rook_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/rook.png'), (60, 60)).convert_alpha()
black_knight = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/knight.png'), (50, 50)).convert_alpha()
black_knight_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/knight.png'), (60, 60)).convert_alpha()
black_pawn = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/pawn.png'), (50, 50)).convert_alpha()
black_pawn_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/pawn.png'), (60, 60)).convert_alpha()


white_king = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/king.png'), (50, 50)).convert_alpha()
white_king_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/king.png'), (30, 30)).convert_alpha()
white_queen = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/queen.png'), (50, 50)).convert_alpha()
white_queen_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/queen.png'), (60, 60)).convert_alpha()
white_bishop = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/bishop.png'), (50, 50)).convert_alpha()
white_bishop_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/bishop.png'), (60, 60)).convert_alpha()
white_rook = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/rook.png'), (50, 50)).convert_alpha()
white_rook_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/rook.png'), (60, 60)).convert_alpha()
white_knight = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/knight.png'), (50, 50)).convert_alpha()
white_knight_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/knight.png'), (60, 60)).convert_alpha()
white_pawn = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/pawn.png'), (50, 50)).convert_alpha()
white_pawn_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/pawn.png'), (60, 60)).convert_alpha()

white_images = [white_king, white_queen,
                white_knight, white_bishop, white_rook, white_pawn]
white_small_images = [white_king_small, white_queen_small,
                      white_knight_small, white_bishop_small, white_rook_small, white_pawn_small]
black_images = [black_king, black_queen,
                black_knight, black_bishop, black_rook, black_pawn]
black_small_images = [black_king_small, black_queen_small,
                      black_knight_small, black_bishop_small, black_rook_small, black_pawn_small]

pieces_list = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']


def draw_board(screen):
    dark_square_color = (217, 180, 138, 255)
    light_square_color = (145, 80, 47, 255)

    square_size = min(screen.get_width() // 8, screen.get_height() // 8)

    for row in range(8):
        for col in range(8):
            x = col * square_size
            y = row * square_size
            color = light_square_color if (
                row + col) % 2 == 0 else dark_square_color
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

    pygame.draw.rect(screen, (239, 214, 170, 255), [600, 0, 100, 600], 3)


def draw_pieces():
    for row in range(len(white_pieces)):
        index = pieces_list.index(white_pieces[row])
        if (white_pieces[row] == 'pawn'):
            screen.blit(white_pawn,
                        (white_locations[row][0]*75+10, white_locations[row][1]*75+10))
        else:
            screen.blit(white_images[index],
                        (white_locations[row][0]*75 + 10, white_locations[row][1]*100+10))
        if turn_steps < 2:
            if selection == row:
                pygame.draw.rect(screen, 'red', [
                                 white_locations[row][0]*75, white_locations[row][1]*75, 75, 75], 2)

    for row in range(len(black_pieces)):
        index = pieces_list.index(black_pieces[row])
        if (black_pieces[row] == 'pawn'):
            screen.blit(black_pawn,
                        (black_locations[row][0]*75 + 10, black_locations[row][1]*75+10))
        else:
            screen.blit(black_images[index],
                        (black_locations[row][0]*75 + 10, black_locations[row][1]*75 + 10))
        if turn_steps >= 2:
            if selection == row:
                pygame.draw.rect(screen, 'blue', [
                                 black_locations[row][0]*75, black_locations[row][1]*75, 75, 75], 2)


run = True
while run:
    timer.tick(fps)
    dark_square_color = (217, 180, 138, 255)

    screen.fill((157, 94, 60, 255))
    draw_board(screen)
    draw_pieces()
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_cord = event.pos[0] // 75
            y_cord = event.pos[1] // 75
            click_cords = (x_cord, y_cord)
            if turn_steps < 2:
                if click_cords in white_locations:
                    selection = white_locations.index(click_cords)
                    turn_steps += 1
                if click_cords in valid_moves and selection != 100:
                    white_locations = 

    pygame.display.flip()

pygame.quit()
