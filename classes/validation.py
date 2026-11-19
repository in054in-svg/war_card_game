class Validation:
    @staticmethod
    def edit_special_cards(num):
        if num == 11:
            return 'J'
        elif num == 12:
            return 'Q'
        elif num == 13:
            return 'K'
        elif num == 14:
            return 'a'
        else:
            return num