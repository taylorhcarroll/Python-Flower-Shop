class Flower:
    def __init__(self, length, container):
        self.stem_length = length
        self.container = container


class IValentineFlower:
    def __init__(self):
        self.stem_length = 7
        self.container_refrigerated = False


class IMothersDayFlower:
    def __init__(self):
        self.stem_length = 4
        self.container_refrigerated = True


class Rose(IValentineFlower):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"{self.color} Rose"


class Lilly()
