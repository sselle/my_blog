__author__ = 'sven'
import uuid
import post
import datetime

class Blog(object):

    def __init__(self, author, title, description, blog_id=None):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = uuid.uuid4().hex if blog_id is None else blog_id
    
    def new_post(self):
        title = input('Enter post title: ')
        content = input('Enter post content: ')
        date = input('Enter data or leave blank (in format DDMMYYYY)')
        post = post.Post(blog_id=self.blog_id, title=title, content=content, author=self.author, date=datetime.datetime.strptime(date, "%d%m%Y"))

    def get_posts(self):
        pass

    def save_to_mongo(self):
        pass
    
    def to_json(self):
        pass