from sqlmodel import create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

## alternative way
# from sqlmodel import create_engine
# import models


# sqlite_file_name = "database1.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url)
# SQLModel.metadata.create_all(engine)