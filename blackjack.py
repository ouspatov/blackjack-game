# NOTE: Font: Inter (Google Font: https://fonts.google.com/specimen/Inter)
# NOTE: Card Root: https://acbl.mybigcommerce.com/52-playing-cards/\

import pygame
import random

class Card():
    def __init__(self, value, name, suit, image):
        # Card Representation: value, name, suit, image
        self.name = name
        self.value = value
        self.suit = suit
        self.image = image

def deckInit():
    # Creates and returns a full deck
    deck = []
    index = 0
    for value_index in range(len(CARD_VALUES)):
        for suit in CARD_SUITS:
            deck.append(Card(CARD_VALUES[value_index], CARD_NAMES[value_index], suit, CARD_IMAGES[index]))
            index += 1
    return deck

def getRandomCard():
    # Removes and returns a random card so there is no duplicates
    global full_deck
    random_index = random.randint(0, len(full_deck) - 1)
    return full_deck.pop(random_index)

def getPlayersCard():
    # Adds a card to the player hand and makes a visual representation
    global player_card_positions_x, player_card_positions_y

    player_hand.append(getRandomCard())

    # Update the x for the new card placement
    if len(player_card_positions_x) == 0:
        player_card_positions_x.append(default_x_position)
    else:
        player_card_positions_x.append(player_card_positions_x[-1] + card_offset)

    # Add the default y for the card
    player_card_positions_y.append(default_y_position)

def getAiCard():
    # Adds a card to the AI hand and updates its positions if the AI hand value is less than 18
    global ai_card_positions_x, ai_card_positions_y, hidden_hand, hidden_hand_positions_x, hidden_hand_positions_y

    if calcHandValue(ai_hand) < 18:
        ai_hand.append(getRandomCard())
        hidden_hand.append(card_back_image)

        # Update the x for hidden and AI cards
        if len(hidden_hand_positions_x) == 0:
            hidden_hand_positions_x.append(default_x_position)
        else:
            hidden_hand_positions_x.append(hidden_hand_positions_x[-1] + card_offset)

        if len(ai_card_positions_x) == 0:
            ai_card_positions_x.append(default_x_position)
        else:
            ai_card_positions_x.append(ai_card_positions_x[-1] + card_offset)

        # Add the default y for AI and hidden cards
        ai_card_positions_y.append(ai_default_y_position)
        hidden_hand_positions_y.append(ai_default_y_position)
        
        return True
    else:
        return False

def calcHandValue(hand):
    # Calculates and returns the value of a hand and aces implementation
    if len(hand) == 0:
        return 0
    else:
        aces = []
        total_value = 0
        for card in hand:
            if card.name == 1:
                aces.append(card)
            total_value += card.value
        # Aces implementation
        if total_value > 21 and len(aces) != 0:
            total_value -= 10
        return total_value

def drawMenu():
    # GUI
    title_text = title_font.render("Blackjack Game", True, white_color)
    subtitle_text = author_font.render("Made by Orkhan Uspatov", True, white_color)
    screen.blit(title_text, (62, 62))
    screen.blit(subtitle_text, (62, 99))

    # Display the current values of player and AI hands
    player_hand_value = calcHandValue(player_hand)
    ai_hand_value = calcHandValue(ai_hand)

    player_hand_text = regular_font.render(f"Your Hand: {player_hand_value}", True, white_color)
    ai_hand_text = regular_font.render(f"AI Hand: {ai_hand_value if spectate else ' '}", True, white_color)

    screen.blit(ai_hand_text, (62, 356))
    screen.blit(player_hand_text, (65, 143))

    # Display game rules
    rules_title_text = heading_font.render("Rules:", True, white_color)
    screen.blit(rules_title_text, (650, 60))
    rules = [
        "Press [Enter] to pass",
        "Press [Space] to hit",
        "Press [Tab] to spectate",
        "Press [Esc] to restart",
    ]
    
    for i, rule_line in enumerate(rules):
        rule_text = regular_font.render(rule_line, True, white_color)
        screen.blit(rule_text, (650, 91 + i * 30))

    # Display the game table status
    table_title_text = heading_font.render("Table:", True, white_color)
    screen.blit(table_title_text, (650, 420))
    table = [
        f"AI score: {str(calcHandValue(ai_hand)) if reveal else ' '}",
        f"Your Score: {str(calcHandValue(player_hand)) if reveal else ' '}",
        f"Winner: {win_messages[win_state]}"
    ]

    for i, table_line in enumerate(table):
        table_text = regular_font.render(table_line, True, white_color)
        screen.blit(table_text, (650, 453 + i * 30))

    # Draw player cards
    for i, card in enumerate(player_hand):
        x = player_card_positions_x[i]
        y = player_card_positions_y[i]
        screen.blit(card.image, (x, y))

    # Draw AI cards or hidden cards based on the game state
    if reveal or spectate:
        for i, card in enumerate(ai_hand):
            x = ai_card_positions_x[i]
            y = ai_card_positions_y[i]
            screen.blit(card.image, (x, y))
    else:
        for i, card in enumerate(hidden_hand):
            x = hidden_hand_positions_x[i]
            y = hidden_hand_positions_y[i]
            screen.blit(card.image, (x, y))
    
    pygame.display.update()


