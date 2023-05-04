import glob
import os

import gpxpy
import pyodbc

# 要扫描的路径
path = 'data/'

# 获取所有GPX文件的列表
gpx_files = glob.glob(os.path.join(path, '*.gpx'))
print(gpx_files)
# 连接数据库，创建游标对象
cnxn = pyodbc.connect("Driver={MySQL ODBC 8.0 Unicode Driver};"
                      "Server=192.168.159.1;"
                      "Database=iot;"
                      "UID=root;"
                      "PWD=Hexagon123;"
                      "charset=utf8mb4")
cursor = cnxn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS gpx_data (id INT AUTO_INCREMENT PRIMARY KEY, lat FLOAT, lon FLOAT, ele FLOAT, time TIMESTAMP)")

# 遍历所有GPX文件
for file in gpx_files:
    with open(file, 'r') as gpx_file:
        print("Parsing %s" % file)
        # 解析GPX文件
        gpx_data = gpxpy.parse(gpx_file)

        # 插入数据到表中
        for track in gpx_data.tracks:
            for segment in track.segments:
                for point in segment.points:
                    # 数据库插入语句
                    insert_statement = "INSERT INTO gpx_data (lat, lon, ele, time) VALUES (?, ?, ?, ?)"
                    print(point.latitude, point.longitude, point.elevation, point.time)
                    data = (point.latitude, point.longitude, point.elevation, point.time)
                    # 执行插入语句
                    cursor.execute(insert_statement, data)
                    cnxn.commit()
    # 移动文件到processed文件夹
    os.rename(file, os.path.join(path, 'processed', os.path.basename(file)))

# 关闭游标和连接
cursor.close()
cnxn.close()
