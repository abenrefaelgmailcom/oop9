

'''
============== without enum

EASY = "easy"
MEDIUM = "medium"
HARD = "hard"

level = MEDIUM

if level == "medium":
    print("You chose medium difficulty.")

# 1 wrong typing
if level == "MEDIUM":
    pass

# 2 no auto-complete
if level == "med....":
    pass

# 3 no choices presented
if level == "....":
    pass
'''

from enum import Enum

class Levels(Enum):
    EASY = 1,
    MEDIUM = 2,
    HARD = 3,
    NIGHTMARE = 4

level = Levels.HARD
if level == Levels.MEDIUM:
    print('medium')
else:
    print('not medium')

def play_game(play_level : Levels) -> None:
    print(play_level)
    if play_level == Levels.HARD:
        print('wow !')

play_game(Levels.HARD)  # returns str

print(Levels.HARD)

if level.value[0] >= Levels.MEDIUM.value[0]:
    print('harder equal to medium')
else:
    print('lower than medium')

for level in Levels:
    print(level.name, level.value)

print(Levels(4))
print(Levels['HARD'])

'''
create days in week:
SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
print all of the days
input a day from the user, check if it is thursday: print yes/no
input a number from the user and print the day
input a day from the user, check if it is after tuesday
'''