import os

from parsers.datasheet_parser import DatasheetParser
from utils import utils


# For each component in folder - create a DatasheetParser
# Returns all the components that match (voltage, temp): `find_matching_components`
class ComponentsDatasheetsParser:
    def __init__(self, folder_path: str):
        self.file_paths_: list[str] = utils.get_file_paths_from_folder(folder_path)  # extract file paths from folder
        self.component_to_datasheet_parser_: dict[str, DatasheetParser] = {}
        self.parse_ranges_to_all_files()  # parse all the files
        for comp, dsp in self.component_to_datasheet_parser_.items():
            print(f"{comp}: {dsp.to_string()}")

    def parse_ranges_to_all_files(self) -> None:
        # Iterates all file paths and creates a DatasheetParser for each one
        for file_path in self.file_paths_:
            datasheet_parser = DatasheetParser(file_path)
            file_name: str = os.path.basename(file_path)  # The name of the file with extenstion (.txt)
            component: str = file_name[:-4]  # Extract the name of the component
            self.component_to_datasheet_parser_[component] = datasheet_parser

    def find_matching_components(self, voltage: float, temp: float) -> list[str]:
        matching_components: list[str] = []
        # Iterate all components and find matches to given voltage and temp:
        for component, ds_parser in self.component_to_datasheet_parser_.items():
            if ds_parser.does_component_match_requirements(voltage, temp):
                matching_components.append(component)
        return matching_components
