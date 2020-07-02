from arrangement import Arrangement, ValentinesDayArrangement, MothersDayArrangement
from flowers import Flower, Rose, Lilly

# if __name__ == "__main__":
#     for_kelly = ValentinesDayArrangement()
#     red_rose = Rose("Red")
#     red_rose.create_valentine()
#     for_kelly.enhance(red_rose)

#     from_penny = MothersDayArrangement()
#     white_lilly = Lilly("White", 7, False)
#     from_penny.enhance(white_lilly)

#     for flower in for_kelly.flowers:
#         print(flower)


red_rose = Rose(10, False, "red")
pink_rose = Rose(7, True, "pink")
red_rose.create_valentine()
pink_rose.create_valentine()

print(red_rose.stem_length, red_rose.container_refridgerated)

for_kelly = ValentinesDayArrangement("Love")
for_kelly.enhance(red_rose)
for_kelly.enhance(pink_rose)

from_penny = MothersDayArrangement("mother's day")
blue_lilly = Lilly(6, True, "blue")
white_lilly = Lilly(10, True, "white")
blue_lilly.create_mothersDay()
white_lilly.create_mothersDay()
from_penny.enhance(blue_lilly)
from_penny.enhance(white_lilly)

# print("This is the arrangement for Kelly from me.")
# for flower in for_kelly.flowers:
#     print(flower)

# print("This is the arrangement for Kelly from me.")
# for flower in from_penny.flowers:
#     print(flower)
