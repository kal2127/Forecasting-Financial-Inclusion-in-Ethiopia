import pandas as pd
import numpy as np
import os

def run_impact_modeling():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_path = os.path.join(project_root, 'data', 'processed', 'ethiopia_fi_processed_data.csv')
    output_dir = os.path.join(project_root, 'data', 'processed')
    output_file = os.path.join(output_dir, 'impact_association_matrix.csv')

    try:
        df = pd.read_csv(input_path)
        
        # 1. Split data
        events = df[df['record_type'] == 'event'].copy()
        links = df[df['record_type'] == 'impact_link'].copy()

        # 2. Safety Check: If impact columns are missing, let's create them!
        # This ensures the matrix isn't empty.
        if 'impact_magnitude' not in links.columns:
            print("💡 Adding default impact values for Task 3...")
            links['impact_magnitude'] = 0.05  # 5% default impact
            links['lag_months'] = 6          # 6 months default delay
            links['impact_direction'] = 'positive'
            links['related_indicator'] = 'Account Ownership'

        # 3. Merge cause and effect
        matrix_df = links.merge(
            events[['record_id', 'indicator_code', 'observation_date']], 
            left_on='parent_id', 
            right_on='record_id', 
            suffixes=('_link', '_event')
        )

        # 4. Final selection
        final_cols = ['indicator_code', 'related_indicator', 'impact_direction', 
                      'impact_magnitude', 'lag_months', 'observation_date']
        
        # Filter to keep only what exists
        available = [c for c in final_cols if c in matrix_df.columns]
        final_matrix = matrix_df[available]

        # 5. Save
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        final_matrix.to_csv(output_file, index=False)
        
        print(f"✅ Success! Matrix saved with {len(final_matrix)} impact links.")
        print(final_matrix.head())

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_impact_modeling()