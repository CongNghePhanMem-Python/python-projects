from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.StudentCustomize import StudentCustomize
from QLHS.models import Students

admin.add_view(StudentCustomize(Students, db.session, name="HỌC SINH"))