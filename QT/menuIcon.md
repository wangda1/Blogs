# menuIcon

添加菜单图标

## 设计模式

1.在menuBar输入框中输入自己要输入的一级菜单名称，二级菜单...

2.Qt中的一个菜单被视为一个Action，在下面Action编辑器中更改“文本”等
- 这里可以通过 &Open,&New,设置加速键，**加速键**：即当菜单处于激活状态时的快捷键
- 这里也可以设置**快捷键shortcut**，在shortcut输入框中输入快捷键

3.当要添加菜单图标时，需要用到“图标”后面的“添加文件”，“添加资源”；
- **资源文件**：Qt使用资源文件将各种外部文件添加至最终生成的可执行文件中
- 文件

4.选取图标所在文件夹里的文件即可


## 编辑模式

原理与上述同，上代码：
```
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //创建新的动作
    QAction *openAction = new QAction("&Open",this);
    //添加图标,这里的路径参考ui_mainwindow.h文件，里面代码与此相同
    QIcon icon(":/myImages/img/actions/fileopen.png");
    openAction->setIcon(icon);
    //设置快捷键
    openAction->setShortcut(QKeySequence("Ctrl+O"));
    //在文件菜单中设置新的打开动作
    ui->menu->addAction(openAction);
}

MainWindow::~MainWindow()
{
    delete ui;
}
```
在主窗口的构造函数中添加"//"部分代码
