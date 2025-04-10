from ch06.Controller.BookController import BookController
from ch06.Model.BookModel import BookModel
from ch06.View.BookView import BookView

if __name__ == "__main__":
    file_name = "books.json"
    book_model = BookModel(file_name)
    book_view = BookView()
    book_controller = BookController(book_model, book_view)






    while True:
        print("\n图书管理")
        print("1. 添加图书")
        print("2. 显示所有图书")
        print("3. 删除图书")
        print("4. 搜索图书")
        print("5. 退出")
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
            print("感谢使用图书管理系统，再见！")
            break
        else:
            book_view.display_message("无效的选择，请重新输入！")

