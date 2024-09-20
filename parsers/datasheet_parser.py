import re
from typing import Optional

VOLTAGE: str = 'v'
TEMPERATURE: str = 't'


# Given datasheet path, parses the file and holds the voltage and temp ranges
# If more than one non-equal range - returns None
class DatasheetParser:
    def __init__(self, file_path):
        self.file_path_: str = file_path
        self.parsed_voltage_range_: Optional[tuple[float, float]] = None
        self.parsed_temp_range_: Optional[tuple[float, float]] = None
        self.parse_ranges()

    def does_component_match_requirements(self, voltage: float, temp: float) -> bool:
        # Checks if component fits the requirements:

        if self.parsed_voltage_range_ and self.parsed_temp_range_:
            # Check matching to voltage:
            matched_to_v_range: bool = self.parsed_voltage_range_[0] <= voltage <= self.parsed_voltage_range_[1]
            # Check matching to temperature:
            matched_to_tmp_range: bool = self.parsed_temp_range_[0] <= temp <= self.parsed_temp_range_[1]
            return matched_to_v_range and matched_to_tmp_range

        # If voltage range or temp is None then return False
        return False

    def parse_ranges(self) -> None:
        self.parse_voltage_ranges()
        self.parse_temperature_ranges()

    def parse_voltage_ranges(self) -> None:
        # Parses the file and find all the voltage ranges:
        with open(file=self.file_path_, mode='r', encoding="utf-8", errors='ignore') as file:
            content = file.read()

        # Regex pattern to match voltage ranges like '2.4V to 5.1V' or '2 v to 5.1v' etc.
        voltage_pattern = r'\??\d*\.?\d+\s?v?\s+to\s+\??\d*\.?\d+\s*v'

        # Find all matches for voltage and temperature ranges (ignores the case)
        voltage_ranges = re.findall(voltage_pattern, content, re.IGNORECASE)
        parsed_voltage_ranges_ = []
        for vr in voltage_ranges:
            matches = re.findall(r'\d+(?:\.\d+)?', vr)  # Find the two numbers (float or int) in the matched strings
            parsed_voltage_ranges_.append(tuple(map(float, matches)))  # convert the numbers to floats

        # Check if only one range found, else - return None:
        only_one_range: bool = len(set(parsed_voltage_ranges_)) == 1
        self.parsed_voltage_range_ = parsed_voltage_ranges_[0] if only_one_range else None

    def parse_temperature_ranges(self) -> None:
        # Parses the file and find all the temp ranges:
        with open(self.file_path_, 'r') as file:
            content = file.read()

        # Regex pattern to match voltage ranges like '–40°C to +105°C'
        en_dash_symb: str = "\u2013"  # for the big '-'
        deg_symb: str = "\u00B0"  # for the deg symbol
        temperature_pattern = rf'[+-{en_dash_symb}]?\d+\s*[{deg_symb}]?c\s*to\s*[+-{en_dash_symb}]?\d+\s*[{deg_symb}]?c'

        # Find all matches for voltage and temperature ranges (ignores the case)
        temperature_ranges = re.findall(temperature_pattern, content, re.IGNORECASE)
        parsed_temp_ranges_ = []
        for tr in temperature_ranges:
            matches = re.findall(rf'[+-{en_dash_symb}]?\d+', tr)  # Find the two numbers (only integers), starts with +/- or nothing
            matches = [match.replace(en_dash_symb, '-') for match in matches]  # replace en dash with '-'
            parsed_temp_ranges_.append(tuple(map(float, matches)))  # convert to floats

        # Check if only one range found, else - return None:
        only_one_range: bool = len(set(parsed_temp_ranges_)) == 1
        self.parsed_temp_range_ = parsed_temp_ranges_[0] if only_one_range else None

    def to_string(self):
        return f"voltage: {self.parsed_voltage_range_}, temp: {self.parsed_temp_range_}"
