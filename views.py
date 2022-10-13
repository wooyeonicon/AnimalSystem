# 作者 : 杨航
# 开发时间 : 2022/10/4 17:54
import tkinter
import due
from tkinter import ttk, messagebox


class About_searchF(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.table_view = tkinter.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        columns = ('id', 'features')
        columns_value = ('id', 'features')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('features', width=300, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('features', text='features')
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)
        # self.tree_view.pack(side=tkinter.BOTH, expand=True)
        self.show_data()
        tkinter.Button(self,text='刷新数据',command=self.show_data).pack(anchor=tkinter.E,pady=5)
    def show_data(self):
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

class About_searchR(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.table_view = tkinter.Frame()
        self.table_view.pack()
        self.create_page()
    def create_page(self):
        columns = ('id', 'f1', 'f2', 'f3', 'f4', 'console')
        columns_value = ('id', 'f1', 'f2', 'f3', 'f4', 'console')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
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
        self.tree_view.pack(fill=tkinter.BOTH,expand=True)
        self.show_data()
        tkinter.Button(self, text='刷新数据', command=self.show_data).pack(anchor=tkinter.E, pady=5)
    def show_data(self):
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

class About_addF(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.status = tkinter.StringVar()
        self.f6 = tkinter.StringVar()
        self.create_page()

    def create_page(self):
        tkinter.Label(self).grid(row=0,pady=10)
        tkinter.Label(self,text='知识').grid(row=3,column=1, pady=1)
        tkinter.Entry(self, textvariable=self.f6).grid(row=3, column=2)
        tkinter.Button(self, text='添加知识', command=self.addFeatures).grid(row=4, column=2, pady=10)
        tkinter.Label(self,textvariable=self.status).grid(row=5,column=2,pady=10,stick=tkinter.E)
    def addFeatures(self):
        message = due.add_feature(self.f6.get())
        if message == 1:
            messagebox.showinfo("添加成功！",'添加成功')
            self.status.set('获取数据成功')
        else:
            messagebox.showerror("添加失败！",'添加失败')
        self.f6.set('')

class About_addR(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f7 = tkinter.StringVar()
        self.f8 = tkinter.StringVar()
        self.f9 = tkinter.StringVar()
        self.f10 = tkinter.StringVar()
        self.consoles = tkinter.StringVar()
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text='f1').grid(row=1, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f7).grid(row=1, column=2)
        tkinter.Label(self, text='f2').grid(row=2, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f8).grid(row=2, column=2)
        tkinter.Label(self, text='f3').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f9).grid(row=3, column=2)
        tkinter.Label(self, text='f4').grid(row=4, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f10).grid(row=4, column=2)
        tkinter.Label(self, text='consoles').grid(row=5, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.consoles).grid(row=5, column=2)
        tkinter.Button(self, text='添加规则', command=self.addRelu).grid(row=8, column=2, pady=10)
    def addRelu(self):
        message = due.data_relu(int(self.f7.get()),int(self.f8.get()),int(self.f9.get()),int(self.f10.get()),int(self.consoles.get()))
        if message == 1:
            messagebox.showinfo("添加成功！", '添加成功')
        else:
            messagebox.showerror("添加失败！", '添加失败')
        self.f7.set('')
        self.f8.set('')
        self.f9.set('')
        self.f10.set('')
        self.consoles.set('')

class About_updateF(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f11 = tkinter.StringVar()
        self.f12 = tkinter.StringVar()
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text='id').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f11).grid(row=3, column=2)
        tkinter.Label(self, text='features').grid(row=4, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f12).grid(row=4, column=2)
        tkinter.Button(self, text='修改知识', command=self.updateFeatures).grid(row=8, column=1, pady=10)
    def updateFeatures(self):
        message = due.update_feature(int(self.f11.get()),self.f12.get())
        if message == 1:
            messagebox.showinfo("修改知识！",'修改成功')
        else:
            messagebox.showerror("修改知识！",'修改失败')
        self.f11.set('')
        self.f12.set('')

class About_updateR(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f13 = tkinter.StringVar()
        self.f14 = tkinter.StringVar()
        self.f15 = tkinter.StringVar()
        self.f16 = tkinter.StringVar()
        self.f17 = tkinter.StringVar()
        self.consoles_s = tkinter.StringVar()
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text='id').grid(row=1, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f13).grid(row=1, column=2)
        tkinter.Label(self, text='f1').grid(row=2, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f14).grid(row=2, column=2)
        tkinter.Label(self, text='f2').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f15).grid(row=3, column=2)
        tkinter.Label(self, text='f3').grid(row=4, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f16).grid(row=4, column=2)
        tkinter.Label(self, text='f4').grid(row=5, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f17).grid(row=5, column=2)
        tkinter.Label(self, text='consoles').grid(row=6, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.consoles_s).grid(row=6, column=2)
        tkinter.Button(self, text='修改规则', command=self.updateRelu).grid(row=8, column=2, pady=10)
    def updateRelu(self):
        message = due.update_relu(int(self.f13.get()),int(self.f14.get()),int(self.f15.get()),int(self.f16.get()),int(self.f17.get()),int(self.consoles_s.get()))
        if message == 1:
            messagebox.showinfo("修改规则！", '修改成功')
        else:
            messagebox.showerror("修改规则！", '修改失败')
        self.f13.set('')
        self.f14.set('')
        self.f15.set('')
        self.f16.set('')
        self.f17.set('')
        self.consoles_s.set('')

