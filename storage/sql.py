from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sql_setup.db_setup import Institution, Base, Course, Session, Media, Tag, Category
from datetime import datetime
from storage import StorageBase
 

class SQL(StorageBase):
    #do not override here, place this in the YAML configuration config.yaml
    
    def __init__(self):
        config = self.get_config(self.__class__.__name__)  # call the super init method to get config

        engine = create_engine(config['connection_string'])
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a instance
        Base.metadata.bind = engine
         
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def store_courses(self, courses):
        session = self.session
        #we can't bulk upsert so lets loop and upsert
        for course in courses:

            i = course['institution']
            new_institution = Institution(
                id=i.get("id"),
                name=i.get("name", "None"),
                description=i.get("name"),
                website=i.get("website"),
                logo_url=i.get("logo_url"),
                city=i.get("city"),
                state=i.get("state"),
                country=i.get("country")
            )

            new_institution = session.merge(new_institution)

            session.add(new_institution)
            session.commit()

            new_course = Course(
                id=course.get("id"),
                name=course.get("course_name"),
                language=course.get("language"),
                instructor=course.get("instructor"),
                providers_id=course.get("providers_id"),
                short_description=course.get("short_description"),
                full_description=course.get("full_description"),
                course_url=course.get("course_url"),
                workload=course.get("workload"),
                institution=new_institution
            )

            new_course = session.merge(new_course)
            session.add(new_course)
            session.commit()

            for s in course['sessions']:
                new_session = Session(
                    id=s.get("provider_session_id"),
                    duration=s.get("duration", None),
                    start_date=datetime.strptime(s.get("start_date"), "%Y%m%d"),
                    course=new_course
                )

                new_session = session.merge(new_session)
                session.add(new_session)
                session.commit()

            media = course['media']
            new_media = session.query(Media).filter_by(course=new_course).first()
            if not new_media:
                new_media = Media(
                    course=new_course,
                    photo_url=media.get("photo_url", None),
                    video_url=media.get("video_url", None),
                    video_type=media.get("video_type", None),
                    video_id=media.get("video_id", None),
                    icon_url=media.get("icon_url", None)
                )
            session.add(new_media)
            session.commit()

            for t in course['tags']:
                new_tag = session.query(Tag).filter_by(tag=t).first()
                if not new_tag:
                    new_tag = Tag(tag=t)
                new_course.tags.append(new_tag)
                session.commit()

            for c in course['categories']:
                new_cat = Category(
                    id=c.get("id"),
                    name=c.get("name"),
                    description=c.get("description", None)
                )
                new_cat = session.merge(new_cat)
                new_course.categories.append(new_cat)
                session.commit()




