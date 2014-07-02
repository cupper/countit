# -*- coding: utf-8 -*-

import os
from datetime import datetime

def add_category(name, image=None):
    c = None
    if image:
        c = Category.objects.get_or_create(name=name, image=image)[0]
    else:
        c = Category.objects.get_or_create(name=name)[0]
    return c

def add_item(name, price, cat_list, date=datetime.now()):
    p = Item.objects.create(name=name, price=price, date=date)
    for c in cat_list:  
        p.category_list.add(add_category(c))
    return p

def populate():
    add_item(name='Хлеб', price=16, cat_list=('Еда', 'Домашняя еда'))
    add_item(name='Кефир', price=42, cat_list=('Еда', 'Домашняя еда'))

    add_item(name='Проездной метро 20', price=540, cat_list={'Проезд'})
    add_item(name='Пивной паб', price=800, cat_list={'Отдых', 'Кафе'})
    add_item(name='Моб. связь', price=200, cat_list={'Счета', 'Коммуникация'})

    print "Category list:"
    for c in Category.objects.all():
        print "- {0}".format(str(c))

    print "Item list:"
    for i in Item.objects.all():
        print "%s, %d руб., %s" % (i, i.price, ",".join(str(c) for c in i.category_list.all()))


# Start execution here!
if __name__ == '__main__':
    print "Starting CountIt population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'countit.settings')
    from project.models import Category, Item
    populate()
