# file-transfer

文件传输服务器 - 用于接受和保存手表采集的数据

使用 HTTP POST 方法来接受手表发送的数据，并保存到电脑硬盘上

# 使用说明

## 请求说明

启动服务器后，向 `http://ip地址/file/` 发送 POST 请求，携带 3 个参数: dirname、filename、data

|URL|http://ip地址/file/|METHOD|POST|
|参数|作用|
|dirname|存放的文件夹名字（注：这个参数非服务器上的绝对路径，只是在某个文件夹下创建一个新的文件夹，这个新的文件夹名为 dirname）|
|filename|文件名（注：保存时并非以该文件名来保存，会在文件名后面加上数字来避免文件名重复）|
|data|要保存的数据|

## 自定义配置

需要修改的配置在 `file_transfer\views.py` 文件下的 `saveFile` 函数，第一行即为要保存的文件夹路径

# 安装

进入项目根目录

## 安装依赖

```
pip install -r requirements.txt
# 
```

## 启动

```
python manage.py runserver 0.0.0.0:8080
```
