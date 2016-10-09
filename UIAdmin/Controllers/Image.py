#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import tornado.web
from Infrastructure import Commons
from ..Core.HttpRequest import AdminRequestHandler


class UploadImageHandler(AdminRequestHandler):

    def post(self, *args, **kwargs):
        ret = {'status': False, 'data': '', 'summary': ''}
        try:
            file_metas = self.request.files["img"]
            for meta in file_metas:
                file_name = meta['filename']

                file_path = os.path.join('Statics', 'Admin', 'Upload', Commons.generate_md5(file_name))
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
            ret['status'] = True
            ret['data'] = file_path
        except Exception as ex:
            ret['summary'] = str(ex)
        self.write(json.dumps(ret))