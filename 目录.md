# Python Linux 系统管理指南

### 第1章 Python语言与Linux系统管理

#### 1.1 Python语言有多流行
#### 1.2 Python语言为什么流行
#### 1.3 Python语言有什么缺点
#### 1.4 Python语言的应用场景
#### 1.5 为什么Python适合Linux系统管理
#### 1.6 使用Python 2还是Python 3

### 第2章 Python生态工具

#### 2.1 Python内置小工具

* 2.1.1 1秒钟启动一个下载服务器
* 2.1.2 字符串转换为JSON
* 2.1.3 检查第三方库是否正确安装

#### 2.2 pip高级用法

* 2.2.1 pip介绍
* 2.2.2 pip常用命令
* 2.2.3 加速pip安装的技巧

#### 2.3 Python编辑器

* 2.3.1 编写Python的vim插件
* 2.3.2 Windows下Python编辑器PyCharm介绍

#### 2.4 Python编程辅助工具

* 2.4.1 Python交互式编程
* 2.4.2 使用IPython交互式编程
* 2.4.3 jupyter的使用

#### 2.5 Python调试器

* 2.5.1 标准库的pdb
* 2.5.2 开源的ipdb

#### 2.6 Python代码规范检查

* 2.6.1 PEP 8编码规范介绍
* 2.6.2 使用pycodestyle检查代码规范
* 2.6.3 使用autopep8将代码格式化

#### 2.7 Python工作环境管理

* 2.7.1 使用pyenv管理不同的Python版本
* 2.7.2 使用virtualenv管理不同的项目

#### 2.8 本章总结

### 第3章 打造命令行工具

#### 3.1 与命令行相关的Python语言特性

* 3.1.1 使用sys.argv获取命令行参数
* 3.1.2 使用sys.stdin和fileinput读取标准输入
* 3.1.3 使用SystemExit异常打印错误信息
* 3.1.4 使用getpass库读取密码

#### 3.2 使用ConfigParse解析配置文件

#### 3.3 使用argparse解析命令行参数

* 3.1.1 ArgumentParse解析器
* 3.3.2 模仿MySQL客户端的命令行参数

#### 3.4 使用logging记录日志

* 3.4.1日志的作用
* 3.4.2 Python的logging模块
* 3.4.3 配置日志格式

#### 3.5 与命令行相关的开源项目

* 3.5.1 使用click解析命令行参数
* 3.5.2 使用prompt_toolkit打造交互式命令行工具

#### 3.6 本章总结

### 第4章 文本处理

#### 4.1 字符串常量

* 4.1.1 定义字符串
* 4.1.2 字符串是不可变的有序集合
* 4.1.3 字符串函数
* 4.1.4 案例：使用Python分析Apache的访问日志
* 4.1.5 字符串格式化

#### 4.2 正则表达式

* 4.2.1 正则表达式语法
* 4.2.2 利用re库处理正则表达式
* 4.2.3 常用的re方法
* 4.2.4 案例：获取HTML页面中的所有超链接

#### 4.3 字符集编码

* 4.3.1 编码历史
* 4.3.2 UTF-8编码
* 4.3.3 从字符集的问题说起
* 4.3.4 Python 2和Python 3中的Unicode

#### 4.4 Jinja2 模板

* 4.4.1 模板介绍
* 4.4.2 Jinja2语法入门
* 4.4.3 Jinja2实战
* 4.4.4 案例：使用Jinja2生成HTML表格和XML配置文件

#### 4.5 本章总结

### 第5章 Linux系统管理

#### 5.1 文件读写

* 5.1.1 Python内置的open函数
* 5.1.2 避免文件句柄泄露
* 5.1.3 常见的文件操作函数
* 5.1.4 Python的文件是一个可迭代对象
* 5.1.5 案例：将文件中所有单词的首字母变成大写

#### 5.2 文件与文件路径管理

* 5.2.1 使用os.path进行路径和文件管理
* 5.2.2 使用os模块管理文件和目录
* 5.2.3 案例：打印最常用的10条Linux命令

#### 5.3 查找文件

* 5.3.1 使用fnmatch找到特定的文件
* 5.3.2 使用glob找到特定的文件
* 5.3.3 使用os.walk遍历目录树
* 5.3.4 案例：找到目录下最大(或最老)的十个文件

#### 5.4 高级文件处理接口shutil

* 5.4.1 复制文件和文件夹
* 5.4.2 文件和文件夹的移动与改名
* 5.4.3 删除目录

#### 5.5 文件内容管理

* 5.5.1 目录和文件比较
* 5.5.2 MD5校验和比较
* 5.5.3 案例：找到目录下的重复文件

#### 5.6 使用Python管理压缩包

