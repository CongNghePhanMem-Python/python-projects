from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.SubjectCustomize import SubjectCustomize
from QLHS.models import Subjects

admin.add_view(SubjectCustomize(Subjects, db.session, name="MÔN HỌC"))