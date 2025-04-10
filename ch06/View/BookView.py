class BookView:
    @staticmethod
    def display_books(books):
        """显示图书列表"""
        if not books:
            print("暂无图书信息！")
        else:
            for book in books:
                print(f"ID: {book['id']}, 标题: {book['title']}, 作者: {book['author']}")

    @staticmethod
    def display_message(message):
        """显示消息"""
        print(message)

    @staticmethod
    def get_user_input(prompt):
        """获取用户输入"""
        return input(prompt)