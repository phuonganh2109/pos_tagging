import tkinter as tk
import random
from nltk.tokenize import word_tokenize
import project as n

punc = '''!()[]{};:'"\, <>./?@#$%^&*_~-...”“'''


def close_program():
    new_root.destroy()


def colorize(root, res):
    # color dictionary
    color_dic = {
        "N": '#87CEEB',
        "PU": '#CAE1FF',
        "A": '#00F5FF',
        "C": '#9C661F',
        "E": '#FFAAA5',
        "V": '#EE00EE',
        "R": '#C0C0C0',
        "Q": '#45A29E',
        "P": '#00FF7F',
        "I": '#7171C6',
        "Na": '#FFFF00',
        "L": '#FFA500',
        "X": '#DC143C'
    }
    #res = """OKOKOKOK"""
    result = tk.Text(root, height=10, width=45, bg='white')
    #result.insert(tk.END, res)
    result.place(x=68, y=220)
    result.configure(state="disabled")

    #list_key = list(res.keys())

    for r in range(len(res)):
        if res[r][-1] == 'N':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'PU':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'A':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'C':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'E':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'V':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'R':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'Q':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'P':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'I':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'Na':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'L':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)
        elif res[r][-1] == 'X':
            text = tk.Label(
                result, text=res[r][0], bg=color_dic[res[r][-1]])
            text.pack(padx=2, pady=20, side=tk.LEFT)


def new_init():
    new_root.destroy()
    global root
    root = tk.Tk()
    root.title("POS TAGGING")
    root.geometry("700x500+250+35")

    # create canvas
    canvas = tk.Canvas(root, width=700, height=500)
    canvas.pack()

    # create input box
    sen_entry = tk.Entry(root, width=60)
    canvas.create_window(260, 140, window=sen_entry)

    # draw text
    label = tk.Label(root, text="Nhập dữ liệu: ")
    canvas.create_window(40, 140, window=label)

    # create POS lists
    N = tk.Label(root, text='N: Danh từ',
                 bg='#87CEEB', width=20, anchor='w')
    canvas.create_window(570, 28, window=N)

    pu_tag = tk.Label(root, text='PU: Dấu câu',
                      bg='#CAE1FF', width=20, anchor='w')
    canvas.create_window(570, 58, window=pu_tag)

    A = tk.Label(root, text='A: Tính từ',
                 bg='#00F5FF', width=20, anchor='w')
    canvas.create_window(570, 88, window=A)

    C = tk.Label(root, text='C: Giới từ/Liên từ',
                 bg='#9C661F', width=20, anchor='w')
    canvas.create_window(570, 118, window=C)

    E = tk.Label(root, text='E: Cảm từ',
                 bg='#FFAAA5', width=20, anchor='w')
    canvas.create_window(570, 148, window=E)

    V = tk.Label(root, text='V: Động từ',
                 bg='#EE00EE', width=20, anchor='w')
    canvas.create_window(570, 178, window=V)

    R = tk.Label(root, text='R: Phụ từ',
                 bg='#C0C0C0', width=20, anchor='w')
    canvas.create_window(570, 208, window=R)

    Q = tk.Label(root, text='Q: Danh từ số lượng',
                 bg='#45A29E', width=20, anchor='w')
    canvas.create_window(570, 238, window=Q)

    P = tk.Label(root, text='P: Đại từ',
                 bg='#00FF7F', width=20, anchor='w')
    canvas.create_window(570, 268, window=P)

    I = tk.Label(root, text='I: Trợ từ',
                 bg='#7171C6', width=20, anchor='w')
    canvas.create_window(570, 298, window=I)

    Na = tk.Label(root, text='Na: Danh từ trừu tượng',
                  bg='#FFFF00', width=20, anchor='w')
    canvas.create_window(570, 328, window=Na)

    L = tk.Label(root, text='L: Phó danh từ chỉ loại',
                 bg='#FFA500', width=20, anchor='w')
    canvas.create_window(570, 358, window=L)

    X = tk.Label(root, text='X: Không xác định',
                 bg='#DC143C', width=20, anchor='w')
    canvas.create_window(570, 388, window=X)

    # get sentence from input box
    def getSentence():
        words = sen_entry.get()
        root.destroy()
        global new_root
        new_root = tk.Tk()
        new_root.title("POS TAGGING")
        new_root.geometry("700x500+250+35")

        # create canvas
        canvas = tk.Canvas(new_root, width=700, height=500)
        canvas.pack()

        # create input box
        # sen_entry = tk.Entry(root, width = 60)
        # canvas.create_window(250,140,window=sen_entry)

        # draw text
        label = tk.Label(new_root, text="Kết quả: ")
        label.config(font=(40))
        canvas.create_window(50, 180, window=label)

        # create POS lists
        N = tk.Label(new_root, text='N: Danh từ',
                     bg='#87CEEB', width=20, anchor='w')
        canvas.create_window(570, 28, window=N)

        pu_tag = tk.Label(new_root, text='PU: Dấu câu',
                          bg='#CAE1FF', width=20, anchor='w')
        canvas.create_window(570, 58, window=pu_tag)

        A = tk.Label(new_root, text='A: Tính từ',
                     bg='#00F5FF', width=20, anchor='w')
        canvas.create_window(570, 88, window=A)

        C = tk.Label(new_root, text='C: Giới từ/Liên từ',
                     bg='#9C661F', width=20, anchor='w')
        canvas.create_window(570, 118, window=C)

        E = tk.Label(new_root, text='E: Cảm từ',
                     bg='#FFAAA5', width=20, anchor='w')
        canvas.create_window(570, 148, window=E)

        V = tk.Label(new_root, text='V: Động từ',
                     bg='#EE00EE', width=20, anchor='w')
        canvas.create_window(570, 178, window=V)

        R = tk.Label(new_root, text='R: Phụ từ',
                     bg='#C0C0C0', width=20, anchor='w')
        canvas.create_window(570, 208, window=R)

        Q = tk.Label(new_root, text='Q: Danh từ số lượng',
                     bg='#45A29E', width=20, anchor='w')
        canvas.create_window(570, 238, window=Q)

        P = tk.Label(new_root, text='P: Đại từ',
                     bg='#00FF7F', width=20, anchor='w')
        canvas.create_window(570, 268, window=P)

        I = tk.Label(new_root, text='I: Trợ từ',
                     bg='#7171C6', width=20, anchor='w')
        canvas.create_window(570, 298, window=I)

        Na = tk.Label(new_root, text='Na: Danh từ trừu tượng',
                      bg='#FFFF00', width=20, anchor='w')
        canvas.create_window(570, 328, window=Na)

        L = tk.Label(new_root, text='L: Phó danh từ chỉ loại',
                     bg='#FFA500', width=20, anchor='w')
        canvas.create_window(570, 358, window=L)

        X = tk.Label(new_root, text='X: Không xác định',
                     bg='#DC143C', width=20, anchor='w')
        canvas.create_window(570, 388, window=X)

        quit_btn = tk.Button(new_root, text='Thoát chương trình',
                             command=close_program, bg='#D8BFD8')
        canvas.create_window(260, 460, window=quit_btn)

        back_btn = tk.Button(
            new_root, text='Nhập tiếp chuỗi mới', command=new_init, bg='#D8BFD8')
        canvas.create_window(420, 460, window=back_btn)

        model = n.POS_tag(words, punc)
        model.read_automate_File()
        a = model.buildG()
        colorize(new_root, a)
        new_root.mainloop()

    # #button to get sentence from GUI
    btn = tk.Button(root, text='POS-tag!', command=getSentence, bg='#D8BFD8')
    canvas.create_window(410, 180, window=btn)
    root.mainloop()


