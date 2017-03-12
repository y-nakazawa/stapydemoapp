from django.conf.urls import url
from cms import views
from cms.views import BookList

urlpatterns = [
    # 書籍
    url(r'^book/$', BookList.as_view(), name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除
]