* 5.6.1 使用tarfile库读取与创建tar包
* 5.6.2 使用tarfile库读取与创建压缩包
* 5.6.3 案例：备份指定文件到压缩包中
* 5.6.4 使用zipfile库创建和读取zip压缩包
* 5.6.5 案例：暴力破解zip压缩包的密码
* 5.6.6 使用shutil创建和读取压缩包

#### 5.7 Python中执行外部命令

* 5.7.1 subprocess模块简介
* 5.7.2 subprocess模块的便利函数
* 5.7.3 subprocess模块的Popen类

#### 5.8 综合案例：使用Python部署MongoDB

#### 5.9 本章总结

### 第6章 使用Python监控Linux系统

#### 6.1 Python编写的监控工具

* 6.1.1 多功能系统资源统计工具dstat
* 6.1.2 交互式监控工具glances

#### 6.2 使用Python打造自己的监控工具

* 6.2.1 Linux系统的/proc目录介绍
* 6.2.2 proc目录下常用文件介绍
* 6.2.3 进程目录下常用文件介绍
* 6.2.4 利用/proc目录找到被删除的文件
* 6.2.5 使用shell脚本监控Linux
* 6.2.6 使用Python监控Linux

#### 6.3 使用开源库监控Linux

* 6.3.1 psutil介绍
* 6.3.2 psutil提供的功能函数
* 6.3.3 综合案例：使用psutil实现监控程序
* 6.3.4 psutil进程管理

#### 6.4 使用pyinotify监控文件系统变化

* 6.4.1 pyinotify模块介绍
* 6.4.2 pyinotify模块API
* 6.4.3 事件标志与事件处理器

#### 6.5 监控应用程序

* 6.5.1 使用Python监控MySQL
* 6.5.2 使用Python监控MongoDB

#### 6.6 本章总结

### 第7章 文档与报告

#### 7.1 使用Python处理Excel文档

* 7.1.1 openpyxl简介与安装
* 7.1.2 使用openpyxl读取Excel文档
* 7.1.3 使用openpyxl修改Excel文档
* 7.1.4 案例：合并多个Excel文档到一个Excel文档

#### 7.2 使用Python操作PDF文档

* 7.2.1 PyPDF2安装与介绍
* 7.2.2 使用PdfFileReader读取PDF文件
* 7.2.3 使用PdfFileWriter创建PDF文件
* 7.2.4 修改PDF页面
* 7.2.5 使用PdfFileMerger合并多个PDF文件

#### 7.3 使用Python归档图片

* 7.3.1 Exif信息介绍
* 7.3.3 在Python使用PIL查看图片元信息

#### 7.4 发送报告

* 7.4.1 SMTP协议
* 7.4.2 邮箱设置（以QQ邮箱为例）
* 7.4.3 使用标准库的smtplib与mime发送邮件
* 7.4.4 使用开源的yagmail发送邮件

#### 7.5 接收邮件

* 7.5.1 接收邮件协议IMAP与POP3
* 7.5.2 使用开源从imapclient接收邮件
* 7.5.3 使用pyzmail解析邮件
* 7.5.4 使用imapclient删除邮件

#### 7.6 综合案例：使用Python打造一个geek的邮件客户端

* 7.6.1 emcli的功能设计
* 7.6.2 emcli的功能实现
* 7.6.3 使用setuptools打包源码
* 7.6.4 使用twine上传到PyPi

#### 7.7 本章总结

### 第8章 网络

#### 8.1 列出网络上所有活跃的主机

* 8.1.1 使用ping命令判断主机是否活跃
* 8.1.2 使用Python判断主机是否活跃
* 8.1.3 使用生产者消费者模型减少线程的数量

#### 8.2 端口扫描

* 8.2.1 使用Python编写端口扫描器
* 8.2.2 使用nmap扫描端口
* 8.2.3 使用python-nmap进行端口扫描

#### 8.3 使用IPy进行IP地址管理

* 8.3.1 IPy模块介绍
* 8.3.2 IPy模块的基本使用
* 8.3.3 网段管理

#### 8.4 使用dnspython解析DNS

* 8.4.1 dnspython简介与安装
* 8.4.2 使用dnspython进行域名解析

#### 8.5 网络嗅探器Scapy

* 8.5.1 Scapy简介与安装
* 8.5.2 Scapy的基本使用
* 8.5.3 使用Scapy发送数据报
* 8.5.4 使用Scapy构造DNS查询请求
* 8.5.5 使用Scapy进行网络嗅探
* 8.5.6 案例：使用Scapy嗅探信用卡信息

#### 8.6 本章总结

### 第9章 Python自动化管理

#### 9.1 使用SSH协议访问远程服务器

