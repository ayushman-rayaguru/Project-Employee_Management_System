from tkinter import *
import pyodbc
def fun():
    def btn_clicked():
        print("Button Clicked")

    #def connectdb():
    conn = pyodbc.connect(
        "Driver={SQL server Native Client 11.0};"
        "Server=AYUSHMAN\AYUSHMSSQL;"
        "Database=pyprj;"
        "Trusted_Connection=yes;"
        )
    

    def read(conn):
        print("Read")
        cursor = conn.cursor()
        cursor.execute("select * from dummy")
        for row in cursor:
            print(f'row = {row}')
        print()

    def create(conn):
        print("Create")
        cursor = conn.cursor()
        cursor.execute("insert into dummy(a,b) values(?,?);",(32206,"Ayushman"))
        conn.commit()
        read(conn)

    def update(conn):
        print("Update")
        cursor = conn.cursor()
        cursor.execute("update dummy set b = ? where a = ?;",("Madhav",32206))
        conn.commit()
        read(conn)

    def delete(conn):
        print("Delete")
        cursor = conn.cursor()
        cursor.execute("delete from dummy where a = ?;",(32206))
        conn.commit()
        read(conn)

    window = Tk()

    window.geometry("800x600")
    window.configure(bg = "#ffffff")
    window.iconbitmap('E:/Ayush/CODING/code/Projects/DB prj/main/dbico.ico')
    window.title('Employee Management System - by Ayushman')

    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    image_0 = PhotoImage(file = "image_0.png")
    canvas_image_0 = canvas.create_image(
        400.0, 300.0,
        image=image_0)

    image_1 = PhotoImage(file = "image_1.png")
    canvas_image_1 = canvas.create_image(
        400.0, 117.0,
        image=image_1)

    canvas.create_text(
        408.0, 265.0,
        text = "Employee Management System",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(30.0)))

    img0 = PhotoImage(file = f"img0.png")

    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = read,
        relief = "flat")

    b0.place(
        x = 47, y = 534,
        width = 110,
        height = 54)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = create,
        relief = "flat")

    b1.place(
        x = 171, y = 534,
        width = 110,
        height = 54)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = update,
        relief = "flat")

    b2.place(
        x = 295, y = 534,
        width = 110,
        height = 54)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = delete,
        relief = "flat")

    b3.place(
        x = 419, y = 534,
        width = 110,
        height = 54)

    """
    b4 = Button(
        text = "Connect to DB",
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 670, y = 549,
        width = 100,
        height = 25)
    """
    canvas.create_text(
        75.5, 317.0,
        text = "Employee_no",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        73.5, 370.0,
        text = "Title",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        454.5, 317.0,
        text = "Name",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        75.5, 420.0,
        text = "Salary",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        75.5, 470.0,
        text = "Hire_Date",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        454.5, 368.0,
        text = "Birth_Date",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    canvas.create_text(
        454.5, 419.0,
        text = "Gender",
        fill = "#ffffff",
        font = ("OpenSans-SemiBold", int(12.0)))

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        201.5, 315.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 144, y = 300,
        width = 115,
        height = 29)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        202.5, 366.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 145, y = 351,
        width = 115,
        height = 29)

    entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas.create_image(
        553.5, 315.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 496, y = 300,
        width = 115,
        height = 29)

    entry3_img = PhotoImage(file = f"img_textBox3.png")
    entry3_bg = canvas.create_image(
        553.5, 367.5,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry3.place(
        x = 496, y = 352,
        width = 115,
        height = 29)

    entry4_img = PhotoImage(file = f"img_textBox4.png")
    entry4_bg = canvas.create_image(
        553.5, 420.5,
        image = entry4_img)

    entry4 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry4.place(
        x = 496, y = 405,
        width = 115,
        height = 29)

    entry5_img = PhotoImage(file = f"img_textBox5.png")
    entry5_bg = canvas.create_image(
        201.5, 417.5,
        image = entry5_img)

    entry5 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry5.place(
        x = 144, y = 402,
        width = 115,
        height = 29)

    entry6_img = PhotoImage(file = f"img_textBox6.png")
    entry6_bg = canvas.create_image(
        201.5, 466.5,
        image = entry6_img)

    entry6 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry6.place(
        x = 144, y = 451,
        width = 115,
        height = 29)

    window.resizable(False, False)
    window.mainloop()

