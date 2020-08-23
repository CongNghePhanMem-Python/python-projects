from QLHS import admin, db
from QLHS.CustomizeRoleAdmin.ClassCustomize import ClassCustomizes
from QLHS.models import Classes

admin.add_view(ClassCustomizes(Classes, db.session, name="LỚP"))