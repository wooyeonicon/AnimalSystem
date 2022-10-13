# 作者 : 杨航
# 开发时间 : 2022/10/4 17:29

import tkinter
from tkinter import ttk, messagebox
from views import About_searchF,About_searchR,About_addF,About_addR,About_updateF,About_updateR,About_deleteF,About_deleteR,About_forward,About_backward
import due

class Main():
    def __init__(self,master):
        self.root = master
        self.root.geometry("1000x1000")  # 设置窗体大小
        self.root.title('产生式系统')
        self.create_page()

    def create_page(self):
        self.about_searchF = About_searchF(self.root)
        self.about_searchR = About_searchR(self.root)
        self.about_addF = About_addF(self.root)
        self.about_addR = About_addR(self.root)
        self.about_updateF = About_updateF(self.root)
        self.about_updateR = About_updateR(self.root)
        self.about_deleteF = About_deleteF(self.root)
        self.about_deleteR = About_deleteR(self.root)
        self.about_forward = About_forward(self.root)
        self.about_backward = About_backward(self.root)


        menubar = tkinter.Menu(self.root)
        menubar.add_command(label='查看知识',command=self.searchFeatures)
        menubar.add_command(label='查看规则',command=self.searchRelu)
        menubar.add_command(label='添加知识',command=self.addFeatures)
        menubar.add_command(label='添加规则',command=self.addRule)
        menubar.add_command(label='修改知识',command=self.updateFeatures)
        menubar.add_command(label='修改规则',command=self.updateRelu)
        menubar.add_command(label='删除知识',command=self.deleteFeatures)
        menubar.add_command(label='删除规则',command=self.deleteRelu)
        menubar.add_command(label='正向推理',command=self.forward)
        menubar.add_command(label='反向推理',command=self.backward)
        self.root['menu'] = menubar


    # 查看所有知识
    def searchFeatures(self):
        self.about_searchF.pack()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()

    # 查看所有规则
    def searchRelu(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()

    def addFeatures(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()


    def addRule(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()

    def updateFeatures(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()
    def updateRelu(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()
    def deleteFeatures(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()
    def deleteRelu(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack()
        self.about_forward.pack_forget()
        self.about_backward.pack_forget()
    def forward(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack()
        self.about_backward.pack_forget()
    def backward(self):
        self.about_searchF.pack_forget()
        self.about_searchR.pack_forget()
        self.about_addF.pack_forget()
        self.about_addR.pack_forget()
        self.about_updateF.pack_forget()
        self.about_updateR.pack_forget()
        self.about_deleteF.pack_forget()
        self.about_deleteR.pack_forget()
        self.about_forward.pack_forget()
        self.about_backward.pack()

if __name__ == '__main__':
    root = tkinter.Tk()
    Main(master=root)
    root.mainloop()