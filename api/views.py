from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class Book(Resource):
    """ The books View """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Returns a list of quotes """
        query = "SELECT * FROM book ORDER BY created DESC"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        books = self.db.clean_select_results(rows, keys)

        return {
            'Books': books
        }

    def post(self):
        """
        Add a book to the db
        Expect a JSON payload with the following format
        {
            "title": "The title of the book",
            "author": "The author",
        }
        """
        data = request.get_json()
        query = "INSERT INTO `book` (`title`, `author`) VALUES (:title, :author)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False