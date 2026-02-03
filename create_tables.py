# BLOG/create_tables.py
from flaskblog import app, db

print("Creating database tables...")
with app.app_context():
    # Drop all existing tables first
    db.drop_all()
    
    # Create new tables
    db.create_all()
    
    print("✅ Database tables created successfully!")
    print("📁 Database file should be at: site.db")