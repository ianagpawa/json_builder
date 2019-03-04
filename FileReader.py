class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        

    def parse_text_file(self):
        """
        Parses text file into array of line items.
        
        @type file_name: str
        @param file_name: Name of text file.
        @rtype: array
        @return Array of line times.
        """
        file = open(self.file_name, "r")
        return file.read().splitlines()


    def lines_parser(self):
        lines = []
        for line in self.parse_text_file():
            value = self.line_parser(line)
            if value:
                lines.append(value)
        return lines


    def line_parser(self, line):
        line = line.replace("'", '"')
        split_line = line.split('"')
        return split_line[1] if len(split_line) > 2 else None
    