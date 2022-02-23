import sys
sys.path.append(".")
import pymongo
from database import Database
from post import Post
from blog import Blog
from menu import Menu

def main():
    Database.initialize()
    menu = Menu()
    menu.run_menu()
    
if __name__ == '__main__':
    main()