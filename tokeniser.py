import os
import random
import datetime

class Tokeniser:
    """Tokens such as {% fn args %} will result in calls to methods on
    this class Tokeniser.fn(args) with returned results replacing the
    token in the source file.
    """

    def __init__(self, src_root, dest_root):
        self.src_root = src_root
        self.dest_root = dest_root
    
    def hello(self):
        return random.choice(["Hello!", "Hi!", "Hoi!"])

    def year(self):
        return datetime.date.today().year

    def include(self, file):
        with open(os.path.join(self.src_dir, file)) as f:
            return f.read()

