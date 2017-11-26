# QCustomPlot 

QCustomPlot是一个绘图的第三方库，可用来绘制一些频谱图等


## 1.控件基本操作
添加控件后，提升为一个类，即可进行画图
### 1.1begin
- **customPlot->addGraph();**    
- **customPlot->addGraph(customPlot->yAxis,customPlot->xAxis2);** 第一个参数是key Axis,第二个参数是value Axis   
添加一幅图形，这里指的是在一幅图里可以绘制多种，添加后会自动为每个Graph排序 Graph(0),Graph(1)...  
- **customPlot->graph(0)->set...;**  
对绘制的每个图层，进行设置   
- **customPlot->replot();**   
这个会自动发生，不添加此函数也可以 

### 1.2坐标轴 axes
可以操作上下左右四个axes: xAxis,xAxis2,yAxis,yAxis2  
1.range
- **customPlot->xAxis->setRange(min,max);**
2.Label
- **customPlot->xAxis->setLabel("string");**

### 1.3图例 legend
1.先设置可视化!!!
- **customPlot->legend->setVisible(true);**   
2.名字交给图层

### 1.4 Ticker
- **customPlot->setTickLength(inside,outside);**  
inside,outside分别为内外高的像素，即坐标轴上的标注高低  
- **customPlot->setSubTickLength(inside,outside);**  


## 2.图层 graph
graph(0),graph(1),graph(2)...

### 2.1数据 data
- **customPlot->graph(0)->setData(x0,y0);**  
x0,y0是取样点数据，注意两者维度要保持一致

### 2.2图例 legend
- **customPlot->graph(0)->setName("string");**

### 2.3 样式
- **customPlot->graph(0)->setScatterStyle(QCPScatterStyle(QCPScatterStyle::ssDisc, 5));**  
可以设置成画出各个取样点的样式   
