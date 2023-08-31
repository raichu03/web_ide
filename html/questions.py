import random

class Question:
    def __init__(self) -> None:
        pass



    def easyQuestion(self):

        easyList = [
            {
                "id": "13567",
                "title": "check palindrome number",
                "description": "given a integer x, return true if x is palindrome integer else return false",
                "example": "input: x = 121,<br> &emsp;output: true",
            },
            {
                "id": "38853",
                "title": "check palindrome string",
                "description": "given a string x, return true if x is palindrome string else return false",
                "example": "input: x = race car,<br> &emsp;output: true",
            }
        ]

        return random.choice(easyList)
    
    def mediumQuestion(self):

        mediumList = [

        ]

        return random.choice(mediumList)
    

    def hardQuestion(self):

        hardList = [

        ]

        return random.choice(hardList)