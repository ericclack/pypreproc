#!/usr/bin/env python3

import os
from pathlib import Path
from shutil import copyfile
import re
from tokenprocessor import TokenProcessor

SRC_ROOT = os.environ.get('SRC_ROOT', 'src')
DEST_ROOT = os.environ.get('DEST_ROOT', 'dest')
PROCESS = ['html']

# Tokens look like this: {% year %}
TOKEN_RE = r'{%\s*(.*?)\s*%}'
TOK = TokenProcessor(SRC_ROOT, DEST_ROOT)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def file_extension(f):
    return os.path.splitext(f)[1][1:]

def dest_equiv(src_dir):
    # Swap the first item in path (src) for the dest directory
    return Path(DEST_ROOT).joinpath(*Path(src_dir).parts[1:])

def process_token(matchobj):
    expression = matchobj.group(1).split(' ')
    fn = expression[0]
    args = expression[1:]
    print("\tProcessing: `%s` with args %s" % (fn, args))

    try:
        return str(getattr(TOK, fn)(*args))
    except AttributeError as e:
        print("ERROR: %s" % e)
        return "<!-- bad token: %s -->" %  matchobj.group(1)

def processfile(src_file, dest_file):
    with open(src_file, "r") as f_in:
        with open(dest_file, "w") as f_out:
            for line in f_in:
                newline = re.sub(TOKEN_RE, process_token, line)
                f_out.write(newline)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Make the destination directory where the site will be created
Path(DEST_ROOT).mkdir(exist_ok=True)

# Walk the source directory structure, copying
# across files and processing HTML
for src_dir, subdirs, files in os.walk(SRC_ROOT):
    print('Directory: %s' % src_dir, end=' ')
    
    dest_dir = dest_equiv(src_dir)
    print('\t-> %s' % dest_dir)
    # Check it exists
    dest_dir.mkdir(exist_ok=True)
    
    for f in files:
        print('\t%s:' % f, end=' ')
        src_file = os.path.join(src_dir, f)                     
        dest_file = os.path.join(dest_dir, f)
        
        if file_extension(f) in PROCESS:
            processfile(src_file, dest_file)
            print('processed.')
        else:
            copyfile(src_file, dest_file)
            print('copied.')
        
    print()

# Validation
print('- ' * 30)
print('diff report:')
os.system('diff -r %s %s' % (SRC_ROOT, DEST_ROOT))
    
