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

* 3.2 使用ConfigParser解析配置文件（49页）

	在这一节中，由于Python 2的ConfigParser在Python 3中重命名为了configparser，并且使用上也有一些细微的差异，因此，需要在书中注明是Python 2还是Python 3。

	**错误**:

	>在Python语言中，标准库的ConfigParser模块用以解析配置文件。

	**正确**:

	>在Python语言中，标准库的ConfigParser模块用以解析配置文件（在Python 3中，ConfigParser模块重命名为了configparser模块，使用上有细微差异）。

	此外，在50页的文字描述的倒数第二行，getinit是错别字。

	**错误**:

	>get、getboolean、getinit、getfloat：获取选项的值。

	**正确**:

	>get、getboolean、getint、getfloat：获取选项的值。

* 3.5.1 使用click解析命令行参数（59页）

    "它的作用与Pytho标准库的argparse相同"，这句话里面的"Pytho"是单词拼写错误。

    **正确**:

    >它的作用与Python标准库的argparse相同

* 4.2.4 案例：获取HTML页面中所有超链接（94页）

    在补充requests相关的说明时，多了两个星号。

    **错误**:

    >\*\*requests补充：\*\*requests是用来发送HTTP请求的库

    **正确**:

    >requests补充：requests是用来发送HTTP请求的库

* 5.2 文件与文件路径管理（123页）

    在对别Linux下与Windows下的路径分隔符时，Windows下的路径分隔符描述有错误。

    **错误**:

    >而Windows下的路径分隔符是"/"

    **正确**:

    >而Windows下的路径分隔符是"\\"

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

* 9.4.3 fab的命令行参数（267页）

	冒号标错了位置。

	**错误**：

	>--Fabric:  提供的便捷操作可以实现不写一行代码进行远程操作。

	**正确**：

	>--：Fabric提供的便捷操作，可以实现不写一行代码进行远程操作。

* 9.4.4 Fabric的env字典（269页）

	冒号标错了位置。

	**错误**：

    >env.user SSH：到远程服务器的用户名。

	>password SSH：到远程服务器的密码。

	**正确**：
	
    >env.user：SSH到远程服务器的用户名。
    
	>password：SSH到远程服务器的密码。

* 10.3.5 Inventory行为参数（302页）

	将“密码”修改为“端口号”。

	**错误**：

	>在10.2.3节中，我们在指定服务器的地址时，还通过ansible_user和ansible_port这两个参数指定了建立SSH连接的用户名和密码。

	**正确**：

	>在10.2.3节中，我们在指定服务器的地址时，还通过ansible_user和ansible_port这两个参数指定了建立SSH连接的用户名和端口号。

* 10.5.3 常用的Ansible模块（315页）

	grop是错别字。

	**错误**：

	>grop：文件或目录解压以后所属的群组；

	**正确**：
	
	>group：文件或目录解压以后所属的群组；

* 10.6.2 使用ansible-playbook执行Playbook（323页）

	冒号标错了位置和错别字。


	**错误**：

	>--list-hosts playbooks：匹配到服务器列表

	**正确**：
	
	>--list-hosts：playbooks匹配的服务器列表

* 11.2.1 MySQL数据库介绍（373页）

    InnsideMySQL是错别字。


    **错误**：

    >在InnsideMySQL公总号发布的国产数据库排行榜中，MySQL偶尔能够超过Oracle数据库，成为国内最热的数据库。

    **正确**：
    
    >在InsideMySQL公总号发布的国产数据库排行榜中，MySQL偶尔能够超过Oracle数据库，成为国内最热的数据库。

* 11.2.3 使用MySQLdb访问MySQL数据库（377页）

	377页的最后一句话，Coursor是错别字。


	**错误**：

	>但是返回的确是一个Coursor对象？

	**正确**：
	
	>但是返回的确是一个Cursor对象？

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
