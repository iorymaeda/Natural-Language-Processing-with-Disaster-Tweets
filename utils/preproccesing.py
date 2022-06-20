import re
import json
import pickle


class TextPreprocessor:
    """Removes trash symbols, replace emoticons and emoji to text"""
    def __init__(self, **kwargs):
        self.convert_emoticons = False
        
        if 'json' in kwargs:
            self.convert_emoticons = True
            with open(kwargs['json'], 'r') as f:
                self.emoticons_vocab = json.load(f)
        
        elif 'pkl' in kwargs:
            self.convert_emoticons = True
            with open(kwargs['pkl'], 'rb') as f:
                self.emoticons_vocab = pickle.load(f)
        
        if self.convert_emoticons:
            self.__unstip_vocab()
        
        
    def __unstip_vocab(self):
        self.emoticons_vocab = {k:f' {v} ' for k, v in self.emoticons_vocab.items()}
    
    
    def __call__(self, text: str) -> str:
        text = text.replace(r'&amp;', 'and')\
            .replace(r'&lt;', '<')\
            .replace(r'&gt;', '>')\
            .replace(r'&le;', '<=')\
            .replace(r'&ge;', '>=')

        # Convert emoticons to text
        if self.convert_emoticons:
            text = self.__emoticons(text)
            
        # Remove links like www.site.com
        text = re.sub(r'www\.[a-zA-Z\-]+\.[a-zA-Z\-]+', '', text)
        # Remove html tags, idk why they are here
        text = re.sub(r"<.+>", '', text)
        # Remove stupid simbols 
        text = text.encode("ascii", errors="ignore").decode()
        text = re.sub(r'[:"#$%&\*+,-/:;<=>@\\^_`{|}~()]+', '', text)
        
        return text
    
    
    def __emoticons(self, text:str) -> str:
        for k, v in self.emoticons_vocab.items():
            text = text.replace(k, v)
            
        return text