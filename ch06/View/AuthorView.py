class AuthorView:
    @staticmethod
    def display_authors(authors):
        """显示作者列表"""
        if not authors:
            print("暂无作者信息！")
        else:
            for author in authors:
                print(f"ID: {author['id']}, 姓名: {author['name']}")

    @staticmethod
    def display_message(message):
        """显示消息"""
        print(message)

    @staticmethod
    def get_user_input(prompt):
        """获取用户输入"""
        return input(prompt)