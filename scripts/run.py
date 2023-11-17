import sys
import os
# (os.path.abspath(file)) gives the full absolute path of this file (run.py)
# (os.path.dirname()) returns the path "dirname" with the last component removed. 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add parent directory to sys.path
sys.path.append(parent_dir)

# Import main using a relative path 
from exchange_rates_alert.main import main

def run():
  main()

if __name__ == '__main__':
  run()