class About_deleteF(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f18 = tkinter.StringVar()
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text='id').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f18).grid(row=3, column=2)
        tkinter.Button(self, text='删除知识', command=self.deleteFeatures).grid(row=8, column=1, pady=10)
    def deleteFeatures(self):
        message = due.delete_feature(int(self.f18.get()))
        if message == 1:
            messagebox.showinfo("删除知识！",'删除成功')
        else:
            messagebox.showerror("删除知识！",'删除失败')
        self.f18.set('')

class About_deleteR(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f19 = tkinter.StringVar()
        self.cteate_page()
    def cteate_page(self):
        tkinter.Label(self, text='id').grid(row=4, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.f19).grid(row=4, column=2)
        tkinter.Button(self, text='删除规则', command=self.deleteRelu).grid(row=8, column=2, pady=10)
    def deleteRelu(self):
        message = due.delete_relu(int(self.f19.get()))
        if message == 1:
            messagebox.showinfo("删除规则！", '删除成功')
        else:
            messagebox.showerror("删除规则！", '删除失败')
        self.f19.set('')

class About_forward(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f1 = tkinter.StringVar()
        self.f2 = tkinter.StringVar()
        self.f3 = tkinter.StringVar()
        self.f4 = tkinter.StringVar()
        self.table_view = tkinter.Frame()
        self.table_view.pack()
        self.create_page()
    def create_page(self):
        tkinter.Label(self, text='事实一').pack()
        tkinter.Entry(self, textvariable=self.f1).pack()
        tkinter.Label(self, text='事实二').pack()
        tkinter.Entry(self, textvariable=self.f2).pack()
        tkinter.Label(self, text='事实三').pack()
        tkinter.Entry(self, textvariable=self.f3).pack()
        tkinter.Label(self, text='事实四').pack()
        tkinter.Entry(self, textvariable=self.f4).pack()
        tkinter.Button(self, text='正向推理', command=self.search).pack()
    def search(self):
        columns = ('id', 'relu')
        columns_value = ('id', 'relu')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('relu', width=300, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('relu', text='relu')
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)
        self.show_data()
    def show_data(self):
        # 删除旧的结点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        relus = due.forward(int(self.f1.get()), int(self.f2.get()), int(self.f3.get()), int(self.f4.get()))
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
        self.f1.set('')
        self.f2.set('')
        self.f3.set('')
        self.f4.set('')
        self.table_view.pack_forget()

class About_backward(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.f5 = tkinter.StringVar()
        self.table_view = tkinter.Frame()
        self.table_view.pack()
        self.create_page()


    def create_page(self):
        # tkinter.Label(self, text='结论').grid(row=3, column=1, pady=10)
        # tkinter.Entry(self, textvariable=self.f5).grid(row=3, column=2)
        # tkinter.Button(self, text='反向推理', command=self.back_result).grid(row=7, column=1, pady=10)
        tkinter.Label(self, text='结论').pack()
        tkinter.Entry(self, textvariable=self.f5).pack()
        tkinter.Button(self, text='反向推理', command=self.back_result).pack()
    def back_result(self):
        columns = ('id', 'relu')
        columns_value = ('id', 'relu')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.column('relu', width=300, anchor='center')
        self.tree_view.heading('id', text='id')
        self.tree_view.heading('relu', text='relu')
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)
        self.show_data()
    def show_data(self):
        # 删除旧的结点
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        relus = due.backward(int(self.f5.get()))
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

        self.f5.set('') # 把原来的值设置为空
        self.table_view.pack_forget()