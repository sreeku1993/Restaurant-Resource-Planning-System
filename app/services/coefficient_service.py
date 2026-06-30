import json


class CoefficientService:

    def __init__(self):

        self.file_path = "data/coefficients.json"

    def load(self):

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save(self, coefficients):

        with open(self.file_path, "w") as file:
            json.dump(coefficients,file,indent=4)