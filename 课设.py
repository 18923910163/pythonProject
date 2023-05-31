import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox
from tkinter import *

# 数据库连接配置
config = {
    'Driver': '{SQL Server}',
    'Server': 'DESKTOP-CFICQBB',
    'Database': 'BMS',
    'UID': 'sa',
    'PWD': 'zry021108+-'
}

# 登录页面
class Page_1():
    def __init__(self, window):
        self.window = window
        self.window.title("图书管理系统")
        self.window.geometry("300x150")
        self.window.config(bg="white")

        # 创建用户名和密码输入框
        self.username_label = tk.Label(self.window, text="用户名:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        self.password_label = tk.Label(self.window, text="密码:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.button_login = tk.Button(self.window, text="登录", command=self.login)
        self.button_login.pack()

    def login(self):
        # 获取输入的用户名和密码
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        # 验证登录
        if  self.username == "manager" and self.password == "123":
            self.button_login.destroy()
            self.username_label.destroy()
            self.username_entry.destroy()
            self.password_label.destroy()
            self.password_entry.destroy()
            Page_7(window)
            messagebox.showinfo("登录成功", "管理员登录成功")
            # open_manager_interface()
            # self.button_manager_interface = tk.Button(self.window, text="登录", command=self.change)

        elif self.username == "1" and self.password == "1":
            self.button_login.destroy()
            self.username_label.destroy()
            self.username_entry.destroy()
            self.password_label.destroy()
            self.password_entry.destroy()
            Page_2(window)
            messagebox.showinfo("登录成功", "读者登录成功")
            # open_reader_interface()
            # self.button_reader_interface = tk.Button(self.window, text="点击进入", command=self.button_reader_interface)

        else:
            messagebox.showerror("登录失败", "用户名或密码错误")

# 书库和读者中心
class Page_2():
    def __init__(self, window):
        self.window = window
        self.window.title("图书管理系统")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_books = tk.Button(self.window, text="书库", command=self.books)
        self.button_books.pack()
        self.button_reader_center = tk.Button(self.window, text="读者中心", command=self.reader_center)
        self.button_reader_center.pack()
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def back(self):
        # pass  # 不知道怎么写，先占位
        self.button_books.destroy()
        self.button_reader_center.destroy()
        self.button_back.destroy()
        Page_1(window)

    def books(self):
        self.button_books.destroy()
        self.button_reader_center.destroy()
        self.button_back.destroy()
        Page_3(window)

    def reader_center(self):
        self.button_books.destroy()
        self.button_reader_center.destroy()
        self.button_back.destroy()
        Page_4(window)


  # 借还书
class Page_3():
    def __init__(self, window):
        self.window = window
        self.window.title("书库中心")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_search_books =tk.Button(self.window, text="查书", command=self.search_books)
        self.button_search_books.pack()
        self.button_borrow_books = tk.Button(self.window, text="借书", command=self.borrow_books)
        self.button_borrow_books.pack()
        self.button_return_books = tk.Button(self.window, text="还书", command=self.return_books)
        self.button_return_books.pack()
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def search_books(self):
        self.button_search_books.destroy()
        self.button_borrow_books.destroy()

        self.button_return_books.destroy()
        self.button_back.destroy()
        Page_5(window)

    def return_books(self):
        self.button_search_books.destroy()
        self.button_borrow_books.destroy()

        self.button_return_books.destroy()
        self.button_back.destroy()
        Page_6(window)

    def borrow_books(self):
        self.button_search_books.destroy()
        self.button_borrow_books.destroy()
        self.button_return_books.destroy()
        self.button_back.destroy()
        Page_14(window)

    def back(self):
        self.button_search_books.destroy()
        self.button_borrow_books.destroy()
        self.button_return_books.destroy()
        self.button_back.destroy()
        Page_2(window)

#读者中心
class Page_4():
    def __init__(self, window):
        self.window = window
        self.window.title("录入信息")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back_reader = tk.Button(self.window, text="返回（读者登入）", command=self.back_reader)
        self.button_back_reader.pack()
        self.button_back_manager = tk.Button(self.window, text="返回（管理员登入）", command=self.back_manager)
        self.button_back_manager.pack()

    def back_reader(self):
        self.button_back_reader.destroy()
        self.button_back_manager.destroy()
        Page_2(window)

    def back_manager(self):
        self.button_back_reader.destroy()
        self.button_back_manager.destroy()
        Page_10(window)

 # 查书（读者登入）
# 创建输入框和按钮

class Page_5():
    def __init__(self, window):
        self.window = window
        self.window.title("查书")
        self.window.geometry("1400x400")
        self.window.config(bg="white")

        # 创建输入框和按钮
        self.search_label = tk.Label(self.window, text="关键词:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()

        self.search_button = tk.Button(self.window, text="查询", command=self.search)
        self.search_button.pack()

        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

        self.tree = ttk.Treeview(self.window, columns=("BookID", "BookName", "BookLBID", "BookWriter", "BookPubID", "BookPublish", "BookPrice", "BookDay", "BookPage", "BookKey", "BookDate", "BookState", "BookPS", "Book_stock"))
        self.tree.column("#0", width=0)
        self.tree.column("BookID", width=80)
        self.tree.column("BookName", width=100)
        self.tree.column("BookLBID", width=100)
        self.tree.column("BookWriter", width=80)
        self.tree.column("BookPubID", width=100)
        self.tree.column("BookPublish", width=100)
        self.tree.column("BookPrice", width=50)
        self.tree.column("BookPrice", width=100)
        self.tree.column("BookDay", width=100)
        self.tree.column("BookPage", width=100)
        self.tree.column("BookKey", width=100)
        self.tree.column("BookDate", width=100)
        self.tree.column("BookState", width=100)
        self.tree.column("BookPS", width=100)
        self.tree.column("Book_stock", width=100)
        self.tree.heading("BookID", text="图书编号")
        self.tree.heading("BookName", text="书名")
        self.tree.heading("BookLBID", text="书籍类别")
        self.tree.heading("BookWriter", text="作者")
        self.tree.heading("BookPubID", text="出版社编号")
        self.tree.heading("BookPublish", text="出版社")
        self.tree.heading("BookPrice", text="单价")
        self.tree.heading("BookDay", text="出版日期")
        self.tree.heading("BookPage", text="页码")
        self.tree.heading("BookKey", text="关键词")
        self.tree.heading("BookDate", text="登记日期")
        self.tree.heading("BookState", text="是否可借")
        self.tree.heading("BookPS", text="备注")
        self.tree.heading("Book_stock", text="书籍库存")
        # 定义显示列宽度
        self.tree.pack()

    def search(self):
        # 清空表格
        self.tree.delete(*self.tree.get_children())

        # 获取检索关键字
        keyword = self.search_entry.get()

        search_results = self.search_from_database(keyword)

        # 遍历结果列表，插入数据到表格中
        for result in search_results:
            图书编号 = result["BookID"]
            书名 = result["BookName"]
            书籍类别 = result["BookLBID"]
            作者 = result["BookWriter"]
            出版社编号 = result["BookPubID"]
            出版社 = result["BookPublish"]
            单价 = result["BookPrice"]
            出版日期 = result["BookDay"]
            页码 = result["BookPage"]
            关键词 = result["BookKey"]
            登记日期 = result["BookDate"]
            是否可借 = result["BookState"]
            备注 = result["BookPS"]
            书籍库存 = result["Book_stock"]

            # 插入数据到表格中
            self.tree.insert("", "end", values=(图书编号, 书名, 书籍类别, 作者, 出版社编号, 出版社, 单价, 出版日期, 页码, 关键词, 登记日期, 是否可借, 备注, 书籍库存))


    def search_from_database(self, keyword):
        # 建立数据库连接并执行查询
        conn = pyodbc.connect(**config)
        cursor = conn.cursor()
        query = "SELECT * FROM Book WHERE BookName LIKE ? OR BookWriter LIKE ? OR BookPublish LIKE ? OR BookDate LIKE ?"
        params = ['%' + keyword + '%'] * 4
        cursor.execute(query, params)

        # 获取查询结果
        search_results = []
        for row in cursor:
            result = {
                "BookID": row.BookID,
                "BookName": row.BookName,
                "BookLBID": row.BookLBID,
                "BookWriter": row.BookWriter,
                "BookPubID": row.BookPubID,
                "BookPublish": row.BookPublish,
                "BookPrice": row.BookPrice,
                "BookDay": row.BookDay,
                "BookPage": row.BookPage,
                "BookKey": row.BookKey,
                "BookDate": row.BookDate,
                "BookState": row.BookState,
                "BookPS": row.BookPS,
                "Book_stock": row.Book_stock
            }
            search_results.append(result)

        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

        return search_results


    def back(self):
        self.button_search.destroy()
        self.button_back.destroy()
        Page_3(window)

# 还书（读者登入）
class Page_6():
    def __init__(self, window):
        self.window = window
        self.window.title("还书")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def back(self):
        self.button_back.destroy()
        Page_3(window)

 # （管理员登入）
class Page_7():
    def __init__(self, window):
        self.window = window
        self.window.title("图书管理系统")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_books_manager = tk.Button(self.window, text="书库管理", command=self.books_manager)
        self.button_books_manager.pack()
        self.button_reader_manager = tk.Button(self.window, text="读者管理", command=self.reader_manager)
        self.button_reader_manager.pack()
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def books_manager(self):
        self.button_books_manager.destroy()
        self.button_reader_manager.destroy()
        self.button_back.destroy()
        Page_9(window)

    def reader_manager(self):
        self.button_books_manager.destroy()
        self.button_reader_manager.destroy()
        self.button_back.destroy()
        Page_10(window)

    def back(self):
        self.button_books_manager.destroy()
        self.button_reader_manager.destroy()
        self.button_back.destroy()
        Page_1(window)

# 查看书籍详情（读者登入）
class Page_8():
    def __init__(self, window):
        self.window = window
        self.window.title("书籍详情")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back_reader = tk.Button(self.window, text="返回（读者登入）", command=self.back_reader)
        self.button_back_reader.pack()
        self.button_back_manager = tk.Button(self.window, text="返回（管理员登入）", command=self.back_manager)
        self.button_back_manager.pack()



    def back_reader(self):
        self.button_back_reader.destroy()
        self.button_back_manager.destroy()
        Page_5(window)

    def back_manager(self):
        self.button_back_reader.destroy()
        self.button_back_manager.destroy()
        Page_9(window)

class Page_9():  # 书库管理（管理员登入）
    def __init__(self, window):
        self.window = window
        self.window.title("书库管理")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_edit = tk.Button(self.window, text="点击修改", command=self.edit)
        self.button_edit.pack()
        self.button_add_book = tk.Button(self.window, text="新增图书", command=self.add_book)
        self.button_add_book.pack()
        self.button_borrow = tk.Button(self.window, text="查看借阅信息", command=self.borrow)
        self.button_borrow.pack()
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def edit(self):
        self.button_edit.destroy()
        self.button_add_book.destroy()
        self.button_borrow.destroy()
        self.button_back.destroy()
        Page_8(window)

    def add_book(self):
        self.button_edit.destroy()
        self.button_add_book.destroy()
        self.button_borrow.destroy()
        self.button_back.destroy()
        Page_11(window)

    def borrow(self):
        self.button_edit.destroy()
        self.button_add_book.destroy()
        self.button_borrow.destroy()
        self.button_back.destroy()
        Page_12(window)

    def back(self):
        self.button_edit.destroy()
        self.button_borrow.destroy()
        self.button_back.destroy()
        Page_7(window)

class Page_10():  # 读者管理（管理员登入）
    def __init__(self, window):
        self.window = window
        self.window.title("读者管理")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_reader_type = tk.Button(self.window, text="读者种类管理", command=self.reader_type)
        self.button_reader_type.pack()
        self.button_reader_information = tk.Button(self.window, text="读者信息管理", command=self.reader_information)
        self.button_reader_information.pack()
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def reader_type(self):
        self.button_reader_type.destroy()
        self.button_reader_information.destroy()
        self.button_back.destroy()
        Page_13(window)

    def reader_information(self):
        self.button_reader_type.destroy()
        self.button_reader_information.destroy()
        self.button_back.destroy()
        Page_4(window)

    def back(self):
        self.button_reader_type.destroy()
        self.button_reader_information.destroy()
        self.button_back.destroy()
        Page_7(window)

class Page_11():  # 新增图书（管理员登入）
    def __init__(self, window):
        self.window = window
        self.window.title("新增图书")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def back(self):
        self.button_back.destroy()
        Page_9(window)

class Page_12():  # 借阅情况（管理员登入）
    def __init__(self, window):
        self.window = window
        self.window.title("查阅借阅情况")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def back(self):
        self.button_back.destroy()
        Page_9(window)

class Page_13():  # 读者种类（管理员登入）
    def __init__(self, window):
        self.window = window
        self.window.title("读者种类管理")
        self.window.geometry("300x300")
        self.window.config(bg="white")
        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()

    def back(self):
        self.button_back.destroy()
        Page_10(window)
# 借书

class Page_14():
    def __init__(self, window):
        self.window = window
        self.window.title("借书")
        self.window.geometry("300x600")
        self.window.config(bg="white")

        # 创建输入框和按钮
        self.search_label = tk.Label(self.window, text="书籍编号:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()
        # 创建用于显示查询结果的文本框
        self.result_text = tk.Text(self.window, height=10, width=40)
        self.result_text.pack()
        self.result_text.configure(state='disabled')  # 初始状态禁用文本框

        self.search_button = tk.Button(self.window, text="查询", command=self.search)
        self.search_button.pack()

        self.borrow_button = tk.Button(self.window, text="借书", command=self.borrow)
        self.borrow_button.pack()

        self.button_back = tk.Button(self.window, text="返回", command=self.back)
        self.button_back.pack()


    def search(self):
        self.result_text.configure(state=NORMAL)  # 将文本框的状态设置为可编辑状态，以便在查询结果插入文本时进行修改。
        self.result_text.delete("1.0", tk.END)  # 删除文本框中从第一行第一个字符（"1.0"）到末尾（tk.END）的内容，即清空整个文本框。

        # 执行查询
        keyword = self.search_entry.get()

        self.search_results = self.search_from_databse(keyword)

        # 将查询结果展示在文本框中
        for result in self.search_results:
            self.result_text.insert(tk.END, f"图书编号: {result['BookID']}\n")
            self.result_text.insert(tk.END, f"书名: {result['BookName']}\n")
            self.result_text.insert(tk.END, f"书籍类别: {result['BookLBID']}\n")
            self.result_text.insert(tk.END, f"作者: {result['BookWriter']}\n")
            self.result_text.insert(tk.END, f"出版社编号: {result['BookPubID']}\n")
            self.result_text.insert(tk.END, f"出版社: {result['BookPublish']}\n")
            self.result_text.insert(tk.END, f"单价: {result['BookPrice']}\n")
            self.result_text.insert(tk.END, f"出版日期: {result['BookDay']}\n")
            self.result_text.insert(tk.END, f"页码: {result['BookPage']}\n")
            self.result_text.insert(tk.END, f"关键词: {result['BookKey']}\n")
            self.result_text.insert(tk.END, f"登记日期: {result['BookDate']}\n")
            self.result_text.insert(tk.END, f"是否可借: {result['BookState']}\n")
            self.result_text.insert(tk.END, f"备注: {result['BookPS']}\n")
            self.result_text.insert(tk.END, f"书籍库存: {result['Book_stock']}\n")
            self.result_text.insert(tk.END, "-----------------------------\n")

        search_button = tk.Button(window, text="查询", command=self.search)
        search_button.pack()

    def search_from_database(self, keyword):
        # 建立数据库连接并执行查询
        conn = pyodbc.connect(**config)
        cursor = conn.cursor()
        query = "SELECT * FROM Book WHERE BookID =?"
        params = ['%' + keyword + '%'] * 4
        cursor.execute(query, params)

        # 获取查询结果
        search_results = []
        for row in cursor:
            result = {
                "BookID": row.BookID,
                "BookName": row.BookName,
                "BookLBID": row.BookLBID,
                "BookWriter": row.BookWriter,
                "BookPubID": row.BookPubID,
                "BookPublish": row.BookPublish,
                "BookPrice": row.BookPrice,
                "BookDay": row.BookDay,
                "BookPage": row.BookPage,
                "BookKey": row.BookKey,
                "BookDate": row.BookDate,
                "BookState": row.BookState,
                "BookPS": row.BookPS,
                "Book_stock": row.Book_stock
            }
            search_results.append(result)

        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

        return search_results

    def borrow(self):
        self.button_back.destroy()
        Page_13(window)
    def back(self):
        self.button_back.destroy()
        Page_3(window)


# 创建主窗口
window = tk.Tk()


p1 = Page_1(window)
# 运行主循环
window.mainloop()
