__author__ = 'sven'
import sys
import pymongo
from database import Database
import uuid
import datetime


class Post(object): # (object) --> Die Klasse erbt alle Eigenschaften von "object"

    def __init__(self, blog_id, title, content, author, timestamp=datetime.datetime.utcnow(), post_id=None): # post_id hat hier einen DefaultValue non
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = timestamp
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.post_to_json())
        
    def post_to_json(self):
        return {
            'post_id': self.post_id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.timestamp
        }
    # get one post by id
    @staticmethod
    def get_single_post(post_id):
        return Database.find_one(collection='posts', query={'id': post_id})
    
    # get all the posts that belong to a specific blog
    @staticmethod
    def get_all_posts(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': blog_id})]