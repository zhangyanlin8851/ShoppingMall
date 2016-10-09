#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ICategoryRepository:

    pass




class CategoryService:

    def __init__(self, category_repository):
        self.categoryRepository = category_repository

    def get_all_category(self):

        # result = [
        #     {
        #         'nid': '1',
        #         'caption': '家具城',
        #         'data': [
        #             {
        #                 'nid': 1,
        #                 'caption': '卧室',
        #                 'data': [
        #                     {'nid': 1 ,'caption': '床'},
        #                     {'nid': 1 ,'caption': '床垫'},
        #                 ]
        #             }
        #             ,
        #             {
        #                 'nid': 2,
        #                 'caption': '客厅',
        #                 'data': []
        #             }
        #         ]
        #     },
        #     {'nid': '2', 'caption': '建材城', 'data': []}
        # ]
        result = []
        temp = {}
        category_list = self.categoryRepository.fetch_all_category()
        for item in category_list:
            if item['c1'] not in temp:
                temp[item['c1']] = {item['c2']: {item['c3']: {}}}
                a = {
                    'nid': item['i1'],
                    'caption': item['c1'],
                    'data': [
                        {
                            'nid': item['i2'],
                            'caption': item['c2'],
                            'data': [
                                {
                                    'nid': item['i3'],
                                    'caption': item['c3'],
                                }
                            ]
                        }
                    ]
                }
                result.append(a)
                continue
            if item['c2'] not in temp[item['c1']]:
                temp[item['c1']][item['c2']] = {item['c3']: {}}
                b = {
                    'nid': item['i2'],
                    'caption': item['c2'],
                    'data': [
                        {
                            'nid': item['i3'],
                            'caption': item['c3'],
                        }
                    ]
                }
                for i in range(len(result)):
                    if result[i]['nid'] == item['i1']:
                        result[i]['data'].append(b)
                        break
                continue
            if item['c3'] not in temp[item['c1']][item['c2']]:
                temp[item['c1']][item['c2']][item['c3']] = {}
                c = {
                    'nid': item['i3'],
                    'caption': item['c3'],
                }

                for i in range(len(result)):
                    if result[i]['nid'] == item['i1']:
                        for j in range(len(result[i]['data'])):
                            if result[i]['data'][j]['nid'] == item['i2']:
                                result[i]['data'][j]['data'].append(c)
                                break
                continue

        return result
