import sys
sys.path.append(".")
import pymongo
from database import Database
from post import Post

def main():
    Database.initialize()
    
    
if __name__ == '__main__':
    main()