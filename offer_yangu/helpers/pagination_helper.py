
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_query_description = 'Inform the page. Starting with 1. Default: 1'
    page_size_query_param = 'limit'
    page_size_query_description = 'Limit per page, Default: 10.'
    max_page_size = settings.MAX_PAGE_SIZE

    def create_paginated_data_dict(self, data):
        """
        create a pagination data dictionary
        """
        return {
            "paginationMeta":   {
                "currentPage": self.page.number,
                "currentPageSize": len(data),
                "totalPages": self.page.paginator.num_pages,
                "totalRecords": self.page.paginator.count,
            },
            'results': data
        }

    def get_paginated_response(self, data):
        """
        Overide the default get_paginated_response()
        """
        return Response(
            self.create_paginated_data_dict(data)
        )
