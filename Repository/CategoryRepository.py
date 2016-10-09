#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.Category import ICategoryRepository
from Repository.DbConnection import DbConnection


class CategoryRepository(ICategoryRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_all_category(self):
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            subsite.nid as i1,
            subsite.caption as c1,
            upper_category.nid as i2,
            upper_category.caption as c2,
            category.nid as i3,
            category.name as c3
        FROM
            category
        LEFT JOIN upper_category ON category.favor_id = upper_category.nid
        LEFT JOIN subsite ON upper_category.favor_id = subsite.nid
        """
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result
