# 📁 文件结构自动创建工具（GUI版）

一个基于 Python 的图形化工具，支持用户输入多层级的目录结构图，一键自动生成对应的文件夹与文件，适用于：

- 插件模板快速搭建
- 前端项目初始化
- 教学与开发者脚本自动生成

---

## 🎉 功能特点

✅ 支持图形界面操作  
✅ 输入类似目录结构文本，自动识别文件与文件夹  
✅ 一键选择生成路径  
✅ 创建前可预览生成结构  
✅ 基于标准库 `tkinter` 实现，无需额外安装依赖

---

## 📷 界面预览

![界面示例]([https://your-screenshot-url-here.com/optional.png](https://raw.githubusercontent.com/MiEa1/File-Structure-Creator/refs/heads/main/screen-shot/1.png))
![界面示例]([https://your-screenshot-url-here.com/optional.png](https://raw.githubusercontent.com/MiEa1/File-Structure-Creator/refs/heads/main/screen-shot/2.png))

---

## 🛠️ 使用方法

1. 安装 Python（建议 Python 3.8+）
2. 下载本仓库中的 `file_structure_gui.py` 文件
3. 在终端或命令行中运行：

```
python file_structure_gui.py
```
粘贴你的文件结构文本，例如：

```
my-project/
├── index.html
├── style.css
└── js/
    └── main.js
```

点击“选择创建位置”

点击“预览结构”查看将生成的内容

点击“创建结构”一键生成 ✅

--- 

📦 打包为可执行文件（Windows）
可使用 pyinstaller 打包：

```
pip install pyinstaller
pyinstaller -F file_structure_gui.py
```

生成的 .exe 可直接运行，无需 Python 环境。

🔒 权限说明
本程序不会读取或上传任何文件，仅在你本地系统中创建你指定的目录结构。

📄 许可证
Apache License 2.0 - 欢迎自由使用、修改与分发。

❤️ 作者
由 MiEa1 开发。欢迎提 Issue 或 PR！
