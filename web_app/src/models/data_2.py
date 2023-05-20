from src import db

# ORM model for table
class Data_2(db.Model):
    __tablename__ = "data_2"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create(name):  # create new entity
        entity = Data_2(name)
        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def get_entities():  # return list of entities
        return [{'entity_id': i.id, 'name': i.name} for i in Data_2.query.order_by('id').all()]
