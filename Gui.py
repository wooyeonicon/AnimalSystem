# 作者 : 杨航
# 开发时间 : 2022/9/30 17:28
import tkinter
from tkinter import ttk, messagebox
import due

class Main():
    def __init__(self,master):
        self.root = master
        self.root.geometry("1000x1000")  # 设置窗体大小
        self.root.title('产生式系统')

        global f1,f2,f3,f4
        f1 = tkinter.StringVar()
        f2 = tkinter.StringVar()
        f3 = tkinter.StringVar()
        f4 = tkinter.StringVar()
        self.page = tkinter.Frame(self.root)  # 定义一张纸
        self.page.pack()
        tkinter.Label(self.page).grid(row=0,column=0)

        tkinter.Label(self.page,text='事实一').grid(row=1,column=1)
        tkinter.Entry(self.page,textvariable=f1).grid(row=1,column=2)

        tkinter.Label(self.page,text='事实二').grid(row=2,column=1,pady=10)
        tkinter.Entry(self.page,textvariable=f2).grid(row=2,column=2)

        tkinter.Label(self.page,text='事实三').grid(row=3,column=1,pady=10)
        tkinter.Entry(self.page,textvariable=f3).grid(row=3,column=2)

        tkinter.Label(self.page,text='事实四').grid(row=4,column=1,pady=10)
        tkinter.Entry(self.page,textvariable=f4).grid(row=4,column=2)

        menubar = tkinter.Menu(self.root)
        filemenu = tkinter.Menu(menubar,tearoff=False)
        filemenu.add_command(label='添加',command=self.add)
        filemenu.add_command(label='修改',command=self.update)
        filemenu.add_command(label='删除',command=self.delete)
        filemenu.add_separator()
        filemenu.add_command(label='退出',command=self.out)
        menubar.add_cascade(label='菜单',menu=filemenu)
        self.root.config(menu=menubar)  # 显示菜单

        tkinter.Button(self.page, text='正向推理', command=self.search).grid(row=5, column=1, pady=10)
        tkinter.Button(self.page, text='反向推理', command=self.back).grid(row=5, column=2, pady=10)

        # 查看所有知识
        # self.page2 = tkinter.Frame(self.root)
        # self.page2.pack()
        tkinter.Button(self.page, text='查看知识', command=self.searchFeatures).grid(row=8, column=1, pady=10)
        tkinter.Button(self.page, text='刷新', command=self.searchFeatures).grid(row=8, column=2, pady=10)
        # 查看所有规则
        tkinter.Button(self.page, text='查看规则', command=self.searchRelu).grid(row=9, column=1, pady=10)
        tkinter.Button(self.page, text='刷新', command=self.searchRelu).grid(row=9, column=2, pady=10)

    def out(self,page):
        page.destroy()
        Main(self.root)
    # 查看所有知识
    def searchFeatures(self):
        columns = ('id', 'features')
        columns_value = ('id', 'features')
        self.tree_view = ttk.Treeview(self.root, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('features', width=300, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('features', text='features')
        # self.tree_view.pack(fill=tkinter.X, expand=True)
        self.tree_view.pack(side=tkinter.LEFT, expand=True)
        # 删除旧的结点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        relus = due.search_feature()
        index = 0
        for relu in relus:
            self.tree_view.insert('', index + 1, values=(
                relu['id'],
                relu['features']
            ))
            index += 1
        self.page.destroy()

    # 查看所有规则
    def searchRelu(self):
        columns = ('id','f1', 'f2','f3','f4','console')
        columns_value = ('id','f1', 'f2','f3','f4','console')
        self.tree_view = ttk.Treeview(self.root, show='headings', columns=columns)
        self.tree_view.column('id', width=40, anchor='center')
        self.tree_view.column('f1', width=40, anchor='center')
        self.tree_view.column('f2', width=40, anchor='center')
        self.tree_view.column('f3', width=40, anchor='center')
        self.tree_view.column('f4', width=40, anchor='center')
        self.tree_view.column('console', width=40, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('f1', text='f1')
        self.tree_view.heading('f2', text='f2')
        self.tree_view.heading('f3', text='f3')
        self.tree_view.heading('f4', text='f4')
        self.tree_view.heading('console', text='console')
        # self.tree_view.pack(fill=tkinter.Y,expand=True)
        self.tree_view.pack(side=tkinter.LEFT, expand=True)
        # 删除旧的结点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        relus = due.searchRelu()
        index = 0
        for relu in relus:
            self.tree_view.insert('', index + 1, values=(
                relu['id'],
                relu['f1'],
                relu['f2'],
                relu['f3'],
                relu['f4'],
                relu['console']
            ))
            index += 1
        self.page.destroy()

    def search(self):
        self.page.destroy()
        Search(self.root)  # 跳转页面
    def back(self):
        self.page.destroy()
        Back(self.root)
    def add(self):
        self.page.destroy()
        Add(self.root)
    def update(self):
        self.page.destroy()
        Update(self.root)
    def delete(self):
        self.page.destroy()
        Delete(self.root)

# 正向推理
class Search(tkinter.Frame):
    def __init__(self,master=None):
        self.root = tkinter.Tk()
        # self.root = master
        self.root.geometry('600x400')
        self.root.title('产生式查询结果')
        self.create_page_search()
        self.create_page()


    def create_page_search(self):
        menubar = tkinter.Menu(self.root)
        menubar.add_command(label='退出',command=self.out)
        self.root['menu'] = menubar

    def out(self):  # 退出
        Main(self.root)


    def create_page(self):
        columns = ('id','relu')
        columns_value = ('id','relu')
        self.tree_view = ttk.Treeview(self.root,show='headings',columns=columns)
        self.tree_view.column('id',width=80,anchor='center')
        self.tree_view.column('relu', width=300, anchor='center')
        self.tree_view.heading('id',text='id')
        self.tree_view.heading('relu', text='relu')
        self.tree_view.pack(fill=tkinter.BOTH,expand=True)
        self.show_result()

    def show_result(self):
        # 删除旧的结点
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass
        relus = due.forward(int(f1.get()), int(f2.get()), int(f3.get()), int(f4.get()))
        relu_s = relus[0]

        index = 0
        for relu in relu_s:
            print(relu)
            self.tree_view.insert('',index+1,values=(
                relu['id'],
                relu['relu']
            ))
            index += 1
        if relus[1] != None:
            messagebox.showinfo('结果', relus[1])
        else:
            messagebox.showerror('结果', None)

# 反向推理
class Back(object):
    def __init__(self,master=None):
        self.root = tkinter.Tk()
        # self.root = master
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.root.geometry('600x400')
        self.root.title('反向推理')
        global f5
        f5 = tkinter.StringVar()
        tkinter.Label(self.page1, text='结论').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page1, textvariable=f5).grid(row=3, column=2)
        tkinter.Button(self.page1, text='反向推理', command=self.back_result).grid(row=7, column=1, pady=10)

    def back_result(self):
        columns = ('id', 'relu')
        columns_value = ('id', 'relu')
        self.tree_view = ttk.Treeview(self.root, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('relu', width=300, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('relu', text='relu')
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)

        # 删除旧的结点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        relus = due.backward(int(f5.get()))
        relu_s = relus[0]

        index = 0
        for relu in relu_s:
            print(relu)
            self.tree_view.insert('', index + 1, values=(
                relu['id'],
                relu['relu']
            ))
            index += 1
        if relus[1] != None:
            messagebox.showinfo('结果', relus[1])
        else:
            messagebox.showerror('结果', None)

# 添加
class Add(object):
    def __init__(self, master=None):
        # self.root = tkinter.Tk()
        self.root = master
        self.page4 = tkinter.Frame(self.root)
        self.page4.pack(side=tkinter.LEFT,expand=True)
        self.page5 = tkinter.Frame(self.root)
        self.page5.pack(side=tkinter.LEFT,expand=True)
        self.root.geometry('600x600')
        self.root.title('添加')

        global f6
        f6 = tkinter.StringVar()
        tkinter.Label(self.page4, text='知识').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page4, textvariable=f6).grid(row=3, column=2)
        tkinter.Button(self.page4, text='添加知识', command=self.addFeatures).grid(row=8, column=1, pady=10)

        global f7,f8,f9,f10,consoles
        f7 = tkinter.StringVar()
        f8 = tkinter.StringVar()
        f9 = tkinter.StringVar()
        f10 = tkinter.StringVar()
        consoles = tkinter.StringVar()
        tkinter.Label(self.page5, text='f1').grid(row=1, column=1, pady=10)
        tkinter.Entry(self.page5, textvariable=f7).grid(row=1, column=2)
        tkinter.Label(self.page5, text='f2').grid(row=2, column=1, pady=10)
        tkinter.Entry(self.page5, textvariable=f8).grid(row=2, column=2)
        tkinter.Label(self.page5, text='f3').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page5, textvariable=f9).grid(row=3, column=2)
        tkinter.Label(self.page5, text='f4').grid(row=4, column=1, pady=10)
        tkinter.Entry(self.page5, textvariable=f10).grid(row=4, column=2)
        tkinter.Label(self.page5, text='consoles').grid(row=5, column=1, pady=10)
        tkinter.Entry(self.page5, textvariable=consoles).grid(row=5, column=2)
        tkinter.Button(self.page5, text='添加规则', command=self.addRelu).grid(row=8, column=2, pady=10)

    def addFeatures(self):
        message = due.add_feature(f6.get())
        if message == 1:
            messagebox.showinfo("添加成功！",'添加成功')
        else:
            messagebox.showerror("添加失败！",'添加失败')

    def addRelu(self):
        message = due.data_relu(f7.get(),f8.get(),f9.get(),f10.get(),consoles.get())
        if message == 1:
            messagebox.showinfo("添加成功！", '添加成功')
        else:
            messagebox.showerror("添加失败！", '添加失败')

# 修改
class Update(object):
    def __init__(self, master=None):
        self.root = tkinter.Tk()
        # self.root = master
        self.page6 = tkinter.Frame(self.root)
        self.page6.pack(side=tkinter.LEFT,expand=True)
        self.page7 = tkinter.Frame(self.root)
        self.page7.pack(side=tkinter.LEFT,expand=True)
        self.root.geometry('600x600')
        self.root.title('修改')
        global f11,f12
        f11 = tkinter.StringVar()
        f12 = tkinter.StringVar()
        tkinter.Label(self.page6, text='id').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page6, textvariable=f11).grid(row=3, column=2)
        tkinter.Label(self.page6, text='features').grid(row=4, column=1, pady=10)
        tkinter.Entry(self.page6, textvariable=f12).grid(row=4, column=2)
        tkinter.Button(self.page6, text='修改知识', command=self.updateFeatures).grid(row=8, column=1, pady=10)

        global f13,f14,f15,f16,f17,consoles_s
        f13 = tkinter.StringVar()
        f14 = tkinter.StringVar()
        f15 = tkinter.StringVar()
        f16 = tkinter.StringVar()
        f17 = tkinter.StringVar()
        consoles_s = tkinter.StringVar()

        tkinter.Label(self.page7, text='id').grid(row=1, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=f13).grid(row=1, column=2)
        tkinter.Label(self.page7, text='f1').grid(row=2, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=f14).grid(row=2, column=2)
        tkinter.Label(self.page7, text='f2').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=f15).grid(row=3, column=2)
        tkinter.Label(self.page7, text='f3').grid(row=4, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=f16).grid(row=4, column=2)
        tkinter.Label(self.page7, text='f4').grid(row=5, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=f17).grid(row=5, column=2)
        tkinter.Label(self.page7, text='consoles').grid(row=6, column=1, pady=10)
        tkinter.Entry(self.page7, textvariable=consoles_s).grid(row=6, column=2)
        tkinter.Button(self.page7, text='修改规则', command=self.updateRelu).grid(row=8, column=2, pady=10)
    def updateFeatures(self):
        message = due.update_feature(int(f11.get()),f12.get())
        if message == 1:
            messagebox.showinfo("修改知识！",'修改成功')
        else:
            messagebox.showerror("修改知识！",'修改失败')

    def updateRelu(self):
        message = due.update_relu(int(f13.get()),int(f14.get()),int(f15.get()),int(f16.get()),int(f17.get()),int(consoles_s.get()))
        if message == 1:
            messagebox.showinfo("修改规则！", '修改成功')
        else:
            messagebox.showerror("修改规则！", '修改失败')

