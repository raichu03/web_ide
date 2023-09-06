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
            },
            {
                "id": "75832",
                "title": "Fibonacci Sequence",
                "description": "write a program that generates Fibonacci sequence up to n term. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.",
                "example": "Input: 7 Output: 0, 1, 2, 3, 5, 8, 13"
            },

            {
                "id": "35156",
                "title": "Second Largest Element",
                "description": "Write a program to find the second largest element in an array or list of integers. Incase of duplicate print any",
                "example": "Input: [45, 23, 35, 9] Output: 35"
            },

            {
                "id": "62314",
                "title": "List of Digits",
                "description": "Write a function that takes a number and returns a list of its digits. ",
                "example": "Input: 2342 Output: [2,3,4,2]"
            },

            {
                "id": "39845",
                "title": "String Length",
                "description": "Write a program that returns the length of string. Without using any built in function.",
                "example": "Input: apple, make Output: 5, 4 "
            },

            {
                "id": "45221",
                "title": "No First Character",
                "description": "Write a program to take string as input and return a second string without a first character from inputed string",
                "example": "Input: kathmandu Output: athmandu"
            }
        ]

        return random.choice(easyList)
    
    def mediumQuestion(self):

        mediumList = [
            {
                "id": "75832",
                "title": "Fibonacci Sequence",
                "description": "write a program that generates Fibonacci sequence up to n term. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.",
                "example": "Input: 7 Output: 0, 1, 2, 3, 5, 8, 13"
            },

            {
                "id": "35156",
                "title": "Second Largest Element",
                "description": "Write a program to find the second largest element in an array or list of integers. Incase of duplicate print any",
                "example": "Input: [45, 23, 35, 9] Output: 35"
            },

            {
                "id": "62314",
                "title": "List of Digits",
                "description": "Write a function that takes a number and returns a list of its digits. ",
                "example": "Input: 2342 Output: [2,3,4,2]"
            },

            {
                "id": "39845",
                "title": "String Length",
                "description": "Write a program that returns the length of string. Without using any built in function.",
                "example": "Input: apple, make Output: 5, 4 "
            },

            {
                "id": "45221",
                "title": "No First Character",
                "description": "Write a program to take string as input and return a second string without a first character from inputed string",
                "example": "Input: kathmandu Output: athmandu"
            }

        ]

        return random.choice(mediumList)
    

    def hardQuestion(self):

        hardList = [
            {
                "id": "98752",
                "title": "Word Count",
                "description": "Write a program to count number of character in a given string and return. Your program should count actual words not characters",
                "example": "Input: Kathmandu University Output: 2"
            },

            {
                "id": "35213",
                "title": "GCD and LCM",
                "description": "Write a program that takes two integers and calculates GCD and LCM of two integers and returns the result",
                "example": "Input: 42 68 Output: GCD = 2 LCM = 1428"
            },

            {
                "id": "65151",
                "title": "Triangle or Not",
                "description": "Write a program that takes three sides of triangle as input and return whether those sides form a triangle or not. If it forms triangle print true else false",
                "example": "Input: (3,4,5), (1,2,5) Output: true, false"
            },

            {
                "id": "56313",
                "title": "Valid Parentheses",
                "description": "Write a program that checks whether the parentheses in a string is valid or not. Open brackets should be closed by the same type, in correct order, every closed bracket have corresponding open bracket",
                "example": "Input: (), ()[]{}, (] Output: true, true, false"
            }

        ]

        return random.choice(hardList)