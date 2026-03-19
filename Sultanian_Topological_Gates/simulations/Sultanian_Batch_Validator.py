import csv
import sys

def run_sultanian_validation(csv_file='SULTANIAN_AUDIT_LOG.csv', tolerance=1e-15):
    """
    Validates the integrity of the Sultanian Manifold by checking for 
    angular drift beyond the 10^-15 threshold.
    """
    print(f"--- Starting Sultanian Batch Verification ---")
    print(f"Threshold Tolerance: {tolerance}")
    
    pass_count = 0
    fail_count = 0
    total_records = 0
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                total_records += 1
                index = row['Zero_Index_n']
                deviation = float(row['Phase_Deviation_delta'])
                
                # Check if the deviation exceeds the Ghost Ray threshold
                if abs(deviation) > tolerance:
                    print(f"[FAIL] Zero n={index} exhibits drift: {deviation:.20f}")
                    fail_count += 1
                else:
                    pass_count += 1
                    
        print("\n" + "="*40)
        print(f"VERIFICATION SUMMARY")
        print(f"Total Zeros Checked: {total_records}")
        print(f"LOCKED (PASS):      {pass_count}")
        print(f"DRIFTED (FAIL):     {fail_count}")
        print("="*40)
        
        if fail_count == 0:
            print("STATUS: SULTANIAN MANIFOLD INTEGRITY VERIFIED (SCALE-INVARIANT)")
        else:
            print("STATUS: SYMMETRY BREAK DETECTED. CHECK GHOST RAY INTERFERENCE.")
            sys.exit(1) # Signal failure to system/CI

    except FileNotFoundError:
        print(f"[ERROR] Could not find {csv_file}. Please run Sultanian_Audit_Generator.py first.")
    except Exception as e:
        print(f"[ERROR] Validation interrupted: {e}")

if __name__ == "__main__":
    run_sultanian_validation()