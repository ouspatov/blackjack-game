#### **Project Overview**

This project is a **Blackjack game** built using **Pygame**. The game simulates a typical Blackjack experience where the player competes against an AI, with gameplay controls managed via the keyboard.

#### **Code Structure**

The project is organized into several key parts:

1. **Card Class** — Handles the individual card attributes.
2. **Deck Initialization** — Creates a full deck of cards.
3. **Game Logic** — Controls the flow of the game, including player and AI actions.
4. **User Interface** — Displays game information and updates on the screen.

---

### **Key Functions and Classes**

#### 1. **Card Class**

The `Card` class represents each card in the deck, storing its value, name, suit, and image.

```python
class Card():
    def __init__(self, value, name, suit, image):
        # Card Representation: value, name, suit, image
        self.name = name
        self.value = value
        self.suit = suit
        self.image = image
```

- **value**: Numeric value of the card (e.g., 2–10, J, Q, K as 10, Ace as 11 or 1).
- **name**: The card’s identifier (1-13, where 1 is Ace, 11 is Jack, etc.).
- **suit**: The suit of the card (1–4 representing Spades, Hearts, Diamonds, Clubs).
- **image**: The image associated with the card used in the UI.

### **Importing Cards**

```python
for card_name in CARD_NAMES:
    for card_suit in CARD_SUITS:
        CARD_IMAGE_PATHS.append(f"Assets/{card_name}-{card_suit}.png")

for path in CARD_IMAGE_PATHS:
    CARD_IMAGES.append(pygame.transform.scale(pygame.image.load(path), (CARD_WIDTH, CARD_HEIGHT)))

card_back_image = Card(0, 0, 0, pygame.transform.scale(pygame.image.load("Assets/card_background.png"), (CARD_WIDTH, CARD_HEIGHT)))
```

- Pulling all of the cards using nested loop
- Rescaling to the (CARD_WIDTH, CARD_HEIGHT)
- `card_back_image` = Card's back

#### 2. **Deck Initialization (`deckInit`)**

The `deckInit` function initializes a deck of 52 cards, creating a new `Card` object for each combination of value and suit.

```python
def deckInit():
    # Creates and returns a full deck
    deck = []
    index = 0
    for value_index in range(len(CARD_VALUES)):
        for suit in CARD_SUITS:
            deck.append(Card(CARD_VALUES[value_index], CARD_NAMES[value_index], suit, CARD_IMAGES[index]))
            index += 1
    return deck
```

-  **Purpose**: It generates a complete deck and returns it.
#### 3. **Get Random Card (`getRandomCard`)**

This function picks a random card from the deck, removes it, and returns it to ensure no duplicates.

```python
def getRandomCard():
    # Removes and returns a random card so there is no duplicates
    global full_deck
    random_index = random.randint(0, len(full_deck) - 1)
    return full_deck.pop(random_index)
```

- **Purpose**: Randomly selects a card from the remaining deck and removes it, ensuring uniqueness in card distribution.

#### 4. **Get Player’s Card (`getPlayersCard`)**

This function adds a card to the player's hand and visually updates its position on the screen.

```python
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
```

- **Purpose**: Draws a card for the player and places it on the screen.
- **player_card_positions_x** and **player_card_positions_y** are used to adjust the card's position on the UI.

#### 5. **Get AI’s Card (`getAiCard`)**

This function adds a card to the AI's hand, but only if the AI’s hand value is less than 18.

```python
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
```

- **Purpose**: Adds cards to the AI's hand until the hand value is 18 or greater.

#### 6. **Calculate Hand Value (`calcHandValue`)**

This function calculates the value of a given hand and adjusts for Aces (which can be 1 or 11).

```python
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
```

- **Purpose**: Adds the card values and accounts for Aces, adjusting the value if it exceeds 21.

#### 7. **Draw Menu (`drawMenu`)**

This function is responsible for rendering the user interface, displaying information like player and AI hand values, game rules, and card images.

```python
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
```

- **Purpose**: This function handles all visual aspects of the game. It updates the screen with text, images, and game status.

#### **Game Loop Overview**

The game loop repeatedly checks for user input, updates game logic (such as checking for win conditions or card values), and redraws the game interface. It runs until the player quits the game.

---

### **Code: Game Loop**

```python
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
                # Hit: Player gets a card
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
                # Pass: Player ends their turn, AI gets a card
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
                # Switch to Spectator Mode
                spectate = not spectate

    # Screen update
    screen.fill(background_color)
    drawMenu()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

### **Detailed Breakdown of the Game Loop**

#### 1. **Main Game Loop:**

The `while run:` loop is the main game loop that keeps running until the game ends (when `run` is set to `False`).

```python
while run:
    for event in pygame.event.get():
```

- **Purpose**: Continuously checks for events (like key presses, quitting the game, etc.) and updates the game state accordingly.

#### 2. **Event Handling:**

The loop checks if an event has occurred. This includes things like key presses and the game window closing.

##### a. **Quit Event:**

```python
if event.type == pygame.QUIT:
    # Handles quitting the game
    run = False
```

- **Purpose**: If the user closes the game window, it sets `run` to `False`, which will exit the game loop.

##### b. **Key Down Events:**

The game checks for specific key presses and triggers actions based on those inputs.

5. **Escape Key (`pygame.K_ESCAPE`) - Restart Game:**
    - When the player presses **Escape**, the game state is reset, and a new session begins.

```python
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
```

- **Purpose**: Resets the game variables and restarts a new session.

6. **Space Key (`pygame.K_SPACE`) - Player Hits (Draw a Card):**
    - When the player presses **Space**, they draw a card (Hit), and the AI also draws a card if needed.

```python
elif event.key == pygame.K_SPACE and session:
    # Hit: Player gets a card
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
```

- **Purpose**: Draw a card for the player and AI, check for win conditions (e.g., bust or blackjack).

7. **Enter Key (`pygame.K_RETURN`) - Player Passes (Ends Turn):**
    - When the player presses **Enter**, they pass their turn, and the AI takes its turn. The winner is determined after the AI’s action.

```python
elif (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN) and session:
    # Pass: Player ends their turn, AI gets a card
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
```

- **Purpose**: The player passes their turn, and the AI gets its next card. Afterward, it checks for the winner.

8. **Tab Key (`pygame.K_TAB`) - Toggle Spectator Mode:**
    - When the player presses **Tab**, they toggle between spectator mode and normal gameplay.

```python
elif event.key == pygame.K_TAB:
    # Switch to Spectator Mode
    spectate = not spectate
```

- **Purpose**: Allows the user to observe the game without interacting directly (AI actions only).

#### 3. **Screen Update:**

After processing the events and updating the game state, the screen is cleared, and the updated game state is rendered.

```python
# Screen update
screen.fill(background_color)
drawMenu()

pygame.display.flip()
clock.tick(60)
```

- **Purpose**:
    - `screen.fill(background_color)` clears the screen with a black background.
    - `drawMenu()` redraws the entire game UI (cards, scores, etc.).
    - `pygame.display.flip()` updates the display with the new content.
    - `clock.tick(60)` ensures the game runs at 60 frames per second.

#### 4. **End of Game Loop:**

The loop continues running until the `run` flag is set to `False`, which happens when the player closes the window or presses **Escape** to restart.
