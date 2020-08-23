from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class StudentCustomize(ModelView):
    column_labels = dict(student_name='Họ và tên học sinh', gender='Giới tính', birthday='Ngày tháng năm sinh',
                         address='Địa chỉ', email='Email', classes='Lớp', semester='Học kì')
    form_excluded_columns = ("marks","gpas")
    can_view_details = True


    def is_accessible(self):
        return current_user.is_authenticated
    