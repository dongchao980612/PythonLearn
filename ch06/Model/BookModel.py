import json
import os


class BookModel:
    def __init__(self, file_name):
        self.file_name = file_name
        self.books = self.load_books()

    def load_books(self):
        """从文件加载图书数据"""
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r", encoding="utf-8") as file:
            try:
                books = json.load(file)
            except json.JSONDecodeError:
                books = []
        return books

    def save_books(self):
        """将图书数据保存到文件"""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def add_book(self, book):
        """添加图书"""
        self.books.append(book)
        self.save_books()

    def get_books(self):
        """获取所有图书"""
        return self.books

    def delete_book(self, book_id):
        """删除图书"""
        self.books = [book for book in self.books if book["id"] != book_id]
        self.save_books()

    def search_books(self, keyword):
        """搜索图书"""
        return [book for book in self.books if keyword in book["title"] or keyword in book["author"]]
