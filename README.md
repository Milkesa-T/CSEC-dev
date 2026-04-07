# CSEC-dev Project Collection

# Statistical Engineering & Simulation Assessment

## Project Overview
This project is a high-performance, pure-Python statistical engine designed to analyze raw numerical data and simulate probabilistic scenarios using the **Monte Carlo method**. Built from scratch using only Python's standard libraries, it demonstrates foundational concepts in data engineering, statistical distribution, and the **Law of Large Numbers (LLN)**.

---

## Technical Features
- **StatEngine Core**: Handles mean, median, multimodal modes, variance (population/sample), and standard deviation.
- **Monte Carlo Simulator**: Models startup server failure rates to compare theoretical vs. simulated probabilities.
- **Outlier Detection**: Identifies performance or salary anomalies using standard deviation thresholds.
- **Robust Error Handling**: Pre-cleans data (handles `None`, strings, mixed types) and prevents division by zero in empty datasets.

---

## Mathematical Logic

### 1. Variance Calculation ($s^2$ vs $\sigma^2$)
We implement logic for both **Population Variance** ($\sigma^2$) and **Sample Variance** ($s^2$):
- **Population Variance**:  $\sigma^2 = \frac{\sum (x - \mu)^2}{N}$  (Used when analyzing the entire group).
- **Sample Variance (Bessel's Correction)**: $s^2 = \frac{\sum (x - \bar{x})^2}{n - 1}$
    - *Note*: We use $n-1$ to correct for the bias in the estimation of the population variance, ensuring a more accurate spread estimation from a subset of data.

### 2. Median (Even vs. Odd constraint)
The median logic ensures accuracy across different dataset sizes:
1.  **Sorted Dataset**: First, the list is sorted in ascending order.
2.  **Odd Length**: Returns the exact middle element at index $n // 2$.
3.  **Even Length**: Calculates the mid-point between the two central values: $\frac{data[n//2 - 1] + data[n//2]}{2}$.

---

## Setup & Running the Code

### Prerequisites
- Python 3.8+ (No external dependencies required)

### Execution
To run the full analysis and simulation:
```bash
python main.py
```

---

## Testing & Engineering Standards
We maintain high code quality standards using Python’s built-in `unittest` framework.

### Run Tests:
```bash
python -m unittest tests/test_stat_engine.py
```

---

## Acceptance Criteria Checklist
- [x] **Pure Python Implementation**: No `numpy`, `pandas`, or external libs used.
- [x] **Multimodal Mode Support**: Returns a list of all modes or a message for unique values.
- [x] **Bessel’s Correction**: Accurately differentiates between Sample and Population variance.
- [x] **Robust Data Cleaning**: Gracefully handles mixed types and empty lists (ZeroDivisionError prevention).
- [x] **Monte Carlo Validation**: Proves the Law of Large Numbers through large-scale simulation.
- [x] **Project Structure**: Follows standard `/src`, `/tests`, and `/data` folder architecture.

---

## Statistical Interpretation (Part 2)

### The Law of Large Numbers (LLN)
The simulation demonstrates that as the number of "trials" (days) increases, the **simulated average** approaches the **theoretical expected value** (4.5%).

**Why is it dangerous to predict a budget based on a 30-day "trial"?**
In small samples, local variance (noise) is extreme. A startup seeing only 0 crashes in 30 days might think their servers are "perfect" and under-budget for maintenance. Conversely, a 10% crash rate in a single month might cause a panic. The LLN proves that you need large datasets to capture the true underlying risk; short-term "luck" is a poor metric for long-term fiscal planning.
