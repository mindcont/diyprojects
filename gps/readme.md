## 图片轨迹

通过提取 iphone `.HEIC`图片格式中gps信息，结合地图绘制热力图 网页

![](demo.png)




### 代码说明
```css
get_image_exif.py # 扫描文件夹下图片，提取信息到 result.txt中
insert_to_mysql.py # 解析result.txt信息，插入到数据库（可选）
draw_heatmap.py #绘制热力地图
```

