from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.GradeCustomize import GradeCustomizes
from QLHS.models import Grades

admin.add_view(GradeCustomizes(Grades, db.session, name="KHỐI"))
