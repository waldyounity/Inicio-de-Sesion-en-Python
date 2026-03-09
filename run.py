from app.__init__ import create_app
from app.extensions import db
from app.models import User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # Crea el usuario admin automáticamente si no existe en la BD
        if not User.query.filter_by(username='admin').first():
            usuario = User(username='admin', role='admin')
            usuario.set_password('123456')
            db.session.add(usuario)
            db.session.commit()
            print("✅ Usuario admin creado por defecto.")
            
    app.run(debug=True)