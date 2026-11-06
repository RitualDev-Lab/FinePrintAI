"""
Example: Auditing a legal agreement and generating redline amendments using FinePrint AI.
Requires: pip install fineprint
"""
import sys
from pathlib import Path
from fineprint import ContractScanner

def audit_document(file_path: str):
    scanner = ContractScanner()
    
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} not found.")
        sys.exit(1)
        
    contract_text = path.read_text(encoding="utf-8")
    
    print(f"📄 Scanning '{path.name}' with 60+ legal risk signatures...\n")
    report = scanner.analyze_text(contract_text)
    
    print(f"Overall Risk Grade: {report.get('grade', 'C')}")
    print(f"Risk Score: {report.get('risk_score', 0)} / 100")
    print(f"Flagged Clauses: {len(report.get('violations', []))}\n")
    
    for idx, v in enumerate(report.get("violations", []), 1):
        print(f"[{idx}] {v.get('category')} — Severity: {v.get('severity')}")
        print(f"    Problem: {v.get('explanation')}")
        print(f"    Suggested Redline: {v.get('recommended_clause')}\n")

if __name__ == "__main__":
    sample_path = Path(__file__).parent / "sample_vendor_agreement.md"
    audit_document(str(sample_path))
