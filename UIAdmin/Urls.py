#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .Controllers import Home
from .Controllers import Account
from .Controllers import Image
from .Controllers import Region
from .Controllers import Merchant
from .Controllers import Product

patterns = [
    # (r"/login.html$", Account.Login),
    (r"/index$", Home.IndexHandler),
    (r"/UploadImg.html$", Image.UploadImageHandler),
    (r"/ProvinceManager.html$", Region.ProvinceManagerHandler),
    (r"/province.html$", Region.ProvinceHandler),
    (r"/CityManager.html$", Region.CityManagerHandler),
    (r"/City.html$", Region.CityHandler),
    (r"/CountyManager.html$", Region.CountyManagerHandler),
    (r"/County.html$", Region.CountyHandler),
    (r"/MerchantManager.html$", Merchant.MerchantManagerHandler),
    (r"/Merchant.html$", Merchant.MerchantHandler),
    (r"/MerchantEdit.html$", Merchant.MerchantEditHandler),
    (r"/ProductManager.html$", Product.ProductManagerHandler),
    (r"/JdProduct.html$", Product.JdProductHandler),
    (r"/JdProductEdit.html$", Product.JdProductEditHandler),
    (r"/JdProductPriceManager.html$", Product.JdProductPriceManagerHandler),
    (r"/JdProductPrice.html$", Product.JdProductPriceHandler),
    (r"/JdProductDetail.html$", Product.JdProductDetailHandler),
    (r"/JdProductView.html$", Product.JdProductViewHandler),
    (r"/TextView.html$", Product.TestProductViewHandler),
]