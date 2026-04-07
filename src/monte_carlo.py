import random
from typing import Dict

def simulate_crashes(days: int) -> Dict[str, float]:
    """
    Simulates startup's daily server failure rate over a given number of days.
    Theory: Crashing probability = 0.045 (4.5%)
    """
    total_crashes = 0
    failure_probability = 0.045
    
    for _ in range(days):
        if random.random() < failure_probability:
            total_crashes += 1
            
    simulated_prob = total_crashes / days if days > 0 else 0.0
    return {
        "days": days,
        "total_crashes": total_crashes,
        "simulated_probability": simulated_prob
    }

def run_monte_carlo_analysis():
    """
    Runs the simulation for 30, 1000, and 10000 days.
    """
    results = []
    for days in [30, 1000, 10000]:
        results.append(simulate_crashes(days))
    return results

if __name__ == "__main__":
    # Test call
    res = run_monte_carlo_analysis()
    for r in res:
        print(f"Days: {r['days']}, Simulated Prob: {r['simulated_probability']:.6f}")
