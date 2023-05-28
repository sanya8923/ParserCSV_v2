from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:pajd6284jdk@localhost/db_parser', echo=True)
