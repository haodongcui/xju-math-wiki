# XJU Math Wiki
欢迎来到本项目，这是一个基于 MkDocs 构建的数学 Wiki 项目，用于分享在新大数院学习期间所用到的一些资料。


## 📝项目概述
功能:
- 分享各学科的部分资料
- 记录一些经验和感悟

技术栈：
- MkDocs 框架
- mkdocs-material 主题
- Github Actions 自动部署
- Markdown 笔记


## 📚项目结构
- 在`课程资料`文件夹中，每个文件夹对应一个课程，文件夹中包含该课程的一些资料。
- 在`docs`文件夹中，包含网站的每个Markdown页面，可自行修改。
- 在`mkdocs.yml`文件中，可配置网站的标题、导航栏等。


## 💻一些命令
安装依赖与构建项目
```shell
pip install mkdocs
pip install mkdocs-material
mkdocs new xju-math-wiki
cd xju-math-wiki
mkdocs serve
mkdocs build
```

若某些命令不可运行，可在命令前加`python -m`, 例如
```shell
python -m mkdocs new xju-math-wiki
python -m mkdocs serve
python -m mkdocs build
```

