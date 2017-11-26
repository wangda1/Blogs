# Template

关于函数模板与函数重载

## Function Template
函数模板：  
建立一个通用函数，其类型名与参数类型都不确定，用虚拟类型来代替
定义（声明）：  
- template <typename T>  或
- template <class T>
当有多个不同类型的参数时  
- template <class T1,typename T2> 
  
示例：
```
    template <typename Type>              //这里是类模板的声明

    class stackTest {

    public:
        stackTest();
        bool isempty();
        bool isfull();
        bool push(const Type & item);
        bool pop(Type & item);

    private:
        enum {MAX = 10};                //声明constant variables
        Type items[MAX];
        int top;
    };

    template <typename Type>            //这里是函数模板的声明，每一函数前都要声明
    stackTest<Type>::stackTest() {
        top = 0;
    }

    template <typename Type>
    bool stackTest<Type>::isempty() {
            return top == 0;
    }

    template <typename Type>
    bool stackTest<Type>::isfull() {
        return top == MAX;
    }

    template <typename Type>
    bool stackTest<Type>::push(const Type &item) {
        if (isfull())   return false;
        else {
            items[top] = item;
            top ++;
        }
    }

    template <typename Type>
    bool stackTest<Type>::pop(Type &item) {
        if(isempty()) return false;
        else {
            item = items[--top];
        }
    }
```


## Function overloading
函数重载：  
一个函数名重新赋予它新的含义，使一个函数名可以多用
