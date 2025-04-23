import random

class options():

    def __init__(self):
        self.dialogue_list = ["Replace people with AIs?", "Buy out the stock of a large AI company?", 
                        "Develop a concious AI?", "Make new identification principles for people that include a digital AI?", 
                        "Spend your life working on an AI project?", "Implement new regulations within the company that people must dataparse manually for better results?",
                        "Develop a warmind during wartime?", "Develop a warmind during peace times?", 
                        "Require workers to use an AI Assistant for jobs?", "Develop an AI that can distribute power accross the country?",
                        "Require all AIs to use uncopyrighted datasets?", "Create regulations that require all AIs to be government regulated?",
                        "Limit token usage across users?", "Force phone users to give privacy access to an on-device AI?",
                        "Create your own data center for your AI tasks?", "Use user data for training on AIs?",
                        "Develop your own programming language for people to develop AIs easier?", "Go out and sue all AI companies for copyrighted data usage?"]
    
    def find_dialogue_option(self):
        rand = random.randint(0, len(self.dialogue_list) - 1)
        p, t, k = self.find_dialogue_cost(rand)
        return self.dialogue_list[rand], p, t, k
    
    def find_dialogue_cost(self, index):
        match index:
            case 0:
                return -1, 2, -1
            case 1:
                return 0, -1, 0
            case 2:
                return -1, 2, 1
            case 3:
                return -1, 1, 0
            case 4:
                return 0, 0, 2
            case 5:
                return -1, 1, 0
            case 6:
                return -2, 2, -1
            case 7:
                return -2, 0, -1
            case 8:
                return 0, 1, 0
            case 9:
                return 1, 2, 0
            case 10:
                return 2, -1, 1
            case 11:
                return 2, -2, 0
            case 12:
                return -1, -1, -1
            case 13:
                return -1, 2, -1
            case 14:
                return -1, 2, -1
            case 15:
                return -2, 2, -1
            case 16:
                return 1, 2, 1
            case 17:
                return 1, -1, 2
            case _:
                return 0, 0, 0