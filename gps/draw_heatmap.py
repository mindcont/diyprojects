import json

import folium
import pyodbc
import requests
from folium.plugins import HeatMap

key = '你的高德 API 密钥'


# 获取经纬度范围内的点
def get_points(city, types):
    url = f'https://restapi.amap.com/v3/place/text?key={key}&city={city}&types={types}&offset=100&page=1&output=json'
    response = requests.get(url)
    data = json.loads(response.text)
    points = [(float(item['location'].split(',')[1]), float(item['location'].split(',')[0])) for item in data['pois']]
    print('Points are ready!', points)
    return points


def get_mypoints():
    # 连接sqlserve 数据库
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=127.0.0.1;'
                          'DATABASE=iot;'
                          'UID=sa;'
                          'PWD=Hexagon123')

    # 创建一个游标对象
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute('SELECT  gps_latitude_ref, gps_longitude FROM iot.dbo.location')
    rows = cursor.fetchall()
    # 打印结果
    # print(rows)
    return rows


def draw_my(points):
    map_osm = folium.Map(location=[points[0][0], points[0][1]], zoom_start=13)
    map_osm.add_child(HeatMap(points))
    print('Map is ready!', map_osm)
    return map_osm


if __name__ == '__main__':
    points = get_mypoints()
    map_osm = draw_my(points)
    map_osm.save('my.html')
