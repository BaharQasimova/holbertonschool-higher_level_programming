from api import app, db

app.app_context():
    db.create_all()
    
