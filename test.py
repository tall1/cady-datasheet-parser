import re


def parse_voltage_ranges(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex pattern to match voltage ranges like '2.4V to 5.1V'
    voltage_pattern = r'\d*\.?\d+\s?v\s+to\s+\d*\.?\d+\s?v'

    # Find all matches for voltage and temperature ranges
    voltage_ranges = re.findall(voltage_pattern, content, re.IGNORECASE)
    voltage_ranges_tuples = []
    for vr in voltage_ranges:
        matches = re.findall(r'\d+(?:\.\d+)?', vr)
        voltage_ranges_tuples.append(tuple(map(float, matches)))
    return voltage_ranges_tuples


def parse_temperature_ranges(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    en_dash_symb: str = "\u2013"  # for the big '-'
    deg_symb: str = "\u00B0"  # for the deg symbol
    temperature_pattern = rf'[+-{en_dash_symb}]?\d+\s*[{deg_symb}]?c\s*to\s*[+-{en_dash_symb}]?\d+\s*[{deg_symb}]?c'

    # Find all matches for voltage and temperature ranges
    temperature_ranges = re.findall(temperature_pattern, content, re.IGNORECASE)
    temperature_ranges_tuples = []
    for tr in temperature_ranges:
        matches = re.findall(rf'[+-{en_dash_symb}]?\d+', tr)
        matches = [match.replace(en_dash_symb, '-') for match in matches]  # replace en dash with '-'
        temperature_ranges_tuples.append(tuple(map(float, matches)))
    return temperature_ranges_tuples


if __name__ == "__main__":
    # Example usage:
    file_path = r'C:\Users\USER\PycharmProjects\CadyExam\example-data\task_example_files\INA225-Q_7212.txt'
    voltage_ranges = parse_voltage_ranges(file_path)
    temperature_ranges = parse_temperature_ranges(file_path)
    print("Voltage Ranges Found:")
    for vr in voltage_ranges:
        print(str(vr))
    print("Temperature Ranges Found:")
    for trng in temperature_ranges:
        print(str(trng))
