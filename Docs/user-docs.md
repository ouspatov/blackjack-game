## Introduction

Welcome to the **Blackjack Game**! This game simulates the classic **Blackjack** card game, where you compete against an AI. Your goal is to get a hand value as close to 21 as possible, without going over. If your hand exceeds 21, you lose. The game also features a simple yet engaging user interface built with **Pygame**.

### Game Controls

- **[Enter]**: Pass your turn. The AI will then take its turn.
- **[Space]**: Draw a card (Hit). You can keep pressing this to draw more cards.
- **[Tab]**: Toggle **Spectator Mode**. In this mode, you can only watch the game as the AI takes actions.
- **[Esc]**: Restart the game from the beginning.

### Gameplay Rules

1. **Objective**: The goal of Blackjack is to get a hand value as close to 21 as possible, but not over. You compete against the AI, and the winner is determined by who has the highest hand value without exceeding 21.
2. **Card Values**:
    - **Aces (A)** can be either 1 or 11 depending on the value of the hand.
    - **Number Cards (2-10)** are worth their respective values.
    - **Face Cards (Jack, Queen, King)** are worth 10.
    - The total value of your hand is the sum of the values of all the cards in it.
3. **Gameplay Flow**:
    - Both you and the AI are dealt two cards at the beginning of the game.
    - **You** can choose to either **"hit"** (draw another card) or **"stand"** (end your turn).
    - The **AI** will automatically draw cards if its hand value is less than 18, but will stop drawing if it has 17 or more.
4. **Winning Conditions**:
    - If your hand value is **greater than 21**, you **bust** and lose the game.
    - If your hand value is **greater than the AI's hand**, you win.
    - If both you and the AI have the same hand value, the game is a **tie**.
    - If the AI busts but you do not, you win.
    - If you bust and the AI does not, the AI wins.

### Aces in Blackjack

In Blackjack, the **Ace** is a special card because it can be worth either **1** or **11**, depending on the situation. This is crucial to ensure the best possible hand value. Here's how the Ace works in the game:

1. If you have an Ace in your hand, and the sum of the rest of your cards is **less than or equal to 10**, the Ace is worth **11** (making it a more powerful card).
2. If adding 11 to the hand would cause the total value to exceed 21 (i.e., **busting**), the Ace will be worth 1 instead.

### Game Display

The game interface is divided into several key sections:

1. **Player's Hand**: The cards you have drawn, along with the total value of your hand.
2. **AI's Hand**: The AI's cards, with the second card hidden until the game is over.
3. **Game Rules**: Instructions are displayed at the top-right corner, including control keys.
4. **Current Score**: Displays the total value of both your hand and the AI's hand.
5. **Winner Display**: After the game ends, it will show the winner and any game results (e.g., Player Wins, AI Wins, Tied, etc.).
