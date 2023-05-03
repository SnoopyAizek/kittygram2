from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CatsPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'pageNumber'
    page_size_query_param = 'pageSize'
    max_page_size = 1000

    def get_paginated_response(self, data):
        pagination = OrderedDict([
            ('totalItems', self.page.paginator.count),
            ('currentPage', self.page.number),
            ('pageSize', self.page.__len__()),
        ])
        return Response(OrderedDict([
            ('data', data),
            ('pagination', pagination)

        ]))
