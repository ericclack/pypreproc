import os
import random
import datetime

class TokenProcessor:
    """Process a token and return the result. """

    def __init__(self, src_root, dest_root):
        self.src_root = src_root
        self.dest_root = dest_root

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Tokens you can use in your source files
    
    def hello(self):
        return random.choice(["Hello!", "Hi!", "Hoi!"])

    def year(self):
        return datetime.date.today().year

    def include(self, file):
        with open(os.path.join(self.src_dir, file)) as f:
            return f.read()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

