from flowers import Flower


class Arrangement:

    def __init__(self):
        self.__flowers = []
# enhance means you are adding a flower to this arrangement,
# this is not meant to imply you are enhancing an existing flower in this arrangement

    def enhance(self, flower):
        self.__flowers.append(flower)

    # @property  # The flowers getter
    # def flowers(self):
    #     try:
    #         return self.__flowers  # Note there are 2 underscores here
    #     except AttributeError:
    #         return "Something went wrong here??"


class ValentinesDayArrangement(Arrangement):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme

    def enhance(self, flower):
        try:
            if flower.stem_length == 7:
                self.flowers.add(flower)
        except AttributeError as ex:
            print(f'{flower} cannot be added to {self.theme} arrangement')


class MothersDayArrangement(Arrangement):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme

    def enhance(self, flower):
        try:
            if flower.stem_length == 4 and flower.container_refridgerated == False:
                self.flowers.add(flower)
        except AttributeError as ex:
            print(f'{flower} cannot be added to {self}')
