from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):

    def get_page_size(self, request):
        print(request.query_params)
        try:
            page_size = int(request.query_params.get("page_size", self.page_size))
            self.page_size = page_size
        except:
            pass

        return self.page_size