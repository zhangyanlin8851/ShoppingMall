#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.Product import IProductRepository
from Repository.DbConnection import DbConnection


class ProductRepository(IProductRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_page_by_merchant_id(self, merchant_id, start, rows):
        cursor = self.db_conn.connect()
        sql = """select nid,title,img,category_id from product where merchant_id=%s order by nid desc limit %s offset %s"""
        cursor.execute(sql, (merchant_id, rows,start,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_count_by_merchant_id(self, merchant_id):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from product where merchant_id=%s"""
        cursor.execute(sql, (merchant_id, ))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_product_by_pid(self, product_id):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from product where  nid=%s"""
        cursor.execute(sql, (product_id, ))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def fetch_product_by_pid(self, merchant_id, product_id):
        cursor = self.db_conn.connect()
        sql = """select nid,title from product where  nid=%s"""
        cursor.execute(sql, (merchant_id, product_id, ))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def fetch_product_by_id(self, merchant_id, product_id):
        cursor = self.db_conn.connect()
        sql = """select nid,title from product where merchant_id=%s and nid=%s"""
        cursor.execute(sql, (merchant_id, product_id, ))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def add_product(self, product_dict, detail_list, img_list):
        """
        创建商品
        :param product_dict: 商品字典 {'title': 'x'}
        :param detail_list: [{'key': xx, 'value': 'xxx'}]
        :param img_list: [{'src': 'fa'},{'src': 'fa'}]
        :return:
        """
        # print(product_dict, detail_list, img_list)
        product_sql = "insert into product(%s) values(%s)"
        p_k_list = []
        p_v_list = []
        for k in product_dict.keys():
            p_k_list.append(k)
            p_v_list.append('%%(%s)s' % k)
        product_sql = product_sql % (','.join(p_k_list), ','.join(p_v_list), )
        cursor = self.db_conn.connect()
        cursor.execute(product_sql, product_dict)

        product_id = cursor.lastrowid

        if detail_list:
            d = map(lambda x: x.update(product_id=product_id), detail_list)
            list(d)
            detail_sql = "insert into product_detail(%s) values(%s)"
            d_k_list = []
            d_v_list = []
            for k in detail_list[0].keys():
                d_k_list.append(k)
                d_v_list.append('%%(%s)s' % k)
            detail_sql = detail_sql % (','.join(d_k_list), ','.join(d_v_list),)
            cursor.executemany(detail_sql, detail_list)


        if img_list:
            i = map(lambda x: x.update(product_id=product_id), img_list)
            list(i)
            img_sql = "insert into product_img(%s) values(%s)"
            i_k_list = []
            i_v_list = []
            for k in img_list[0].keys():
                i_k_list.append(k)
                i_v_list.append('%%(%s)s' % k)
            img_sql = img_sql % (','.join(i_k_list), ','.join(i_v_list),)
            print(img_sql, img_list)
            cursor.executemany(img_sql, img_list)

        self.db_conn.close()

    def fetch_price_by_product_id(self,merchant_id, product_id):
        cursor = self.db_conn.connect()
        sql = """select price.nid as nid,
                        standard,
                        price,
                        selling_price,
                        product_id
                        from
                          price
                        left join product on price.product_id = product.nid
                        where
                          product.merchant_id=%s
                        and
                          product_id=%s
                        order by nid desc"""

        cursor.execute(sql, (merchant_id, product_id,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def add_price(self, price_dict):

        price_sql = "insert into price(%s) values(%s)"
        p_k_list = []
        p_v_list = []
        for k in price_dict.keys():
            p_k_list.append(k)
            p_v_list.append('%%(%s)s' % k)
        price_sql = price_sql % (','.join(p_k_list), ','.join(p_v_list), )

        cursor = self.db_conn.connect()
        cursor.execute(price_sql, price_dict)
        self.db_conn.close()

    def update_price(self, nid, price_dict):

        sql = """update price set %s where nid=%s"""
        value_list = []
        for k, v in price_dict.items():
            value_list.append('%s=%%(%s)s' % (k, k))
        sql = sql % (','.join(value_list), nid )

        cursor = self.db_conn.connect()
        cursor.execute(sql, price_dict)
        self.db_conn.close()

    def fetch_product_pv(self, product_id):

        sql = """select timespan,count(nid) as pv from product_view where product_id=%s group by timespan"""

        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, product_id)
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_product_uv(self, product_id):

        sql = """select timespan, count(1) as uv from (select ip,timespan,count(1) from product_view where product_id=%s group by timespan,ip) as B group by timespan"""

        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, product_id)
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def add_product_puv(self, product_id, ip, current_date, current_timestamp):
        sql = 'insert into product_view(product_id,ip,ctime,timespan) values(%s,%s,%s,%s)'
        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, (product_id, ip, current_date, current_timestamp,))
        self.db_conn.close()

    def fetch_super_new_product(self):
        """
        获取首页新品上市的数据
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            price.nid as nid,
            product.title as title,
            product.img as img,
            price.selling_price as selling_price,
            product.nid as product_id

        FROM
            super_product
        LEFT JOIN price ON super_product.price_id = price.nid
        LEFT JOIN product ON product.nid = price.product_id

        where super_product.super_type =1
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_super_excellent_product(self):
        """
        获取首页精品推荐数据
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            price.nid as nid,
            product.title as title,
            product.img as img,
            price.selling_price as selling_price,
            product.nid as product_id

        FROM
            super_product
        LEFT JOIN price ON super_product.price_id = price.nid
        LEFT JOIN product ON product.nid = price.product_id

        where super_product.super_type =2
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_limit_price_and_product(self, subsite_caption):
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            price.nid as nid,
            product.title as title,
            product.img as img,
            price.selling_price as selling_price,
            product.nid as product_id
        FROM
            price
        LEFT JOIN product ON product.nid = price.product_id
        LEFT JOIN category ON product.category_id = category.nid
        LEFT JOIN upper_category ON category.favor_id = upper_category.nid
        LEFT JOIN subsite ON upper_category.favor_id = subsite.nid

        where subsite.caption = %s
        group by product.nid
        order by price.nid DESC

        limit 6 offset 0
        """
        cursor.execute(sql,(subsite_caption,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_product_and_merchant(self, product_id):
        sql = """
        select
            product.nid,
            product.title,
            product.img,
            merchant.name,
            merchant.business_phone,
            merchant.business_mobile,
            merchant.qq

        from product

        left join merchant on product.merchant_id = merchant.nid

        where product.nid = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchone()
        self.db_conn.close()
        return result

    def fetch_price_list(self, product_id):

        sql = """
            select
                price.nid as price_id,
                product.nid as product_id,
                price.standard,
                price.price,
                price.selling_price
            from price

            left join product on product.nid = price.product_id

            where product.nid = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_price_detail(self, price_id):
        sql = """
            select
                price.nid,
                price.standard,
                price.price,
                price.selling_price
            from price
            where price.nid = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (price_id,))
        result = cursor.fetchone()
        self.db_conn.close()
        return result

    def fetch_image_list(self, product_id):
        sql = """
            select
                src as img
            from product_img

            where product_img.product_id = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_detail_list(self, product_id):
        sql = """
            select
                name,
                value
            from product_detail

            where product_detail.product_id = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_comment_list(self, product_id):
        sql = """
            select
                content,
                username,
                comment.ctime
            from comment
            left join userinfo on comment.user_id = userinfo.nid

            where product_id = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_comment_count(self, product_id, fine):
        """

        :param product_id: 商品ID
        :param fine: 1表示满意，2表示不满意
        :return:
        """
        sql = """
            select
                count(1) as count
            from comment
            where product_id = %s and fine = %s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id, fine))
        result = cursor.fetchone()
        self.db_conn.close()
        return result['count']

