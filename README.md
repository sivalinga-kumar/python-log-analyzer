# Python Log Analyzer

A simple, class-based Python tool to log system events, parse log files, and generate clean summary reports.

## What It Does
- Logs events with timestamps to `server.log`.
- Reads and parses logs line-by-line using standard Python file handling (`with open`).
- Counts occurrences of `INFO`, `WARNING`, and `ERROR` entries using a dictionary.
- Catches missing file errors (`FileNotFoundError`) safely so the script doesn't crash.
- Exports a quick health summary to `report.txt`.

## Files
- `log_analyzer.py` — The core script containing the `LogAnalyzer` class.
- `server.log` — Raw text file where events are appended.
- `report.txt` — Generated summary report.

## How to Run

Run the script from your terminal or command prompt:

```bash
python log_analyzer.py
```

## Sample Output

### Raw Log (`server.log`)
```text
[2026-10-26 20:15:10] [INFO] Server started on port 8000
[2026-10-26 20:16:22] [WARNING] High memory usage detected
[2026-10-26 20:17:45] [ERROR] Database connection lost
[2026-10-26 20:18:05] [ERROR] Payment gateway timed out
```

### Summary Report (`report.txt`)
```text
=== SYSTEM REPORT ===
Total Events: 4
INFO: 1
WARNING: 1
ERROR: 2
```
