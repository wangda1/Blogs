# 绘图  

## plot  
> - plot(x,y);  
> - plot(x,y1;x,y2);  
> - plot(matrix);  绘制矩阵每一列的数据，以矩阵行为坐标  



## hold & figure 
> - hold on;hold off;用于在同一幅图形里继续绘图  
> - figure,figure1,figure2用于绘制第几幅图形  




## 线条与标注   
> - plot(x,y,':ok')  **线条类型**为点  **点类型**为.   **颜色**为黑色  
> - axis(v)  思维矢量设置坐标轴  
> - legend('string1','string2',etc)  设置图例  
> - text(x_coordinate,y_coordinate,'string')  在图形不同位置添加文本框
> - gtext('string')  文本框的位置由鼠标确定  
> - title('string')   设置标题  
```
title('\alpha \beta \gamma')  希腊字母  
title('x^2')    设置上标   
title('x_5')    创建下标  
title('k^{-1}')   创建下标  
```
 
