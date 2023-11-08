from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from app import app, db
from app.models import Category, Product

admin = Admin(app=app, name="Quản Trị Bán Hàng", template_mode ="bootstrap4")

class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))