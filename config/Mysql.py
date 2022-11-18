import logging

import pymysql


def adb(sql):
    """adb3.0:lansi_fdh数据库连接"""
    conn = pymysql.connect(host='am-uf6266p8y5ad6tvm8167330o.ads.aliyuncs.com',
                           user='adb_sa',
                           password='Lansi123',
                           database='lansi_fdh',
                           charset="utf8mb4")

    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        record = cursor.fetchall()
        return record
    except:
        conn.rollback()
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            filename="F:/Python项目/City_kfs_API/logs/sql.log")
        logging.info(f"{sql}查询出错啦~(adb3.0)")
    finally:
        conn.close()
