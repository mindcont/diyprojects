# encoding=utf-8
import pyodbc


# 解析result.txt 并插入sqlserver 数据库
def insert():
    # 连接数据库
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=127.0.0.1;'
                          'DATABASE=iot;'
                          'UID=sa;'
                          'PWD=Hexagon123')

    # 创建一个游标对象
    cursor = conn.cursor()

    # 解析文本文件 ,逐行
    with open('result.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            # {'Create Date': '2021:04:05 09:58:11', 'GPS Latitude': 36.0494888888889, 'GPS Longitude': 120.348130555556,
            #  'GPS Latitude Ref': 'N', 'GPS Longitude Ref': 'E',
            #  'filename': 'Z:\\MobileBackup\\iPhone\\2021\\04\\294CEAA1-B74B-4880-B965-A1ED5CDB57C1.HEIC'}

            # 转换为字典
            parts = line.split(',')
            # print(len(parts))
            create_date = parts[0].split(': ')[1]
            gps_latitude = parts[1].split(': ')[1]
            gps_longitude = parts[2].split(': ')[1]
            gps_latitude_ref = parts[3].split(":")[1]
            gps_longitude_ref = parts[4].split(":")[1]
            pic_name = parts[5].split("Z")[1].strip(" :")
            print(gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref, create_date, pic_name)

            # 插入数据库
            sql = "INSERT INTO location (gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref, create_date, pic_name) VALUES (?, ?, ?, ?, ?, ?)"
            values = (gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref, create_date, pic_name)
            cursor.execute(sql, values)

            # 提交更改
            conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    insert()
