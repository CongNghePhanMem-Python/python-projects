
from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.GpaCustomize import GpaCustomize
from QLHS.models import Gpas

admin.add_view(GpaCustomize(Gpas, db.session, name="ĐIỂM TRUNG BÌNH HỌC KÌ"))