from datetime import date
import inflect
import sys


class HowOld:
    """
    Handles the conversion of age from dates to minutes
    """
    def __init__(self, birth, today):
        # Validates format
        try:
            self.birth = date.fromisoformat(birth)
        except:
            sys.exit("Invalid date")
        self.today = today

    @classmethod
    def info(cls):
        birth = input("Date of Birth: ")
        today = date.today()
        return cls(birth, today)

    def calculate_minutes(self):
        #Calculates the total minutes between birth and a given date.
        diff = self.today - self.birth
        return diff.days * 24 * 60


def main():
    #Converts the minutes into English words using inflect.
    p = inflect.engine()
    user_data = HowOld.info()
    total_minutes = user_data.calculate_minutes()
    words = p.number_to_words(total_minutes, andword="")
    print(f"{words.capitalize()}")


if __name__ == "__main__":
    main()
