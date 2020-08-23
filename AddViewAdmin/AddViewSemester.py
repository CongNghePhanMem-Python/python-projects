from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.SemesterCustomize import SemesterCustomize
from QLHS.models import Semesters

admin.add_view(SemesterCustomize(Semesters, db.session,name="HỌC KÌ"))