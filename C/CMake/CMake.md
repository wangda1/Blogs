# CMake  

首先，CMake是什么？  
引用官方网站
```
CMake is an open-source, cross-platform family of tools designed to build, test and package software. 
CMake is used to control the software compilation process using simple platform and compiler independent configuration files, 
and generate native makefiles and workspaces that can be used in the compiler environment of your choice. 
The suite of CMake tools were created by Kitware in response to the need for a powerful, cross-platform build environment 
for open-source projects such as ITK and VTK.
```

其次，怎么用？   
1.CMake工具链：cmake  + make    

2.编写  CMakeLists.txt文档，使用cmake语言与语法

2.建议语言： C C++ Java

3.安装：官方网站下载安装(一般Linux发行版都已经包含该组件)   

现在开始......

# cmake语言与语法    

一份最简化的  CMakeLists.txt  如下：     
```
PROJECT(HELLO)
ADD_EXECUTABLE(hello main.c)
```

扩充一下，加一些提示性信息：      
```
PROJECT(HELLO)
SET(SRC_LIST  main.c)
MESSAGE(STATUS  "This is BINARY DIR"  ${HELLO_BINARY_DIR})
MESSAGE(STATUS  "This is BINARY DIR"  ${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello main.c)
```

等等，我知道你用SET设置了变量，并且那个 ${} 就是取变量的值，这和  make  脚本编写是一样的，但  HELLO_BINARY_DIR,HELLO_SOURCE_DIR   
哪来的？？？    

原来在那个 PROJECT 命令里，隐式地定义了两个  cmake 变量  
- <projectname>_BINARY_DIR, <projectname>_SOURCE_DIR      
因为我们就一个文件 main.c  所以就都指的是当前目录了      
- PROJECT_BINARY_DIR, PROJECT_SOURCE_DIR    
这两个系统预定义的变量与上述两者的含义是完全一致的

**下面开始语法**

1.PROJECT指令：      
`PROJECT(projectname  [CXX] [C] [Java])`      
后面是支持的语言list,默认是全部支持，当然你也可以自己指定

2.SET指令：      
`SET(VAR  [VALUE] [CACHE TYPE DOCSTRING [FORCE]])`    
显式地定义变量     

如：SET(SRC_LIST  main.c  hello.c hello1.c)

3.MESSAGE指令：           
`MESSAGE([SEND_ERROR  | STATUS  | FATAL_ERROR]  "messageto display"...)`      
用于向终端输出用户定义的消息

4.ADD_EXECUTABLE指令：        
ADD_EXECUTABLE(HELLO  ${SRC_LIST})        

定义该工程会生成一个名为hello的可执行文件，即最终目标文件，后面是相关的源文件列表




## Tips 

1.  变量使用  ${}来取值，但是在  IF  控制语句中是直接使用变量名     
目前，还没遇到，遇到再说吧 :)

2.指令是**大小写无关的**，不过一般的指令都是大写的


























