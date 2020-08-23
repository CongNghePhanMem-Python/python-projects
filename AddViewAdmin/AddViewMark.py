from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.MarkCustomize import MarkCustomizes
from QLHS.models import Marks

admin.add_view(MarkCustomizes(Marks, db.session, name="ĐIỂM MÔN HỌC"))