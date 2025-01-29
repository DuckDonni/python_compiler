

# Tokenizes each line of source code into a sequence of tokens

class Lexer: 
    
    def __init__(self, input_text):
        self.input_text = input_text
        self.current_position = 0
        self.tokens = []
        self.keywords = {
            'def','return','if','else',
            'while','for','in','break',
            'continue','True','False',
            'None',"and','or","not",'is',
            }


    def get_next_token(self):
        # Token Logic
        pass

