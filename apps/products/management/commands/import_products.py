import openpyxl
from django.core.management.base import BaseCommand, CommandError
from apps.products.models import Product
from decimal import Decimal
from django.db import transaction

REQUIRED=['name','description','price','stock_quantity']

class Command(BaseCommand):
    help='Import products from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self,*args,**opts):
        path=opts['file']
        try:
            wb=openpyxl.load_workbook(path)
        except Exception as e:
            raise CommandError(e)

        ws=wb.active
        headers=[(h or '').lower() for h in next(ws.iter_rows(min_row=1,max_row=1,values_only=True))]
        if any(c not in headers for c in REQUIRED):
            raise CommandError("Missing columns")

        idx={c:headers.index(c) for c in REQUIRED}
        created=updated=failed=0

        for row in ws.iter_rows(min_row=2, values_only=True):
            try:
                name=str(row[idx['name']]).strip()
                desc=row[idx['description']] or ''
                price=Decimal(str(row[idx['price']]))
                stock=int(row[idx['stock_quantity']])
                if price<=0 or stock<0: raise ValueError("Bad values")
                with transaction.atomic():
                    obj,new=Product.objects.update_or_create(
                        name=name,
                        defaults={'description':desc,'price':price,'stock_quantity':stock}
                    )
                created+=1 if new else updated+=1
            except Exception as e:
                failed+=1
                self.stderr.write(str(e))

        self.stdout.write(f"Created={created}, Updated={updated}, Failed={failed}")
