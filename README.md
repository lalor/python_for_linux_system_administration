# 勘误表

## 书籍信息

* 书名：Python Linux系统管理与自动化运维
* 完整目录: <https://github.com/lalor/python_for_linux_system_administration/blob/master/table_of_contents.md>
* 作者：赖明星
* 作者邮箱：me@mingxinglai.com
* 知乎：https://www.zhihu.com/people/mingxinglai
* IMG（Inside MySQL Group）社区公众号：

    ![img](http://cdn.huodongxing.com/file/20160220/11668836D67E17B48B99B6842EF86DB58A/30622730670102782.jpg)

## 其他资料

* 7.6 使用Python打造一个geek的邮件客户端 (<https://github.com/lalor/emcli>)
* 11.4 使用Python打造MySQL专家系统（<https://github.com/lalor/health-checker>）

## 勘误

* 2.2.3 加速pip安装的技巧（14页）

    在"将软件下载到本地部署"这一段内容中，所有pwd命令两侧的引号，都是反引号。

    **错误**:

        pip install --download='pwd' -r requirements.txt

    **正确**:

        pip install --download=`pwd` -r requirements.txt

* 3.1.3 使用SystemExit异常打印错误信息（48页）

    在这一页的末尾，test_system_exit.py文件的内容如下：

        raise SystemExit("error message")

    **正确**:
    
        $ cat test_system_exit.py
        raise SystemExit("error message")
    
        $ python test_system_exit.py
        error message
    
        $ echo $?
        1

* 3.5.1 使用click解析命令行参数（59页）

    "它的作用于Pytho标准库的argparse相同"，这句话里面的Python拼写错误。

    **正确**:

    它的作用于Python标准库的argparse相同

* 4.2.4 案例：获取HTML页面中所有超链接

    在补充requests相关的说明时，多了两个星号。

    **错误**:

    \*\*requests补充：\*\*requests是用来发送HTTP请求的库

    **正确**:

    requests补充：requests是用来发送HTTP请求的库

* 5.2 文件与文件路径管理（123页）

    在对别Linux下与Windows下的路径分隔符时，Windows下的路径分隔符描述有错误。

    **错误**:

    而Windows下的路径分隔符是"/"

    **正确**:

    而Windows下的路径分隔符是"\\"

* 8.5.6 案例：使用Scapy嗅探信用卡信息（252页）

    代码排版有错误。

    **错误**:

        def find_credit_card(packet):
            raw = packet.sprintf('%Raw.load%')
            america_re = re.findall('3[47][0-9]{13}', raw)
            master_re = re.findall('5[1-5][0-9]{14}', raw)    visa_re = re.findall('4[0-9][0-9]{12}(?:[0-9]{3})?', raw)

    **正确**:

        def find_credit_card(packet):
            raw = packet.sprintf('%Raw.load%')
            america_re = re.findall('3[47][0-9]{13}', raw)
            master_re = re.findall('5[1-5][0-9]{14}', raw)
            visa_re = re.findall('4[0-9][0-9]{12}(?:[0-9]{3})?', raw)

* 11.3.1 Python中的多线程（382页）

    代码排版有错误，在say_hi函数中，使用了8个空格的缩进。

    **错误**:

        def say_hi():
                time.sleep(1)
                print("hello, world")

    **正确**:

        def say_hi():
            time.sleep(1)
            print("hello, world")
