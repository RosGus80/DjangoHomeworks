from django.core.management import BaseCommand

import json

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_list = []
        with open('fixtures/category_fixtures.json', 'r') as file:
            read = json.load(file)
            for one in read:
                category_list.append(Category(name=one['fields']['name'], desc=one['fields']['desc'], pk=one['pk']))

        Category.objects.bulk_create(category_list)

        product_list = []
        with open('fixtures/product_fixtures.json', 'r') as file:
            read = json.load(file)
            for one in read:
                product_list.append(Product(name=one['fields']['name'],
                                            desc=one['fields']['desc'],
                                            preview=one['fields']['preview'],
                                            category=Category.objects.get(pk=one['fields']['category']),
                                            price=one['fields']['price'],
                                            date=one['fields']['date'],
                                            ChangeDate=one['fields']['ChangeDate']))

        Product.objects.bulk_create(product_list)
