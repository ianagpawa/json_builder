from Project import Project
from itertools import zip_longest

class JsonBuilder:
    def __init__(self, values_arr):
        self.values_arr = values_arr

    def build_json(self):
        projects = []
        grouped_info = self.grouper(self.values_arr, 8, 'x')
        for proj in grouped_info:
            projects.append(self.create_project(proj))
        for p in projects:
            print(p)
        return projects


    def grouper(self, iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return list(zip_longest(*args, fillvalue=fillvalue))
    

    def create_project(self, values):
        return Project(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7]).details()

        

