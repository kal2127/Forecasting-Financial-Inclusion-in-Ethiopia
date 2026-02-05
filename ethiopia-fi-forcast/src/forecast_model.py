import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def run_forecast_analysis():
    # --- 1. PATH SETUP ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Define folder for figures
    figures_dir = os.path.join(project_root, 'reports', 'figures')
    if not os.path.exists(figures_dir):
        os.makedirs(figures_dir)
        print(f"📁 Created folder: {figures_dir}")

    # --- 2. DATA SETUP ---
    # --- 2. DATA SETUP (CORRECTED) ---
    years_hist = [2011, 2014, 2017, 2021, 2024]
    values_hist = [14, 22, 35, 46, 49] # Note: updated first point to match actual Findex 2011
    
    # We start future lines at 2024 so they connect to the history line
    years_future = [2024, 2025, 2026, 2027]
    
    # Updated these to match your specific forecast CSV results!
    # Pessimistic: Stays at 49%
    pessimistic = [49, 49, 49, 49.0] 
    
    # Base Case: Smooth path to 59.65
    base = [49, 52.5, 56.1, 59.65] 
    
    # Optimistic: Smooth path to 62.41
    optimistic = [49, 53.4, 57.9, 62.41]

    # --- 3. PLOTTING ---
    plt.figure(figsize=(10, 6))
    
    # Plot Historical
    plt.plot(years_hist, values_hist, marker='o', color='black', label='Historical (Findex)', linewidth=2)
    
    # Plot Scenarios
    plt.plot(years_future, pessimistic, '--', color='red', label='Pessimistic Scenario')
    plt.plot(years_future, base, '--', color='orange', label='Base Case (Trend + Event)')
    plt.plot(years_future, optimistic, '--', color='green', label='Optimistic Scenario')

    # Formatting
    plt.title("Ethiopia Financial Inclusion Forecast (2025-2027)", fontsize=14, fontweight='bold')
    plt.xlabel("Year")
    plt.ylabel("Account Ownership (%)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()

    # --- 4. SAVE TO REPORTS/FIGURES ---
    save_path = os.path.join(figures_dir, 'inclusion_forecast_2027.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"📊 Success! Graph saved to: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    run_forecast_analysis()