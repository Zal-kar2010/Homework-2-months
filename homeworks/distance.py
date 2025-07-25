class Distance:
    measures = {
        'мм': 0.001,
        'см': 0.01,
        'дм': 0.1,
        'м': 1.0,
        'км': 1000.0,
    }

    def __init__(self, value: float, measure: str):
        if measure not in Distance.measures:
            raise ValueError(f"Недопустимая мера: {measure}")
        self.value = value
        self.measure = measure

    def __str__(self):
        return f"{self.value} {self.measure}"

    def to_meters(self) -> float:
        return self.value * Distance.measures[self.measure]

    def _from_meters(self, meters: float):
        return Distance(meters / Distance.measures[self.measure], self.measure)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_m = self.to_meters() + other.to_meters()
        return self._from_meters(result_m)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_m = self.to_meters() - other.to_meters()
        if result_m < 0:
            raise ValueError("Результат вычитания не может быть отрицательным")
        return self._from_meters(result_m)

    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()