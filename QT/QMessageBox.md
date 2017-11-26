# QMessageBox

弹窗

## modal dialog

对话框的两种模式，default是application modal，两者区别见下：
**application modal**
```
When an application modal dialog is opened, the user must finish interacting with the dialog and close it before they can access any other window in the application.
```
什么意思呢？就是在application dialog模式下，必须完成与该dialog的交互，才能与其它dialog交互，完全阻塞

**window modal**
```
Window modal dialogs only block access to the window associated with the dialog, allowing the user to continue to use other windows in an application.
```
window modal模式下，就是非必须完成交互也能与其它不相关窗口交互


## QMessageBox
继承于QDialog class

```
QMessageBox box;
        box.setWindowTitle("警告");
        box.setIcon(QMessageBox::Warning);
        box.setText(curFile+"尚未保存，是否保存？");
        QPushButton *yesBtn = box.addButton("是(&Y)",QMessageBox::YesRole);
        box.addButton("否(&N)",QMessageBox::NoRole);
        QPushButton *cancelBtn = box.addButton("取消",QMessageBox::RejectRole);
        box.exec();                                                 //窗口关闭时获取DialogCode
        if(box.clickedButton()==yesBtn) {
            return save();
        }
        else if(box.clickedButton()==cancelBtn){
            return false;
        }
```


