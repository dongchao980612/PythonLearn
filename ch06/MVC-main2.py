from ch06.Controller.AuthorController import AuthorController
from ch06.Controller.BookController import BookController
from ch06.Model.AuthorModel import AuthorModel
from ch06.Model.BookModel import BookModel
from ch06.View.AuthorView import AuthorView
from ch06.View.BookView import BookView

if __name__ == "__main__":
    book_file_name = "books.json"
    author_file_name = "authors.json"

    book_model = BookModel(book_file_name)
    author_model = AuthorModel(author_file_name)

    book_view = BookView()
    author_view = AuthorView()

    book_controller = BookController(book_model, book_view)
    author_controller = AuthorController(author_model, author_view)

    while True:
        print("\n图书管理系统")
        print("1. 图书管理")
        print("2. 作者管理")
        print("3. 退出")
        choice = book_view.get_user_input("请选择操作: ")

        if choice == "1":
            while True:
                print("\n图书管理")
                print("1. 添加图书")
                print("2. 显示所有图书")
                print("3. 删除图书")
                print("4. 搜索图书")
                print("5. 返回")
                book_choice = book_view.get_user_input("请选择操作: ")
                if book_choice == "1":
                    book_controller.add_book()
                elif book_choice == "2":
                    book_controller.display_books()
                elif book_choice == "3":
                    book_controller.delete_book()
                elif book_choice == "4":
                    book_controller.search_books()
                elif book_choice == "5":
                    break
                else:
                    book_view.display_message("无效的选择，请重新输入！")

        elif choice == "2":
            while True:
                print("\n作者管理")
                print("1. 添加作者")
                print("2. 显示所有作者")
                print("3. 删除作者")
                print("4. 搜索作者")
                print("5. 返回")
                author_choice = author_view.get_user_input("请选择操作: ")
                if author_choice == "1":
                    author_controller.add_author()
                elif author_choice == "2":
                    author_controller.display_authors()
                elif author_choice == "3":
                    author_controller.delete_author()
                elif author_choice == "4":
                    author_controller.search_authors()
                elif author_choice == "5":
                    break
                else:
                    author_view.display_message("无效的选择，请重新输入！")

        elif choice == "3":
            print("感谢使用图书管理系统，再见！")
            break
        else:
            book_view.display_message("无效的选择，请重新输入！")