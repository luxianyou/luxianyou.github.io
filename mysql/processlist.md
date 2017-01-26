**关键词**：==show processlist== ==sql== ==mysql== ==优化==
~~~
概要：
   SHOW PROCESSLIST显示哪些线程正在运行。如果您有SUPER权限，您可以看到所有线程。否则，您只能看到您自己的线程（也就是，与您正在使用的MySQL账户相关的线程）。如果您不使用FULL关键词，则只显示每个查询的前100个字符。

   本语句报告TCP/IP连接的主机名称（采用host_name:client_port格式），以方便地判定哪个客户端正在做什么。

   如果您得到“too many connections”错误信息，并且想要了解正在发生的情况，本语句是非常有用的。MySQL保留一个额外的连接，让拥有SUPER权限的 账户使用，以确保管理员能够随时连接和检查系统（假设您没有把此权限给予所有的用户）。
~~~

**目录**：
1. [命令用法](content-1)
2. 参数解析
3. 参考资料

---

###### 1  命令用法
> mysql> show processlist;

![image](./images/processlist.png)