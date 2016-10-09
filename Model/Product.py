#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import json

class IProductRepository:
    pass


class ProductModel:
    pass


class ProductService:

    def __init__(self, product_repository):
        self.productRepository = product_repository

    def get_page_by_merchant_id(self, merchant_id, start, row):
        count = self.productRepository.fetch_count_by_merchant_id(merchant_id)
        result = self.productRepository.fetch_page_by_merchant_id(merchant_id, start, row)
        return count, result

    def get_product_by_id(self, merchant_id, product_id):
        result = self.productRepository.fetch_product_by_id(merchant_id, product_id)
        return result

    def create_product(self, merchant_id, input_dict):

        product_dict = {
            'merchant_id': merchant_id,
            'title': input_dict['title'],
            'img': input_dict['img'],
            'category_id': 1,
            'ctime': time.strftime('%Y-%m-%d')
        }
        detail_list = json.loads(input_dict['detail_list'])
        img_list = json.loads(input_dict['img_list'])
        self.productRepository.add_product(product_dict, detail_list, img_list)

    def get_price_by_product_id(self, merchant_id, product_id):
        result = self.productRepository.fetch_price_by_product_id(merchant_id, product_id)
        return len(result), result

    def get_product_detail(self, merchant_id, product_id):
        is_valid = self.productRepository.fetch_product_by_id(merchant_id, product_id)
        if not is_valid:
            raise Exception('商品不存在')

    def create_price(self, merchant_id, product_id, input_dict):

        # 检查当前用户是否有权限为该商品增加规格
        is_valid = self.productRepository.fetch_product_by_id(merchant_id, product_id)
        if not is_valid:
            raise Exception('无权创建规格')

        self.productRepository.add_price(input_dict)

    def update_price(self, merchant_id, product_id, nid, input_dict):

        # 检查当前用户是否有权限为该商品增加规格
        is_valid = self.productRepository.fetch_product_by_id(merchant_id, product_id)
        if not is_valid:
            raise Exception('无权更新规格')

        self.productRepository.update_price(nid, input_dict)

    def get_upv(self, merchant_id, product_id):
        is_valid = self.productRepository.fetch_product_by_id(merchant_id, product_id)
        if not is_valid:
            raise Exception('无权获取PUV')
        pv = self.productRepository.fetch_product_pv(product_id)
        uv = self.productRepository.fetch_product_uv(product_id)
        return [{'name': 'pv', 'data': pv}, {'name': 'uv', 'data': uv}]

    def create_puv(self, product_id, ip):

        import time
        import datetime

        if not self.productRepository.exist_product_by_pid(product_id):
            raise Exception('商品ID不存在')

        current_date = time.strftime('%Y-%m-%d')
        current_timestamp = time.mktime(datetime.datetime.strptime(current_date, "%Y-%m-%d").timetuple()) * 1000

        self.productRepository.add_product_puv(product_id, ip, current_date, current_timestamp)

    def fetch_index_product(self):

        super_new_list = self.productRepository.fetch_super_new_product()
        super_excellent_list = self.productRepository.fetch_super_excellent_product()

        a = self.productRepository.fetch_limit_price_and_product('家具城')
        b = self.productRepository.fetch_limit_price_and_product('建材城')
        c = self.productRepository.fetch_limit_price_and_product('家具家装')
        return {
            'super_new_list': super_new_list,
            'super_excellent_list': super_excellent_list,
            'furniture': a,
            'building_materials': b,
            'decoration': c
        }


    def fetch_product_detail(self, product_id, price_id):
        product_detail = self.productRepository.fetch_product_and_merchant(product_id)
        price_detail = self.productRepository.fetch_price_detail(price_id)
        price_list = self.productRepository.fetch_price_list(product_id)

        image_list = self.productRepository.fetch_image_list(product_id)
        detail_list = self.productRepository.fetch_detail_list(product_id)
        comment_list = self.productRepository.fetch_comment_list(product_id)

        fine = self.productRepository.fetch_comment_count(product_id, 1)
        no_fine = self.productRepository.fetch_comment_count(product_id, 2)


        return {
            'product_detail': product_detail,
            'price_detail': price_detail,
            'price_list': price_list,
            'image_list': image_list,
            'detail_list': detail_list,
            'comment_list': comment_list,
            'comment_count': {'fine': fine, 'fine_percent': fine/(fine+no_fine) * 100 if fine else 0, 'no_fine': no_fine, 'no_fine_percent': no_fine/(fine+no_fine)* 100 if no_fine else 0,'total': fine+no_fine}

        }


