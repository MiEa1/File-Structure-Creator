import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def parse_structure(structure_str):
    lines = structure_str.strip().splitlines()
    stack = []
    paths = []

    for line in lines:
        stripped = line.lstrip("├─└│ ")
        indent = len(line) - len(stripped)
        level = indent // 4  # 层级推断

        while len(stack) > level:
            stack.pop()

        stack.append(stripped)
        current_path = os.path.join(*stack)
        paths.append(current_path)

    return paths


def is_file(path):
    name = os.path.basename(path)
    return "." in name and not path.endswith("/")


def create_structure(paths, base_dir):
    for path in paths:
        full_path = os.path.join(base_dir, path)
        if is_file(path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write("")
        else:
            os.makedirs(full_path, exist_ok=True)


# GUI 部分
class FileStructureGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("文件结构生成器")
        self.base_dir = ""

        # 文本输入框
        tk.Label(root, text="请输入文件结构:").pack(anchor="w", padx=10, pady=(10, 0))
        self.input_text = scrolledtext.ScrolledText(root, width=80, height=15)
        self.input_text.pack(padx=10, pady=5)

        # 按钮区域
        frame = tk.Frame(root)
        frame.pack(pady=5)

        tk.Button(frame, text="选择创建位置", command=self.select_directory).pack(side="left", padx=5)
        tk.Button(frame, text="预览结构", command=self.preview_structure).pack(side="left", padx=5)
        tk.Button(frame, text="创建结构", command=self.create_structure).pack(side="left", padx=5)

        # 预览框
        tk.Label(root, text="预览:").pack(anchor="w", padx=10, pady=(10, 0))
        self.preview_text = scrolledtext.ScrolledText(root, width=80, height=10, state="disabled")
        self.preview_text.pack(padx=10, pady=5)

    def select_directory(self):
        self.base_dir = filedialog.askdirectory()
        if self.base_dir:
            messagebox.showinfo("目录选择成功", f"创建目录位置:\n{self.base_dir}")

    def preview_structure(self):
        structure_str = self.input_text.get("1.0", tk.END)
        if not structure_str.strip():
            messagebox.showwarning("警告", "请输入文件结构")
            return

        try:
            paths = parse_structure(structure_str)
        except Exception as e:
            messagebox.showerror("解析失败", f"错误: {e}")
            return

        # 显示预览
        self.preview_text.config(state="normal")
        self.preview_text.delete("1.0", tk.END)
        for path in paths:
            prefix = "[文件] " if is_file(path) else "[目录] "
            self.preview_text.insert(tk.END, prefix + path + "\n")
        self.preview_text.config(state="disabled")

    def create_structure(self):
        if not self.base_dir:
            messagebox.showwarning("未选择目录", "请先选择创建目录的位置")
            return

        structure_str = self.input_text.get("1.0", tk.END)
        if not structure_str.strip():
            messagebox.showwarning("警告", "请输入文件结构")
            return

        try:
            paths = parse_structure(structure_str)
            create_structure(paths, self.base_dir)
            messagebox.showinfo("成功", "文件结构已成功创建！")
        except Exception as e:
            messagebox.showerror("创建失败", f"错误: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileStructureGUI(root)
    root.mainloop()
