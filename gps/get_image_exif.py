import exiftool

# 待扫描的图片文件夹路径
image_foder = r'Z:\MobileBackup'

count = 0  # 计数


def get_exif(filename):
    """获取 HEIC 文件的 Exif 数据"""

    with exiftool.ExifTool(executable=r'C:\ExifTool\exiftool.exe') as et:
        metadata = et.execute(filename)
        # print(metadata) # 打印 Exif 数据

        metadata_dict = {}
        result_dict = {}
        for line in metadata.split('\r\n'):
            parts = line.split(':')
            if len(parts) != 2:
                # print(line)
                if line.startswith('[EXIF]          Create Date'):
                    # 按照 Create Date 分割
                    parts = line.split('Create Date')
                    # print('时间', parts[1].strip(" :"))  # 提取创建日期
                    date_string = parts[1].strip(" :")
                    # 添加到字典中 result_dict key 是Create Date，value date_string
                    result_dict.update({'Create Date': date_string})

                continue
            key, value = parts
            key = key.strip()  # 去除键的前后空格
            value = value.strip()  # 去除值的前后空格
            metadata_dict.update({key: value})
        print(metadata_dict)

    # 如果 字典 metadata_dict['[Composite]     GPS Latitude'] 有值，说明有 GPS 数据
    if '[Composite]     GPS Latitude' not in metadata_dict:
        print('没有 GPS 数据')
        return None

    # 提取 GPS 数据
    gps_latitude = metadata_dict['[Composite]     GPS Latitude']  #
    gps_latitude_ref = metadata_dict['[EXIF]          GPS Latitude Ref']
    gps_longitude = metadata_dict['[Composite]     GPS Longitude']
    gps_longitude_ref = metadata_dict['[EXIF]          GPS Longitude Ref']

    # 计算经纬度
    if gps_latitude and gps_longitude and gps_latitude_ref and gps_longitude_ref:
        latitude = float(gps_latitude)
        longitude = float(gps_longitude)
        if gps_latitude_ref == 'S':
            latitude = -latitude
        if gps_longitude_ref == 'W':
            longitude = -longitude
        # print('经度：{}'.format(longitude))
        # print('纬度：{}'.format(latitude))

        result_dict.update({'GPS Latitude': latitude})
        result_dict.update({'GPS Longitude': longitude})
        result_dict.update({'GPS Latitude Ref': gps_latitude_ref})
        result_dict.update({'GPS Longitude Ref': gps_longitude_ref})
        result_dict.update({'filename': filename})
        return result_dict


def get_photos(root_directory):
    """获取目录下所有 HEIC 文件的路径"""
    import os
    photos_paths = []
    # 要扫描的根目录
    if not root_directory:
        root_directory = 'Z:\MobileBackup'
    # 递归遍历目录及其所有子目录
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            try:
                # 仅处理图片文件
                if file.endswith(".HEIC"):
                    # 将图像文件的路径添加到列表中
                    photos_paths.append(os.path.join(root, file))
            except IOError:
                # 通过异常处理器检测非照片文件
                pass

    # 打印所有添加到列表的照片文件路径
    for photo_path in photos_paths:
        print(photo_path)
    return photos_paths


if __name__ == '__main__':

    path = get_photos(image_foder)  # 扫描
    if path:
        for filename in path:
            # print(filename)
            result = get_exif(filename)  # 获取 Exif 数据
            if result:
                count += 1
                print('第{}张图片'.format(count))
                print(result)

                # 保存到文件
                with open('result.txt', 'a', encoding='utf-8') as f:
                    f.write(str(result) + '\n')
