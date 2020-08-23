from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class ClassCustomizes(ModelView):
    column_labels = dict(class_name="Lớp", total_students="tổng số học sinh", grade="Khối")
    form_columns = ('class_name', 'total_students', 'grade')


    def is_accessible(self):
        return current_user.is_authenticated