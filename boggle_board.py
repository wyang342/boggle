import random
import string


class BoggleBoard:
    dice_faces = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY",
                  "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]

    def __init__(self):
        for i in range(4):
            print("____")

    def shake(self):
        for i, die in enumerate(self.dice_faces):
            chosen_letter = random.choice(self.dice_faces[i])
            if chosen_letter == "Q":
                print("Qu", end=" ")
            else:
                print(chosen_letter, end="  ")
            if i % 4 == 3:
                print()


board1 = BoggleBoard()
print()
board1.shake()
