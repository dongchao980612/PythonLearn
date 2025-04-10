class AuthorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_author(self):
        """添加作者"""
        author_id = self.view.get_user_input("请输入作者ID: ")
        name = self.view.get_user_input("请输入作者姓名: ")
        author = {"id": author_id, "name": name}
        self.model.add_author(author)
        self.view.display_message("作者添加成功！")

    def display_authors(self):
        """显示所有作者"""
        authors = self.model.get_authors()
        self.view.display_authors(authors)

    def delete_author(self):
        """删除作者"""
        author_id = self.view.get_user_input("请输入要删除的作者ID: ")
        self.model.delete_author(author_id)
        self.view.display_message("作者删除成功！")

    def search_authors(self):
        """搜索作者"""
        keyword = self.view.get_user_input("请输入搜索关键词: ")
        authors = self.model.search_authors(keyword)
        self.view.display_authors(authors)