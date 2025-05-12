from abc import ABC, abstractmethod

# Abstract class
class ReportGenerator(ABC):
    def generate(self):
        self.fetch_data()
        self.analyze_data()
        self.format_report()
        self.print_report()

    def fetch_data(self):
        print("Fetching data from database...")

    def analyze_data(self):
        print("Analyzing the data...")

    @abstractmethod
    def format_report(self):
        pass

    def print_report(self):
        print("Printing the report...")


# Concrete class
class CSVReport(ReportGenerator):
    def format_report(self):
        print("Formatting report as CSV...")


class PDFReport(ReportGenerator):
    def format_report(self):
        print("Formatting report as PDF...")


# Usage
csv_report = CSVReport()
pdf_report = PDFReport()

csv_report.generate()
pdf_report.generate()