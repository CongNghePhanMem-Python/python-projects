from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MarkCustomizes(ModelView):
    column_labels = dict(subject= "Tên môn học", student= "Tên học sinh", mark_1="Điểm kiểm tra miệng",
                         mark_2="Điểm kiểm tra 15 phút", mark_3="Điểm kiểm tra 1 tiết", mark_semester="Điểm thi học kì",
                         mark_total="Tổng điểm")
    form_excluded_columns = ("gpa",)
    def is_accessible(self):
        return current_user.is_authenticated