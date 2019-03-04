from FileReader import FileReader
from JsonBuilder import JsonBuilder

class Util:
    def __init__(self, file_name, output_file):
        self.file_reader = FileReader(file_name)
        self.json_builder = JsonBuilder()
        self.output_file = output_file

    def transform_to_json(self):
        parsed_values = self.file_reader.lines_parser()
        self.json_builder.write_json_file(self.output_file, parsed_values)
