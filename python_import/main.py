import sys
sys.path.insert(0, './python_import/libs')
# from helper import greeting # Imports the greeting fucntion only
import helper as h # Alias call out

def render():
    print(h.greeting('James', 'Jager'))


render()