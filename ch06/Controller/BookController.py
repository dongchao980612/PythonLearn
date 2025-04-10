class BookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self):
        """添加图书"""
        book_id = self.view.get_user_input("请输入图书ID: ")
        title = self.view.get_user_input("请输入图书标题: ")
        author = self.view.get_user_input("请输入图书作者: ")
        book = {"id": book_id, "title": title, "author": author}
        self.model.add_book(book)
        self.view.display_message("图书添加成功！")

    def display_books(self):
        """显示所有图书"""
        books = self.model.get_books()
        self.view.display_books(books)

    def delete_book(self):
        """删除图书"""
        book_id = self.view.get_user_input("请输入要删除的图书ID: ")
        self.model.delete_book(book_id)
        self.view.display_message("图书删除成功！")

    def search_books(self):
        """搜索图书"""
        keyword = self.view.get_user_input("请输入搜索关键词: ")
        books = self.model.search_books(keyword)
        self.view.display_books(books)

