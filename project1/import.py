import os 
import csv 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    f= open("books.csv")
    reader1 = csv.reader(f)
    for ISBN ,TITLE ,AUTHOR ,YEAR in reader1:
        db.execute("INSERT INTO books( isbn ,title ,author ,year) VALUES (:id, :id1 ,:id2 , :id3 )",{"id":ISBN , "id1": TITLE , "id2":AUTHOR, "id3": YEAR})
        print(TITLE)

    db.commit()


if __name__ == "__main__":
    main()
