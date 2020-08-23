from QLHS import admin
from QLHS.Logout.Logout import LogoutView

admin.add_view(LogoutView(name="LOG OUT"))