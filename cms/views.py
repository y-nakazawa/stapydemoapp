from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from cms.forms import BookForm
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


def book_edit(request, book_id=None):
    """書籍の編集"""
    if book_id:  # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:  # book_id が指定されていない (追加時)
        book = Book()
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            form.save()
            return redirect('cms:book_list')
    else:  # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')