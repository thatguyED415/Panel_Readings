# Panel_Readings
A simple command-line tool for electricians to record and verify panel voltage readings.  
Designed for single-phase 120/240 V systems but easy to adapt for other nominal values.

---

## Features
- Enter L1–N, L2–N, and L1–L2 readings manually  
- Checks voltage ranges (±5 %)  
- Detects leg imbalance  
- Logs readings with timestamps to `panel_readings.csv`

---

## Usage
1. Clone or download the repo.  
2. (Optional) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate