from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class SubjectCustomize(ModelView):
    column_labels = dict(subject_name="Tên môn học", coefficient="Hệ số môn học")
    form_columns = ("subject_name", "coefficient",)

    def is_accessible(self):
        return current_user.is_authenticated
