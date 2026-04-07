import json
import os
from src.stat_engine import StatEngine
from src.monte_carlo import run_monte_carlo_analysis

def load_data(file_path):
    """
    Loads JSON data from the specified path.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def format_results(results):
    """
    Neatly prints results for the user.
    """
    print("="*60)
    print("     STATISTICAL ENGINEERING & SIMULATION ASSESSMENT")
    print("="*60)
    
    print("\n--- [PART 1 & 2: STATISTICAL SALARY ANALYSIS] ---")
    print(f"Data Source: data/sample_salaries.json")
    
    engine = StatEngine(results['salary_data'])
    print(f"Dataset Size       : {len(results['salary_data'])}")
    print(f"Arithmetic Mean    : ${engine.get_mean():,.2f}")
    print(f"Median Salary      : ${engine.get_median():,.2f}")
    print(f"Mode(s)            : {engine.get_mode()}")
    print(f"Sample Variance    : {engine.get_variance(is_sample=True):,.2f}")
    print(f"Sample Std Dev     : ${engine.get_standard_deviation(is_sample=True):,.2f}")
    print(f"Population Std Dev : ${engine.get_standard_deviation(is_sample=False):,.2f}")
    
    outliers = engine.get_outliers(threshold=2)
    print(f"\n[Outlier Detection (Threshold=2 SD)]")
    print(f"Number of Outliers : {len(outliers)}")
    print(f"Outlier Values     : {sorted([f'${x:,.2f}' for x in outliers])}")
    
    print("\n\n--- [PART 3: MONTE CARLO - SERVER FAILURE SIMULATION] ---")
    print("Theoretical Failure Rate: 4.5% (0.045)")
    mc_results = results['mc_sims']
    print(f"{'Days':<10} | {'Total Crashes':<15} | {'Simulated Prob':<15}")
    print("-" * 45)
    for res in mc_results:
        print(f"{res['days']:<10} | {res['total_crashes']:<15} | {res['simulated_probability']:.6f}")

    print("\n--- [INTERPRETATION: LAW OF LARGE NUMBERS] ---")
    print("The Law of Large Numbers (LLN) states that as a sample size increases,")
    print("the sample mean approaches the 'expected value' (theoretical probability).")
    print("\nSimulation Insights:")
    print("- 30 Days: Often varies significantly from 0.045 due to small sample size.")
    print("- 10,000 Days: Closely matches the 0.045 (4.5%) threshold.")
    print("\nWARNING FOR STARTUPS:")
    print("Predicting a yearly budget based on a small trial (e.g., 30 days) is dangerous.")
    print("If failure rates spike early by chance, you might over-allocate budget and kill your cashflow.")
    print("Conversely, an 'unusually lucky' month can lead to disastrous under-budgeting if the rate stabilizes higher over time.")
    print("="*60 + "\n")

def main():
    try:
        # Load salary data
        salary_data = load_data('data/sample_salaries.json')
        
        # Run Monte Carlo simulation
        mc_sims = run_monte_carlo_analysis()
        
        # Wrap results
        full_results = {
            'salary_data': salary_data,
            'mc_sims': mc_sims
        }
        
        # Format and display
        format_results(full_results)
        
    except Exception as e:
        print(f"Error executing assessment: {e}")

if __name__ == "__main__":
    main()
