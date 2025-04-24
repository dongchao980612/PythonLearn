if __name__ == '__main__':
    import pymysql

    # 打开数据库连接
    connect = pymysql.connect(host = "localhost",
                              port = 8080,
                              user = "test123",
                              passwd = "1233",
                              db = "testDb",
                              charset="utf-8")

    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()

    # 查询数据
    # 使用execute方法执行SQL语句
    sql="select * from stu_t"
    cursor.execute(sql)

    # name age
    for row in cursor.fetchall():
        print("Name:%s\tAge:%f " ,row )
    print("一共查到",cursor.rowcount,"条数据")

    # 插入数据
    sql = "insert into stu_t (id,name,age) values (1,zhangsan,18)"
    cursor.execute(sql)
    connect.commit()
    print("插入成功")


    # 删除语句
    sql = "delete from stu_t where age > 20"
    cursor.execute(sql)
    connect.commit()
    print("删除成功")

    sql = "update stu_t set age =20 where name = zhangsan"
    cursor.execute(sql)
    connect.commit()
    print("删除成功")

    # 错误处理
    # 发生错误时回滚
    # connect.rollback()

    # 关闭数据库连接
    connect.close()