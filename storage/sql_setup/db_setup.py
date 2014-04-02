from sqlalchemy import Column, ForeignKey, Date, String, Text, Integer, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import yaml


def get_settings():
    config = yaml.load(open('config.yaml'))
    return config['storage_configs'].get("SQL", None)
 
Base = declarative_base()
 

course_tag_association_table = Table(
    'course_tag_association',
    Base.metadata,
    Column('course_id', String(50), ForeignKey('course.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

course_category_association_table = Table(
    'course_category_association',
    Base.metadata,
    Column('course_id', String(50), ForeignKey('course.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)


class Institution(Base):
    __tablename__ = 'institution'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text)
    website = Column(String(250))
    logo_url = Column(String(250))
    city = Column(String(250))
    state = Column(String(250))
    country = Column(String(250))


class Course(Base):
    __tablename__ = "course"
    id = Column(String(50), primary_key=True)
    name = Column(String(250), nullable=False)
    language = Column(String(250))
    instructor = Column(String(250))
    providers_id = Column(String(50), nullable=False)
    short_description = Column(Text)
    full_description = Column(Text)
    course_url = Column(String(250))
    workload = Column(String(250))
    institution_id = Column(String(50), ForeignKey('institution.id'))
    institution = relationship(Institution)
    tags = relationship("Tag", secondary=course_tag_association_table)
    categories = relationship("Category", secondary=course_category_association_table)


class Session(Base):
    __tablename__ = "session"
    id = Column(Integer, primary_key=True)
    course_id = Column(String(50), ForeignKey('course.id'))
    course = relationship(Course)
    duration = Column(String(250))
    start_date = Column(Date)


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    course_id = Column(String(50), ForeignKey('course.id'))
    course = relationship(Course)
    photo_url = Column(String(250))
    icon_url = Column(String(250))
    video_url = Column(String(250))
    video_type = Column(String(20))
    video_id = Column(String(50))


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True, nullable=False)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    description = Column(Text)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(get_settings()['connection_string'])
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
