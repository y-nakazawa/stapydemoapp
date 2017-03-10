from django.shortcuts import render
from django.views.generic import ListView

from cms.models import Book


class BookList(ListView):
    """書籍の一覧"""
    context_object_name = 'books'
    template_name = 'cms/book_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kw):
        self.object_list = Book.objects.all().order_by('id')  # 書籍を全件取得
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
