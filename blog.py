__author__ = 'sven'
import uuid
from post import Post
from database import Database
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
        date_input = input('Enter data or leave blank (in format DDMMYYYY)')

        if date_input == "":
            date_input = datetime.datetime.utcnow()
        else:
            date_input = datetime.datetime.strptime(date_input, "%d%m%Y")

        post = Post(blog_id=self.blog_id, 
                    title=title, 
                    content=content, 
                    author=self.author,
                    timestamp=date_input)

        post.save_to_mongo()

    def get_posts(self):
        return Post.get_all_posts(self.blog_id)

    def save_to_mongo(self):
        Database.insert(collection = 'blogs',
                        data=self.post_to_json())
    
    def post_to_json(self):
        return {'author': self.author,
                'title': self.title,
                'description': self.description,
                'blog_id': self.blog_id}
    
    @classmethod
    def get_from_mongo(cls, blog_id):
        blog_data = Database.find_one(collection='blogs', query={'blog_id': blog_id})

        return cls(author=blog_data['author'], 
                    title=blog_data['title'], 
                    description=blog_data['description'], 
                    blog_id=blog_data['blog_id'])
        