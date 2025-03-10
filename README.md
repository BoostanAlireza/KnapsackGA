# Knapsack Genetic Algorithm Solver

This project implements a genetic algorithm to solve the 0/1 knapsack problem. Given a set of items with associated values and weights, the algorithm finds an optimal subset that maximizes total value while staying within a specified weight limit.

## Overview

The 0/1 knapsack problem is a classic optimization challenge where each item can either be included (1) or excluded (0) from the knapsack. This implementation uses a genetic algorithm—a nature-inspired optimization technique—to evolve a population of solutions over multiple generations, converging toward an optimal or near-optimal result.

Key features:
- Binary genome representation for item selection
- Roulette wheel selection for parent selection
- Single-point crossover and bit-flip mutation
- Early stopping if the best solution stagnates

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `random` module)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/[your-repo-name].git