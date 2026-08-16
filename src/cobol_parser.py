# cobol_parser.py — Parse COBOL source into structured data
# Extracts IDENTIFICATION, DATA, PROCEDURE, ENVIRONMENT divisions

import re

class COBOLParser:
    """Parses COBOL source code into structured divisions"""
    
    def __init__(self):
        self.divisions = {
            "IDENTIFICATION": {},
            "DATA": {"working_storage": [], "linkage": [], "file_section": []},
            "PROCEDURE": [],
            "ENVIRONMENT": {},
        }
    
    def parse(self, source: str) -> dict:
        """Parse COBOL source into divisions"""
        lines = source.split('\n')
        current_division = None
        current_section = None
        
        for line in lines:
            stripped = line.strip()
            
            # Detect divisions
            if 'IDENTIFICATION DIVISION' in stripped.upper():
                current_division = "IDENTIFICATION"
            elif 'DATA DIVISION' in stripped.upper():
                current_division = "DATA"
            elif 'PROCEDURE DIVISION' in stripped.upper():
                current_division = "PROCEDURE"
            elif 'ENVIRONMENT DIVISION' in stripped.upper():
                current_division = "ENVIRONMENT"
            
            # Detect sections within DATA division
            elif current_division == "DATA":
                if 'WORKING-STORAGE SECTION' in stripped.upper():
                    current_section = "working_storage"
                elif 'LINKAGE SECTION' in stripped.upper():
                    current_section = "linkage"
                elif 'FILE SECTION' in stripped.upper():
                    current_section = "file_section"
            
            # Collect data
            if current_division == "IDENTIFICATION":
                if 'PROGRAM-ID' in stripped.upper():
                    parts = stripped.split('.')
                    self.divisions["IDENTIFICATION"]["program_id"] = parts[1].strip() if len(parts) > 1 else parts[0].strip()
            elif current_division == "DATA":
                if current_section and stripped and not stripped.startswith('*'):
                    self.divisions["DATA"][current_section].append(stripped)
            elif current_division == "PROCEDURE":
                if stripped and not stripped.startswith('*'):
                    self.divisions["PROCEDURE"].append(stripped)
        
        return self.divisions
    
    def extract_business_rules(self) -> list:
        """Extract business logic from PROCEDURE division"""
        rules = []
        
        for line in self.divisions["PROCEDURE"]:
            # IF/ELSE conditions
            if 'IF' in line.upper() and 'THEN' in line.upper():
                rules.append(line.strip())
            # COMPUTE statements
            elif 'COMPUTE' in line.upper():
                rules.append(line.strip())
            # MOVE statements
            elif 'MOVE' in line.upper() and 'TO' in line.upper():
                rules.append(line.strip())
        
        return rules
    
    def translate_to_python(self) -> str:
        """Translate extracted business rules to Python"""
        python_lines = []
        
        for rule in self.extract_business_rules():
            # Translate IF condition
            if 'IF' in rule.upper():
                condition = rule.upper().replace('IF', '').replace('THEN', ':')
                python_lines.append(f"if {condition.lower()}")
            # Translate COMPUTE
            elif 'COMPUTE' in rule.upper():
                expr = rule.upper().replace('COMPUTE', '').strip()
                python_lines.append(f"result = {expr.lower()}")
            # Translate MOVE
            elif 'MOVE' in rule.upper():
                move_parts = rule.upper().replace('MOVE', '').split('TO')
                if len(move_parts) == 2:
                    python_lines.append(f"{move_parts[1].strip().lower().replace('.', '')} = {move_parts[0].strip().lower()}")
        
        return '\n'.join(python_lines)
