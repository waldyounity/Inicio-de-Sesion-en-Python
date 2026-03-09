from flask_login import current_user
from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from .extensions import admin, db
from .models import User

# --- Clase para la Gestión de Personal (SOLO ADMIN) ---
class AdminModelView(ModelView):
    # Corregí un pequeño detalle aquí: es column_exclude_list (con 'n')
    column_exclude_list = ["password"] 
    
    def is_accessible(self):
        # LA MAGIA: Solo entra si está logueado Y su rol es admin
        return current_user.is_authenticated and current_user.role == 'admin'
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))
    
    # Encriptamos el password al crearse
    def on_model_change(self, form, model, is_created):
        if hasattr(form, 'password') and form.password.data:
            model.set_password(form.password.data)
            
    # Activar Modales
    create_modal = True
    edit_modal = True
    can_view_details = True
    details_modal = True
    
def configuracion_admin():
    # Solo mostramos la tabla de usuarios protegida
    admin.add_view(AdminModelView(User, db.session, name="Gestión de Personal"))