import json
from itertools import zip_longest
from Project import Project

class JsonBuilder:

    def build_json(self, values_arr):
        projects = []
        grouped_info = self.grouper(values_arr, 8, 'x')
        for proj in grouped_info:
            projects.append(self.create_project(proj))
        return projects


    def write_json_file(self, file_name, values_arr):
        with open(file_name, 'w') as outfile:
            json.dump(self.build_json(values_arr), outfile)


    def grouper(self, iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return list(zip_longest(*args, fillvalue=fillvalue))
    

    def create_project(self, values):
        return Project(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7]).details()

        

