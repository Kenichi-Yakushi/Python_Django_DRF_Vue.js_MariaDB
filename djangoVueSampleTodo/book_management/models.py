from django.contrib.auth.models import User
from django.db import models


class Branch(models.Model):
    """
    図書館支店マスタ
    """
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    remark = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'book_management_m_branch'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=100)
    color = models.CharField('色(16進数)', max_length=7, default='#000000')

    class Meta:
        db_table = 'book_management_m_category'

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    書籍 著者名
    """
    name = models.CharField('著者名', max_length=256)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    書籍マスタ
    システムを使用するひとつの自治体が束ねる、n個の支店図書館すべてが所蔵する本
    """
    name = models.CharField('タイトル', max_length=256)
    thumbnail = models.ImageField('サムネイル', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='著者')
    lead_text = models.TextField('紹介文')
    amount = models.PositiveSmallIntegerField('数量')
    isbn = models.CharField('ISBNコード', max_length=20)
    publication_date = models.DateField('出版年月日')
    created_at = models.DateField('登録日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True, null=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    """
    システムを使用するひとつの自治体が束ねる、n個の支店図書館がそれぞれどの本をいくつ所蔵するか
    ある支店図書館にある本の数量合計が、Bookテーブルの amount と一致する
    """
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.book.name}({self.amount}) {self.branch.name}"


class Lending(models.Model):
    """
    貸出日と created_at は同じになる
    返却が終わると active が 0 になる
    """
    return_date = models.DateField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    active = models.BooleanField(default=1)
    customer_user = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    contact_user = models.ForeignKey(User, related_name='contact', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)
