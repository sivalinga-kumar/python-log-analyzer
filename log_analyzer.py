from datetime import datetime

class LogAnalyzer:
    def __init__(self, filename="server.log"):
        self.filename = filename

    def log_event(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        with open(self.filename, "a") as file:
            file.write(entry)

    def analyze_logs(self):
        counts = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    for level in ["INFO", "WARNING", "ERROR"]:
                        if f"[{level}]" in line:
                            if level in counts:
                                counts[level] = counts[level] + 1
                            else:
                                counts[level] = 1
            return counts
        except FileNotFoundError:
            return {}

    def export_summary(self, report_filename="report.txt"):
        counts = self.analyze_logs()
        total_events = sum(counts.values())
        with open(report_filename, "w") as file:
            file.write("=== SYSTEM REPORT ===\n")
            file.write(f"Total Events: {total_events}\n")
            for level, count in counts.items():
                file.write(f"{level}: {count}\n")


if __name__ == "__main__":
    analyzer = LogAnalyzer("server.log")

    analyzer.log_event("INFO", "Server started on port 8000")
    analyzer.log_event("WARNING", "High memory usage detected")
    analyzer.log_event("ERROR", "Database connection lost")
    analyzer.log_event("ERROR", "Payment gateway timed out")

    print("Analysis Result:", analyzer.analyze_logs())
    analyzer.export_summary("report.txt")
    print("Report successfully saved to report.txt")