# 删除
class Delete(object):
    def __init__(self, master=None):
        self.root = tkinter.Tk()
        # self.root = master
        self.page8 = tkinter.Frame(self.root)
        self.page8.pack(side=tkinter.LEFT,expand=True)
        self.page9 = tkinter.Frame(self.root)
        self.page9.pack(side=tkinter.LEFT,expand=True)
        self.root.geometry('600x600')
        self.root.title('删除')
        global f18,f19
        f18 = tkinter.StringVar()
        f19 = tkinter.StringVar()
        tkinter.Label(self.page8, text='id').grid(row=3, column=1, pady=10)
        tkinter.Entry(self.page8, textvariable=f18).grid(row=3, column=2)
        tkinter.Button(self.page8, text='删除知识', command=self.deleteFeatures).grid(row=8, column=1, pady=10)

        tkinter.Label(self.page9, text='id').grid(row=4, column=1, pady=10)
        tkinter.Entry(self.page9, textvariable=f19).grid(row=4, column=2)
        tkinter.Button(self.page9, text='删除规则', command=self.deleteRelu).grid(row=8, column=2, pady=10)
    def deleteFeatures(self):
        message = due.delete_feature(int(f18.get()))
        if message == 1:
            messagebox.showinfo("删除知识！",'删除成功')
        else:
            messagebox.showerror("删除知识！",'删除失败')

    def deleteRelu(self):
        message = due.delete_relu(int(f19.get()))
        if message == 1:
            messagebox.showinfo("删除规则！", '删除成功')
        else:
            messagebox.showerror("删除规则！", '删除失败')

if __name__ == '__main__':
    root = tkinter.Tk()
    Main(master=root)
    root.mainloop()