* 9.1.1 SSH协议
* 9.1.2 OpenSSH实现
* 9.1.3 使用密钥登录远程服务器
* 9.1.4 使用ssh-agent管理私钥

#### 9.2 使用Polysh批量管理服务器

* 9.2.1 批量修改密码
* 9.2.2 Polysh的使用

#### 9.3 SSH协议的Python实现paramiko

* 9.3.1 paramiko的安装
* 9.3.2 SSHClient类与SFTPClient类
* 9.3.3 paramiko的基本使用
* 9.3.4 使用paramiko部署监控程序

#### 9.4 自动化部署工具Fabric

* 9.4.1 Fabric安装
* 9.4.2 Fabric使用入门
* 9.4.3 fab的命令行参数
* 9.4.4 Fabric的env字典
* 9.4.5 Fabric提供的命令
* 9.4.6 Fabric提供的上下文管理器
* 9.4.7 Fabric提供的装饰器
* 9.4.8 其他功能函数
* 9.4.9 使用Fabric源码安装redis
* 9.4.10 综合案例：使用Fabric部署Flask应用

#### 9.5 本章总结

### 第10章 深入浅出Ansible

#### 10.1 Ansible介绍

* 10.1.1 Ansible的优点
* 10.1.2 Ansible 与Fabric之间比较
* 10.1.3 Ansible与SaltStack之间比较

#### 10.2 Ansible使用入门

* 10.2.1 安装Ansible
* 10.2.2 Ansible的架构
* 10.2.3 Ansible的运行环境
* 10.2.4 Ansible的ad-hoc模式
* 10.2.5 使用playbook控制服务器

#### 10.3 Inventory管理

* 10.3.1 hosts文件位置
* 10.3.2 灵活定义hosts文件内容
* 10.3.3 灵活匹配hosts文件内容
* 10.3.4 动态Inventory获取
* 10.3.5 Inventory行为参数
* 10.3.6 定义服务器变量

#### 10.4 YAML语法

#### 10.5 Ansible模块

* 10.5.1 Ansible的模块工作原理
* 10.5.2 模块列表与帮助信息
* 10.5.3 常用的Ansible模块
* 10.5.4 模块的返回值

#### 10.6 Playbook

* 10.6.1 Playbook的定义
* 10.6.2 使用ansible-playbook执行Playbook
* 10.6.3 Playbook的详细语法
* 10.6.4 使用Playbook部署nginx
* 10.6.5 使用Playbook部署MongoDB
* 10.6.6 Playbook中的高级语法

#### 10.7 role的定义与使用

* 10.7.1 role的概念
* 10.7.2 使用ansible-galaxy命令管理role
* 10.7.3 如何使用role
* 10.7.4 使用role改造部署MongoDB的例子

#### 10.8 Ansible的配置文件

* 10.8.1 配置文件的查找路径
* 10.8.2 Ansible中的常用配置

#### 10.9 Ansible的最佳实践

* 10.9.1 Ansible的文件组织
* 10.9.2 Ansible最佳实践
* 10.9.3 使用role部署LAMP应用

#### 10.10 本章总结

### 第11章 使用Python打造MySQL专家系统

#### 11.1 Python语言高级特性

* 11.1.1 深入浅出Python生成器
* 11.1.2 深入浅出Python装饰器
* 11.1.3 Python上下文管理器

#### 11.2 MySQL数据库

* 11.2.1 MySQL数据库介绍
* 11.2.2 Python连接数据库
* 11.2.3 使用MySQLdb访问MySQL数据库
* 11.2.4 使用上下文管理器对数据库连接进行管理
* 11.2.5 案例：从csv文件导入数据到MySQL

#### 11.3 Python并发编程

* 11.3.1 Python中的多线程
* 11.3.2 线程同步与互斥锁
* 11.3.3 线程安全队列Queue
* 11.3.4 案例：使用Python打造一个MySQL压测工具

#### 11.4 专家系统设计

* 11.4.1 专家系统使用
* 11.4.2 专家系统检查内容
* 11.4.3 如何进行数据库检查
* 11.4.4 专家系统评分体系

#### 11.5 MySQL专家系统整体架构

* 11.5.1 专家系统架构设计
* 11.5.2 专家系统文件组织

#### 11.6 数据库专家系统的客户端设计

* 11.6.1 实现数据库连接池
* 11.6.2 使用装饰器检查参数
* 11.6.3 利用Python的动态语言特性执行命令
* 11.6.4 利用call方法实现可调用对象
* 11.6.5 Python的property

#### 11.7 数据库专家系统服务端设计

* 11.7.1 将相同的操作提升到父类中
* 11.7.2 在Python中实现map-reduce模型
* 11.7.3 利用动态语言特性实现工厂模式

#### 11.8 本章总结