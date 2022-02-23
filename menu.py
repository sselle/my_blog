__author__ = 'sven'
from database import Database
from blog import Blog 

class Menu(object):
    def __init__(self):
        self.user = input('enter author name: ')
        self.user_blog = None
        if self._user_has_account() == True:
            print ('Welcome back {}'.format(self.user))
        else:
            self._prompt_user_for_account()
        
    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['blog_id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input('enter title of the blog: ')
        description = input('enter description of the blog: ')
        blog = Blog(author=self.user, 
                    title=title, 
                    description=description)
        
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        read_or_write = input('Do you want to read (R) or write (W) blogs?')

        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write =='W':
            self.user_blog.new_post()
        else:
            print('invalid input, abort')

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print('ID: {}, Title: {}, Author: {}, '.format(blog['blog_id'], blog['title'], blog['title']))
    
    def _view_blog(self):
        selected_blog = input('Enter the ID of the blog you like to read')
        blog = Blog.get_from_mongo(selected_blog)
        posts = blog.get_posts()
        for post in posts:
            print('Date: {}, title: {}\n\n{}'.format(post['created_date'], post['title'], post['content']))