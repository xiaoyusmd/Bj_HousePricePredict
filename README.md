# Bj_HousePrice_Analysis-Prediction
北京二手房房价预测分析 —— 从爬虫到机器学习预测

作者：xiaoyu

时间：2018.4.11

### 项目简介
本项目根据个人需求进行北京二手房信息的数据分析，通过数据分析观察住房特征规律，利用机器学习模型进行简单的预测。
### 数据源
通过爬虫爬取第三方房屋中间商网站（链家和安居客）获取数据源，仅供学习使用。
>注：爬虫源代码见`spiders`文件夹。

### 目的
北京房价是最受关注的话题。因此，本项目以研究北京二手房房价为目的，对二手房房价进行数据分析，并希望能对未来房价进行预测（仅供参考）。
- 统计北京各区域二手房房价情况
- 统计北京各区域二手房数量
- 统计西城区、东城区和海淀区各地方二手房房价
- 统计房价与房屋面积区段的房屋数量
- 预测北京二手房房价

### 技术和工具
本项目以Python语言编程完成从爬取，数据分析，到预测。

- 爬虫工具：`scrapy` ，`beautifulsoup`
- 数据分析：`pandas`，`numpy`，`matplolib`
- 机器学习：`sklearn`

## 大区房价对比 
![img](https://github.com/xiaoyusmd/Bj_HousePricePredict/blob/master/ershoufang_0.JPG)
## 大区房屋数量
![img1](https://github.com/xiaoyusmd/Bj_HousePricePredict/blob/master/ershoufang_1.JPG)
## 区间房价和面积的房屋数量
![img2](https://github.com/xiaoyusmd/Bj_HousePricePredict/blob/master/ershoufang_2.JPG)
## 学习曲线观察拟合度
![img3](https://github.com/xiaoyusmd/Bj_HousePricePredict/blob/master/ershoufang_3.JPG)
