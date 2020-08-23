from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class GradeCustomizes(ModelView):
    column_labels = dict(grade_name='Khối')
    form_columns = ('grade_name',)

    def is_accessible(self):
        return current_user.is_authenticated

