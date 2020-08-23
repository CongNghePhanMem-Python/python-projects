from flask import render_template
from flask_admin import BaseView, expose
from flask_login import current_user


class RegisterView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render("admin/register.html")

    def is_accessible(self):
        return not current_user.is_authenticated