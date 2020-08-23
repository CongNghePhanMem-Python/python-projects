from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class SemesterCustomize(ModelView):
    column_labels = dict(semester_name='Học Kì')
    form_columns = ('semester_name',)

    def is_accessible(self):
        return current_user.is_authenticated
