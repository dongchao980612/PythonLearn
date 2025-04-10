import json
import os


class AuthorModel:
    def __init__(self, file_name):
        self.file_name = file_name
        self.authors = self.load_authors()

    def load_authors(self):
        """从文件加载作者数据"""
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r", encoding="utf-8") as file:
            try:
                authors = json.load(file)
            except json.JSONDecodeError:
                authors = []
        return authors

    def save_authors(self):
        """将作者数据保存到文件"""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.authors, file, ensure_ascii=False, indent=4)

    def add_author(self, author):
        """添加作者"""
        self.authors.append(author)
        self.save_authors()

    def get_authors(self):
        """获取所有作者"""
        return self.authors

    def delete_author(self, author_id):
        """删除作者"""
        self.authors = [author for author in self.authors if author["id"] != author_id]
        self.save_authors()

    def search_authors(self, keyword):
        """搜索作者"""
        return [author for author in self.authors if keyword in author["name"]]
