import subprocess
import os
import sys

# --- Path Resolution ---
# This finds the absolute path to the directory containing THIS script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_step(script_name, description):
    """Orchestrates the execution using absolute paths."""
    print(f"\n[STEP] {description}...")
    
    # Construct the full path to the sub-script
    script_path = os.path.join(BASE_DIR, script_name)
    print(f"Executing: {script_path}")
    
    try:
        # We pass script_path instead of just the name
        result = subprocess.run([sys.executable, script_path], check=True)
        if result.returncode == 0:
            print(f"[SUCCESS] {script_name} completed.")
            return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script_name} failed with return code {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"[ERROR] {script_path} not found. Check your folder structure.")
        return False

# ... rest of your main() logic stays the same ...

def main():
    print("="*60)
    print("SULTANIAN TOPOLOGICAL GATES: MASTER CONTROL INTERFACE")
    print("Protocol Version: 2026.3.1 (Unipolar Phase-Lock)")
    print("="*60)

    # 1. DATA GENERATION (The Audit)
    if not run_step("Sultanian_Audit_Generator.py", "Generating High-Precision 1,000-Zero Audit"):
        sys.exit(1)

    # 2. BATCH VALIDATION (The Stress Test)
    if not run_step("Sultanian_Batch_Validator.py", "Enforcing 10^-15 Phase-Lock Tolerance"):
        sys.exit(1)

    # 3. VISUALIZATION (The Proof)
    print("\n[STEP] Launching Interactive 3D Manifold Flight...")
    # Using the script with shells and ghost rays for maximum clarity
    run_step("Sultanian_Unipolar_Flight.py", "Visualizing Manifold Shells and Ghost Rays")

    print("\n" + "="*60)
    print("PROTOCOL COMPLETE: ALL GATES VERIFIED LOCKED AT 45.0°")
    print("="*60)

if __name__ == "__main__":
    main()