from FileReader import FileReader
from JsonBuilder import JsonBuilder

class Util:
    def __init__(self, file_name):
        self.file_reader = FileReader(file_name)
        # self.json_builder = JsonBuilder()

    def parse_file(self):
        JsonBuilder(self.file_reader.lines_parser()).build_json()
