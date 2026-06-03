from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

conn = engine.connect()

print("Database created successfully!")

conn.close()