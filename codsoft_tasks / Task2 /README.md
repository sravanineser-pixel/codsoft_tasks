# Task 2 – Tic-Tac-Toe AI

## 📌 Project Overview

This project is a console-based Tic-Tac-Toe game developed using Python as part of the CodSoft internship.

The game allows a human player to play against an AI opponent. The AI uses the Minimax algorithm to make intelligent decisions and select the best possible move.

## 🎯 Objective

The objective of this task is to develop a Tic-Tac-Toe game where:

- The user can play against the computer.
- The computer makes intelligent moves.
- The game detects wins and draws.
- The AI uses the Minimax algorithm for decision-making.

## 🛠️ Technologies Used

- Python
- Functions
- Lists
- Loops
- Conditional statements
- Math module
- Minimax algorithm

## 🎮 Features

- Human vs AI gameplay
- Human player uses X
- AI player uses O
- Input validation
- Prevents already occupied positions
- Detects winning combinations
- Detects draws
- AI selects the best possible move

## 🧠 Minimax Algorithm

The Minimax algorithm is used to help the AI choose the best move.

The scoring system is:

- AI win → Positive score
- Human win → Negative score
- Draw → 0

The AI tries to maximize its score while considering the opponent's possible moves.

## 📋 Board Positions

The player selects a position from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
