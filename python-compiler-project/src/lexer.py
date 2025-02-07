
from Token import Token
# Tokenizes each line of source code into a sequence of tokens

class Lexer: 
    
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []
        self.keywords = {
            'def','return','if','else',
            'while','for','in','break',
            'continue','True','False',
            'None',"and','or","not",'is',
            }


    def get_next_token(self):
        if self.position >=(self.input_text):
            return None

        current_char = self.input_text[self.position]

        if current_char.isspace():
            self.position += 1
            return self.get_next_token()
        if current_char.isalpha():
            return self._identifier()
        if current_char.isdigit():
            return self._number()
        if current_char in '+-*/%^':
            return Token('OPERATOR', current_char)
        if current_char in '(){}[],.:;':
            self.position +=1
            return Token('DELIMITER', current_char)
        self.position += 1
        
        return Token('UNKNOWN', current_char)

    def _identifier(self):
        start_pos = self.position
        while self.position < len(self.input_text) and (self.input_text[self.position].isalnum() or self.input_text[self.position] == '_'):
            self.position += 1
        value = self.input_text[start_pos:self.position]
        token_type = 'KEYWORD' if value in self.keywords else 'IDENTIFIER'
        return Token(token_type, value)
    
    def _number(self):
        start_pos = self.position
        while self.position < len(self.input_text) and self.input_text[self.position].isdigit():
            self.position += 1
        value = self.input_text[start_pos:self.position]
        return Token('NUMBER', value)
    def tokenize(self):
        while self.position<len(self.input_text):
            token = self.get_next_token()
            if token:
                self.tokens.append(token)
        return self.tokens