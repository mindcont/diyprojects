-- location
exec   sp_rename 'dbo.location', 'location_48579';
/*
警告: 表名可能非法 - location
*/
create table  dbo.location
(
       id                INT identity(1, 1) not null  /*编号*/,
       gps_latitude      VARCHAR(4000) null  /*纬度*/,
       gps_latitude_ref  VARCHAR(4000) null  /*维度标识*/,
       gps_longitude     VARCHAR(4000) null  /*经度*/,
       gps_longitude_ref VARCHAR(4000) null  /*经度标识*/,
       create_date       VARCHAR(4000) default getdate() null  /*创建日期*/,
       pic_name          VARCHAR(4000) null  /*图片名称*/
);
alter  table dbo.location
       add constraint PK_location_id primary key (id);
EXEC sp_addextendedproperty 'MS_Description', '地理位置表', 'user', dbo, 'table', location, NULL, NULL;
EXEC sp_addextendedproperty 'MS_Description', '编号', 'user', dbo, 'table', location, 'column', id;
EXEC sp_addextendedproperty 'MS_Description', '纬度', 'user', dbo, 'table', location, 'column', gps_latitude;
EXEC sp_addextendedproperty 'MS_Description', '维度标识', 'user', dbo, 'table', location, 'column', gps_latitude_ref;
EXEC sp_addextendedproperty 'MS_Description', '经度', 'user', dbo, 'table', location, 'column', gps_longitude;
EXEC sp_addextendedproperty 'MS_Description', '经度标识', 'user', dbo, 'table', location, 'column', gps_longitude_ref;
EXEC sp_addextendedproperty 'MS_Description', '创建日期 默认为当前时间', 'user', dbo, 'table', location, 'column', create_date;
EXEC sp_addextendedproperty 'MS_Description', '图片名称', 'user', dbo, 'table', location, 'column', pic_name;

