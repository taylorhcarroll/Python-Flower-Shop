from arrangement import Arrangement

class ValentinesDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.stem_length == 7:
                self.flowers.append(flower)
            else:
                raise AttributeError
        except AttributeError:
            print(f"{flower} doesn\'t belong in this arrangement.")