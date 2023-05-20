from src import db

class Data_3(db.Model):
    __tablename__ = "data_3"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create(name):  # create new entity
        entity = Data_3(name)
        db.session.add(entity)
        db.session.commit()

    @staticmethod
    def get_entities():  # return list of entities
        return [{'entity_id': i.id, 'name': i.name} for i in Data_3.query.order_by('id').all()]