# Initialization
pygame.init()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("BlackJack")
icon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
CARD_NAMES = list(range(1, 14))
CARD_SUITS = list(range(1, 5))

CARD_WIDTH = 100
CARD_HEIGHT = 150

CARD_IMAGE_PATHS = []
CARD_IMAGES = []

player_hand = []
player_card_positions_x = []
player_card_positions_y = []

ai_hand = []
ai_card_positions_x = []
ai_card_positions_y = []

hidden_hand = []
hidden_hand_positions_x = []
hidden_hand_positions_y = []

default_x_position = 65
default_y_position = 181
ai_default_y_position = 392
card_offset = 50

background_color = (26, 26, 26)
white_color = (255, 255, 255)

for card_name in CARD_NAMES:
    for card_suit in CARD_SUITS:
        CARD_IMAGE_PATHS.append(f"Assets/{card_name}-{card_suit}.png")

for path in CARD_IMAGE_PATHS:
    CARD_IMAGES.append(pygame.transform.scale(pygame.image.load(path), (CARD_WIDTH, CARD_HEIGHT)))

card_back_image = Card(0, 0, 0, pygame.transform.scale(pygame.image.load("Assets/card_background.png"), (CARD_WIDTH, CARD_HEIGHT)))

title_font = pygame.font.Font("Fonts/Inter-Bold.ttf", 32)
author_font = pygame.font.Font("Fonts/Inter-Regular.ttf", 16)
regular_font = pygame.font.Font("Fonts/Inter-Regular.ttf", 20)
heading_font = pygame.font.Font("Fonts/Inter-Bold.ttf", 24)

full_deck = deckInit()

win_state = 0
win_messages = ['', 'PLAYER WINS', 'AI WINS', 'PLAYER BUST - AI WINS', 'PLAYER WINS - AI BUST', 'TIED', 'NO WINNERS']

run = True
reveal = False
session = True
spectate = False

# Game Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Handles quitting the game
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Resets the game state and starts a new session
                full_deck = deckInit()
                session = True
                win_state = 0
                reveal = False
                spectate = False
                player_hand = []
                player_card_positions_x = []
                player_card_positions_y = []
                ai_hand = []
                ai_card_positions_x = []
                ai_card_positions_y = []
                hidden_hand = []
                hidden_hand_positions_x = []
                hidden_hand_positions_y = []

            elif event.key == pygame.K_SPACE and session:
                # Hit
                getPlayersCard()
                ai_hit = getAiCard()

                # Determines if either hand reached a winning condition
                if calcHandValue(ai_hand) > 21 and calcHandValue(player_hand) > 21:
                    session = False
                    win_state = 6
                    reveal = True
                elif calcHandValue(ai_hand) > 21:
                    session = False
                    win_state = 4
                    reveal = True
                elif calcHandValue(player_hand) > 21:
                    session = False
                    win_state = 3
                    reveal = True
                elif calcHandValue(ai_hand) == 21 or calcHandValue(player_hand) == 21:
                    session = False
                    reveal = True
                    win_state = 1 if calcHandValue(player_hand) == 21 else 2

            elif (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN) and session:
                # Player pass and AI action
                ai_hit = getAiCard()

                # Check winner after AI action
                if not ai_hit:
                    if calcHandValue(ai_hand) > calcHandValue(player_hand):
                        session = False
                        win_state = 2
                        reveal = True
                    elif calcHandValue(ai_hand) < calcHandValue(player_hand):
                        session = False
                        win_state = 1
                        reveal = True
                    else:
                        session = False
                        win_state = 5
                        reveal = True
                else:
                    if calcHandValue(ai_hand) > 21 and calcHandValue(player_hand) > 21:
                        session = False
                        win_state = 6
                        reveal = True
                    elif calcHandValue(ai_hand) > 21:
                        session = False
                        win_state = 4
                        reveal = True
                    elif calcHandValue(ai_hand) == 21 or calcHandValue(player_hand) == 21:
                        session = False
                        reveal = True
                        win_state = 1 if calcHandValue(player_hand) == 21 else 2

            elif event.key == pygame.K_TAB:
                # Spectate mode
                spectate = not spectate

    # Screen update
    screen.fill(background_color)
    drawMenu()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()