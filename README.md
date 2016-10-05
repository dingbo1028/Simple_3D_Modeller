# Simple_3D_Modeller
A Simple 3d modeller by Python
这是一个用Python写的简易3D建模工具

基于Python 2.7

需要以下拓展包
PyOpenGL
bumpy

MacOS Linux 可直接编译使用
Windows x64 可能无法使用，原因可能是OpenGL的hult32.dll的问题，暂时还未解决


功能：
1、坐标轴系统和简单物体渲染：
 ![image](https://github.com/dingbo1028/Simple_3D_Modeller/blob/master/image/normal.jpeg)
2、trackball轨迹球旋转视口
 ![image](https://github.com/dingbo1028/Simple_3D_Modeller/blob/master/image/trackball.jpeg)
3、aabb包围盒pick节点
 ![image](https://github.com/dingbo1028/Simple_3D_Modeller/blob/master/image/select.jpeg)
4、move节点
 ![image](https://github.com/dingbo1028/Simple_3D_Modeller/blob/master/image/move.jpeg)
5、place新节点	
 ![image](https://github.com/dingbo1028/Simple_3D_Modeller/blob/master/image/place.jpeg)


目录结构：
＝3D	程序猿程序
	－aabb.py		aabb包围框
	-color.py		颜色数组
	-interaction.py		交互类
	-node.py		节点类
	-primtive.py		图元绘制
	-scene.py		场景类
	-trackball.py		轨迹球
	-transformation.py	移动和缩放矩阵
	-viewer.py		主视口文件，程序入口，配置gl，注册窗口
＝image	程序运行截图
	