def init():
    global root
    root = tk.Tk()
    root.title("POS TAGGING")
    root.geometry("700x500+250+35")

    # create canvas
    canvas = tk.Canvas(root, width=700, height=500)
    canvas.pack()

    # create input box
    sen_entry = tk.Entry(root, width=60)
    canvas.create_window(260, 140, window=sen_entry)

    # draw text
    label = tk.Label(root, text="Nhập dữ liệu: ")
    canvas.create_window(40, 140, window=label)

    # create POS lists
    N = tk.Label(root, text='N: Danh từ',
                 bg='#87CEEB', width=20, anchor='w')
    canvas.create_window(570, 28, window=N)

    pu_tag = tk.Label(root, text='PU: Dấu câu',
                      bg='#CAE1FF', width=20, anchor='w')
    canvas.create_window(570, 58, window=pu_tag)

    A = tk.Label(root, text='A: Tính từ',
                 bg='#00F5FF', width=20, anchor='w')
    canvas.create_window(570, 88, window=A)

    C = tk.Label(root, text='C: Giới từ/Liên từ',
                 bg='#9C661F', width=20, anchor='w')
    canvas.create_window(570, 118, window=C)

    E = tk.Label(root, text='E: Cảm từ',
                 bg='#FFAAA5', width=20, anchor='w')
    canvas.create_window(570, 148, window=E)

    V = tk.Label(root, text='V: Động từ',
                 bg='#EE00EE', width=20, anchor='w')
    canvas.create_window(570, 178, window=V)

    R = tk.Label(root, text='R: Phụ từ',
                 bg='#C0C0C0', width=20, anchor='w')
    canvas.create_window(570, 208, window=R)

    Q = tk.Label(root, text='Q: Danh từ số lượng',
                 bg='#45A29E', width=20, anchor='w')
    canvas.create_window(570, 238, window=Q)

    P = tk.Label(root, text='P: Đại từ',
                 bg='#00FF7F', width=20, anchor='w')
    canvas.create_window(570, 268, window=P)

    I = tk.Label(root, text='I: Trợ từ',
                 bg='#7171C6', width=20, anchor='w')
    canvas.create_window(570, 298, window=I)

    Na = tk.Label(root, text='Na: Danh từ trừu tượng',
                  bg='#FFFF00', width=20, anchor='w')
    canvas.create_window(570, 328, window=Na)

    L = tk.Label(root, text='L: Phó danh từ chỉ loại',
                 bg='#FFA500', width=20, anchor='w')
    canvas.create_window(570, 358, window=L)

    X = tk.Label(root, text='X: Không xác định',
                 bg='#DC143C', width=20, anchor='w')
    canvas.create_window(570, 388, window=X)

    # get sentence from input box
    def getSentence():
        words = sen_entry.get()
        root.destroy()
        global new_root
        new_root = tk.Tk()
        new_root.title("POS TAGGING")
        new_root.geometry("700x500+250+35")

        # create canvas
        canvas = tk.Canvas(new_root, width=700, height=500)
        canvas.pack()

        # create input box
        # sen_entry = tk.Entry(root, width = 60)
        # canvas.create_window(250,140,window=sen_entry)

        # draw text
        label = tk.Label(new_root, text="Kết quả: ")
        label.config(font=(40))
        canvas.create_window(50, 180, window=label)

        # create POS lists
        N = tk.Label(new_root, text='N: Danh từ',
                     bg='#87CEEB', width=20, anchor='w')
        canvas.create_window(570, 28, window=N)

        pu_tag = tk.Label(new_root, text='PU: Dấu câu',
                          bg='#CAE1FF', width=20, anchor='w')
        canvas.create_window(570, 58, window=pu_tag)

        A = tk.Label(new_root, text='A: Tính từ',
                     bg='#00F5FF', width=20, anchor='w')
        canvas.create_window(570, 88, window=A)

        C = tk.Label(new_root, text='C: Giới từ/Liên từ',
                     bg='#9C661F', width=20, anchor='w')
        canvas.create_window(570, 118, window=C)

        E = tk.Label(new_root, text='E: Cảm từ',
                     bg='#FFAAA5', width=20, anchor='w')
        canvas.create_window(570, 148, window=E)

        V = tk.Label(new_root, text='V: Động từ',
                     bg='#EE00EE', width=20, anchor='w')
        canvas.create_window(570, 178, window=V)

        R = tk.Label(new_root, text='R: Phụ từ',
                     bg='#C0C0C0', width=20, anchor='w')
        canvas.create_window(570, 208, window=R)

        Q = tk.Label(new_root, text='Q: Danh từ số lượng',
                     bg='#45A29E', width=20, anchor='w')
        canvas.create_window(570, 238, window=Q)

        P = tk.Label(new_root, text='P: Đại từ',
                     bg='#00FF7F', width=20, anchor='w')
        canvas.create_window(570, 268, window=P)

        I = tk.Label(new_root, text='I: Trợ từ',
                     bg='#7171C6', width=20, anchor='w')
        canvas.create_window(570, 298, window=I)

        Na = tk.Label(new_root, text='Na: Danh từ trừu tượng',
                      bg='#FFFF00', width=20, anchor='w')
        canvas.create_window(570, 328, window=Na)

        L = tk.Label(new_root, text='L: Phó danh từ chỉ loại',
                     bg='#FFA500', width=20, anchor='w')
        canvas.create_window(570, 358, window=L)

        X = tk.Label(new_root, text='X: Không xác định',
                     bg='#DC143C', width=20, anchor='w')
        canvas.create_window(570, 388, window=X)

        quit_btn = tk.Button(new_root, text='Thoát chương trình',
                             command=close_program, bg='#D8BFD8')
        canvas.create_window(260, 460, window=quit_btn)

        back_btn = tk.Button(
            new_root, text='Nhập tiếp chuỗi mới', command=new_init, bg='#D8BFD8')
        canvas.create_window(420, 460, window=back_btn)

        model = n.POS_tag(words, punc)
        model.read_automate_File()
        a = model.buildG()
        colorize(new_root, a)
        new_root.mainloop()

    # #button to get sentence from GUI
    btn = tk.Button(root, text='POS-tag!', command=getSentence, bg='#D8BFD8')
    canvas.create_window(410, 180, window=btn)
    root.mainloop()


init()
