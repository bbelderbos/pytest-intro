class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = int(year)
        self._mileage = []

    def __str__(self):
        return f"Car: {self.model} ({self.year})"

    def add_mileage(self, miles):
        self._mileage.append(miles)

    @property
    def miles_driven(self):
        return sum(self._mileage)

    @property
    def mileage_report(self):
        print("\n".join(str(i) for i in self._mileage))
        print("---")
        print(self.miles_driven)

    @classmethod
    def from_string(cls, car_string):
        car_args = car_string.split()
        return cls(*car_args)

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year
