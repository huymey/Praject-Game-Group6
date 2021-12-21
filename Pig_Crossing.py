import tkinter as tk
root = tk.Tk()
root.geometry('600x600')
frame = tk.Frame()
frame.master.title('game')
canvas = tk.Canvas(root)







canvas.pack(expand= True, fill="both")
frame.pack(expand= True, fill="both")
root.mainloop()
