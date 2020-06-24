
class Flower:
    def __init__(self, length, container):
        self.stem_length = length
        self.container_refridgerated = container

    def create_mothersDay(self):
        self.stem_length = 7
        self.container_refridgerated = False

    def create_valentine(self):
        self.stem_length = 4
        self.container_refridgerated = True


class Rose(Flower):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"{self.color} Rose"


class Lilly(Flower):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"{self.color} Lilly"
