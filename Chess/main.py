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
selection = 1000


# pieces
black_king = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/king.png'), (80, 80)).convert_alpha()
black_king_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/king.png'), (60, 60)).convert_alpha()
black_queen = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/queen.png'), (80, 80)).convert_alpha()
black_queen_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/queen.png'), (60, 60)).convert_alpha()
black_bishop = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/bishop.png'), (80, 80)).convert_alpha()
black_bishop_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/bishop.png'), (60, 60)).convert_alpha()
black_rook = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/rook.png'), (80, 80)).convert_alpha()
black_rook_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/rook.png'), (60, 60)).convert_alpha()
black_knight = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/knight.png'), (80, 80)).convert_alpha()
black_knight_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/knight.png'), (60, 60)).convert_alpha()
black_pawn = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/pawn.png'), (80, 80)).convert_alpha()
black_pawn_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/black_pieces/pawn.png'), (60, 60)).convert_alpha()


white_king = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/king.png'), (80, 80)).convert_alpha()
white_king_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/king.png'), (60, 60)).convert_alpha()
white_queen = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/queen.png'), (80, 80)).convert_alpha()
white_queen_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/queen.png'), (60, 60)).convert_alpha()
white_bishop = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/bishop.png'), (80, 80)).convert_alpha()
white_bishop_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/bishop.png'), (60, 60)).convert_alpha()
white_rook = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/rook.png'), (80, 80)).convert_alpha()
white_rook_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/rook.png'), (60, 60)).convert_alpha()
white_knight = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/knight.png'), (80, 80)).convert_alpha()
white_knight_small = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/knight.png'), (60, 60)).convert_alpha()
white_pawn = pygame.transform.scale(pygame.image.load(
    'Chess/assets/white_pieces/pawn.png'), (80, 80)).convert_alpha()
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

run = True
while run:
    timer.tick(fps)
    screen.fill("black")

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
