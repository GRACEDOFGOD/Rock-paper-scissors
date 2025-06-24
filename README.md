# 🪨📄✂️ Intelligent Rock Paper Scissors Player

![Data Science Badge](https://img.shields.io/badge/Data%20Science-Strategic%20Modeling-blueviolet?style=flat-square)

---

## 📖 Project Overview

This project develops an intelligent Rock Paper Scissors (RPS) player designed to outperform baseline random strategies by leveraging data-driven pattern recognition, probabilistic modeling, and adaptive strategy selection.

Unlike a naive random choice bot, this player analyzes historical opponent moves to predict their next play and counter it effectively, aiming to win at least 60% of matches against diverse algorithmic opponents.

---

## 🎯 Objectives

- Demonstrate capability to **track sequential data** and extract meaningful patterns in adversarial settings.
- Build and implement **statistical and probabilistic models** for prediction and decision-making.
- Design an **adaptive algorithm** that evolves based on opponent behavior.
- Showcase skills in **state management**, **data structure manipulation**, and **algorithmic thinking**.
- Validate performance through testing against multiple opponents with varying strategies.

---

## 🛠️ Methodology

- **Stateful History Tracking:** Persist opponent’s move history across rounds to enable learning from sequence data.
- **N-gram Analysis & Markov Prediction:** Use frequency counts of recent move sequences to forecast next opponent move.
- **Counter-Move Logic:** Select winning moves based on predicted opponent behavior.
- **Strategy Switching:** Dynamically adapt tactics based on win rate and detected opponent patterns.
- **Randomization:** Introduce controlled randomness to prevent predictability.

---

## 🧠 Data Science Relevance

This project exemplifies critical data science skills:

- **Data Collection & Preprocessing:** Capturing and managing sequential data under strict performance constraints.
- **Feature Engineering:** Extracting predictive features from temporal move sequences.
- **Predictive Modeling:** Employing Markov chain-inspired techniques for sequence forecasting.
- **Algorithm Development:** Balancing exploitation and exploration in adversarial environments.
- **Evaluation & Iteration:** Using performance feedback loops to refine strategy.

These skills mirror real-world problems involving time series forecasting, user behavior prediction, and adversarial modeling.

---

## ⚙️ How to Run

1. Edit the `player` function inside `RPS.py` to implement your strategy.
2. Use `main.py` to run simulations against provided opponents:
   ```bash
   python main.py
