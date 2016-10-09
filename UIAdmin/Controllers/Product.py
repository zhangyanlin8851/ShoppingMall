#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import tornado.web
import datetime
from Model.Product import ProductService
from Repository.ProductRepository import ProductRepository
from Infrastructure.JsonEncoder import JsonCustomEncoder
from UIAdmin.Forms.Product import JdProductForm
from UIAdmin.Forms.Product import JdProductPriceForm
from ..Core.HttpRequest import AdminRequestHandler



class ProductManagerHandler(AdminRequestHandler):
    """
    商品管理页面
    """
    def get(self, *args, **kwargs):

        self.render('Product/JdProductManager.html')



class JdProductHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):

        # 根据参数，获取产品信息（type：自营（商户ID），type：所有商品）
        # 后台管理用户登陆成功后，Session中保存自营ID
        # 自营ID＝1
        ret = {'status': False, 'message': '', 'total': 0, 'rows': []}
        try:
            # 手动获取京东自营ID为14
            merchant_id = 14
            page = int(self.get_argument('page', 1))
            rows = int(self.get_argument('rows', 10))
            start = (page-1) * rows
            service = ProductService(ProductRepository())
            total, result = service.get_page_by_merchant_id(merchant_id, start, rows)
            ret['status'] = True
            ret['total'] = total
            ret['rows'] = result
        except Exception as e:
            ret['message'] = str(e)
        self.write(json.dumps(ret))



class JdProductEditHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Product/JdProductEdit.html')

    def post(self, *args, **kwargs):
        ret = {'status': False, 'summary': '', 'detail': ""}
        form = JdProductForm()
        try:
            is_valid = form.valid(self)
            if is_valid:
                # print(is_valid, form._error_dict, form._value_dict)
                merchant_id = 14
                service = ProductService(ProductRepository())
                service.create_product(merchant_id, form._value_dict)
                ret['status'] = True
            else:
                ret['detail'] = form._error_dict
        except Exception as e:
            ret['summary'] = str(e)

        self.write(json.dumps(ret))



class JdProductPriceManagerHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):
        ret = {'status': False, 'summary': '', 'data': {}}
        try:
            product_id = self.get_argument('productid', None)
            if not product_id:
                raise Exception('请输入商品ID')
            merchant_id = 14
            service = ProductService(ProductRepository())
            result = service.get_product_by_id(merchant_id=merchant_id, product_id=product_id)
            if not result:
                raise Exception('未获取商品信息')
            ret['status'] = True
            ret['data'] = result
        except Exception as e:
            ret['summary'] = str(e)

        self.render('Product/JdProductPriceManager.html', **ret)


class JdProductPriceHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):

        ret = {'status': False, 'summary': '', 'total': 0, 'rows': []}
        try:
            product_id = self.get_argument('productid', None)
            if not product_id:
                raise Exception('商品ID不能为空')
            merchant_id = 14
            service = ProductService(ProductRepository())
            total, result = service.get_price_by_product_id(merchant_id=merchant_id, product_id=product_id)
            ret['total'] = total
            ret['rows'] = result
            ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)

        self.write(json.dumps(ret, cls=JsonCustomEncoder))

    def post(self, *args, **kwargs):
        ret = {'status': False, 'summary': '', 'detail': {}}
        try:
            form = JdProductPriceForm()
            is_valid = form.valid(self)
            if is_valid:
                form._value_dict.pop('nid')
                merchant_id = 14
                service = ProductService(ProductRepository())
                service.create_price(merchant_id, form._value_dict['product_id'], form._value_dict)
            else:
                ret['detail'] = form._error_dict
                raise Exception('输入内容不合法')
            ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)

        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        ret = {'status': False, 'summary': '', 'detail': {}}
        try:
            form = JdProductPriceForm()
            is_valid = form.valid(self)
            if is_valid:
                nid = form._value_dict.pop('nid')
                merchant_id = 14
                service = ProductService(ProductRepository())
                service.update_price(merchant_id, form._value_dict['product_id'], nid, form._value_dict)
            else:
                ret['detail'] = form._error_dict
                raise Exception('输入内容不合法')
            ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)

        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        pass



class JdProductDetailHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):
        # 数据库中获取数据，显示在页面

        merchant_id = 14
        product_id = self.get_argument('productid', None)
        service = ProductService(ProductRepository())
        series = service.get_product_detail(merchant_id, product_id)

        self.render('Product/JdProductDetail.html', product_id=product_id)


class JdProductViewHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):
        ret = {'status': False, 'summary': '', 'data': []}
        try:
            merchant_id = 14
            product_id = self.get_argument('product_id', None)
            if not product_id:
                raise Exception('请输入产品ID')

            service = ProductService(ProductRepository())
            series = service.get_upv(merchant_id, product_id)
            ret['data'] = series
            ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)
        self.write(json.dumps(ret))


class TestProductViewHandler(AdminRequestHandler):

    def get(self, *args, **kwargs):
        summary = 'success'

        product_id = self.get_argument('productid', None)
        try:
            if not product_id:
                raise Exception('请输入商品ID')
            ip = self.request.remote_ip
            service = ProductService(ProductRepository())
            service.create_puv(product_id, ip)
        except Exception as e:
            summary = str(e)
        self.write(summary)