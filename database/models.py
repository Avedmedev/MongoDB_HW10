from mongoengine import Document, StringField, ReferenceField, ListField, connect, CASCADE, DateTimeField, EmailField

connect(db='organizer', host='mongodb://localhost:27017/organizer')


class Owner(Document):
    login = StringField(required=True)
    hash = StringField(required=True)
    meta = {'collection': 'owners'}


class Person(Document):
    first_name = StringField(max_length=120, required=True)
    last_name = StringField(max_length=120, required=True)
    birth_date = DateTimeField()
    work_place = StringField(max_length=120)
    post_name = StringField(max_length=120)
    meta = {'collection': 'persons'}


class Phone(Document):
    phone_number = StringField(max_length=120, required=True, unique=True)
    description = StringField(max_length=120, required=False)
    person = ReferenceField(Person, reverse_delete_rule=CASCADE)
    meta = {'collection': 'phones'}


class Email(Document):
    email = EmailField(required=True, unique=True)
    description = StringField(max_length=120, required=False)
    person = ReferenceField(Person, reverse_delete_rule=CASCADE)
    meta = {'collection': 'emails'}
