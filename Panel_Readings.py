import csv
from datetime import datetime


# readings reference points
NOMINAL_LN = 115.0
NOMINAL_LL = 220.0
LN_TOLERANCE = .05 # lower end of the threshold
LL_TOLERANCE = .05

voltages = "user_input"
print(voltages)
# lets begin with checks

def in_range(value, nominal, tol):
    low = nominal * (1 - tol)
    high = nominal * (1 + tol)
    return low <= value <= high, (low, high)

# analyze the results

def analyze_panel(l1n, l2n, l1l2):
    issues = []

    ok_l1, (l1_low, l1_high) = in_range(l1n, NOMINAL_LN, LN_TOLERANCE)
    ok_l2, (l2_low, l2_high) = in_range(l2n, NOMINAL_LN, LN_TOLERANCE)
    ok_ll, (ll_low, ll_high) = in_range(l1l2, NOMINAL_LL, LL_TOLERANCE)

    if not ok_l1:
        issues.append(f"L1-N out of range ({l1n:.1f} V, expected {l1_low:.1f}-{l1_high:.1f})")
    if not ok_l2:
        issues.append(f"L2-N out of range ({l2n:.1f} V, expected {l2_low:.1f}-{l2_high:.1f})")
    if not ok_ll:
        issues.append(f"L1-L2 out of range ({l1l2:.1f} V, expected {ll_low:.1f}-{ll_high:.1f})")

# make sure you're balanced!

    imbalance = abs(l1n-l2n)
    if imbalance > 3: # volts
        issues.append(f"Leg imbalance: {imbalance:.1f} V between L1 and L2")

    return issues

# log readings

def log_reading(filename, panel_name, l1n, l2n, l1l2, issues):
    fieldnames = ["timestamp", "panel", "L1_N", "L2_N", "L1_L2", "issues"]
    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "panel": panel_name,
        "L1_N": l1n,
        "L2_N": l2n,
        "L1_L2": l1l2,
        "issues": " | ".join(issues) if issues else "OK"
    }

    try:
        with open(filename, "x", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(row)
    except FileExistsError:
        with open(filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(row)


# and we begin
def main():
    print("Panel Voltage Logger (120/240V single-phase)")
    panel = input("Panel name / location: ").strip()

    l1n = float(input("L1–N voltage: "))
    l2n = float(input("L2–N voltage: "))
    l1l2 = float(input("L1–L2 voltage: "))

    issues = analyze_panel(l1n, l2n, l1l2)

    if issues:
        print("\nIssues detected:")
        for i in issues:
            print(" -", i)
    else:
        print("\nAll voltages within set ranges.")

    log_reading("panel_readings.csv", panel, l1n, l2n, l1l2, issues)
    print("\nSaved to panel_readings.csv")

if __name__ == "__main__":
    main()