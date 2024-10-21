## Question 1
You are tasked with developing a Python program to suggest search query completions based on a user's search history. The program should efficiently find completions using a any search algorithm.

Input:
search_history = [
        "apple",
        "banana",
        "carrot",
        "pear",
        "pineapple",
        "potato",
        "strawberry"
    ]

Output:
Enter your partial search query: p
Suggestions:
pear
pineapple
potato

## Question 2
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert the minimum number of characters from/in str1 to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted at some another point.

Example 1:
Input :
str1 = "heap", str2 = "pea"
Output :
Minimum Deletion = 2 and
Minimum Insertion = 1

## Question 3
Create a python code to demonstrate the working of decision tree, for the input use knowledge base:
K_Base = {
   "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}
  }
 },
        "No": "Check the power supply and cables"
    }
}

## Question 4
Create a program to find out if a number plate is valid or not.The most common format for private vehicles in India is "XX NN YY NNNN", where: "XX" represents two uppercase letters indicating the code of the state or union territory where the vehicle is registered. "NN" represents two digits indicating the RTO (Regional Transport Office) code within the state. "YY" represents two uppercase letters indicating a series. "NNNN" represents a four-digit number. For example, a private vehicle registered in Maharashtra might have a number plate like "MH 12 AB 1234".
