from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class GpaCustomize(ModelView):
    column_labels = dict(mark='Điểm tổng môn học', mark_gpa="điểm trung bình môn")

    def is_accessible(self):
        return current_user.is_authenticated
