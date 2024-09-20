import argparse
import os.path

from parsers.components_datasheets_parser import ComponentsDatasheetsParser


def main(folder_path, voltage, temperature):
    # Example functionality: print the received arguments
    print(f"Folder Path: {folder_path}")
    print(f"Voltage: {voltage}")
    print(f"Temperature: {temperature}")

    # Folder path validation:
    if not os.path.isdir(folder_path):
        raise Exception(f"Incorrect input: {folder_path} is not a folder path!")

    # You can add additional logic here to work with the folder and arguments
    ds_parser = ComponentsDatasheetsParser(folder_path)
    matching_components: list[str] = ds_parser.find_matching_components(voltage, temperature)
    print(f"The matching components: {matching_components}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some folder and parameters.")
    parser.add_argument("folder_path", type=str, help="Path to the folder")
    parser.add_argument("voltage", type=float, help="Voltage value")
    parser.add_argument("temperature", type=float, help="Temperature value")

    args = parser.parse_args()

    main(args.folder_path, args.voltage, args.temperature)
