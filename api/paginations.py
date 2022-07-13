from rest_framework import pagination

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'per_page'


class PostStandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'