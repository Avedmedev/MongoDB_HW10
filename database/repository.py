from datetime import datetime

from database.models import Owner, Person, Phone, Email
from bson import ObjectId


def get_user_by_login(login):
    owner = Owner.objects(login=login).first()
    return owner


def add_contact(name, phone_, email_):
    fn, ln = name.split()
    person = Person(first_name=fn, last_name=ln)
    person.save()

    phone = Phone(phone_number=phone_, person=person)
    phone.save()

    email = Email(email=email_, person=person)
    email.save()


def remove_phone_number(pk):
    phone = Phone.objects(pk=pk).first()
    phone.delete()


def remove_email(pk):
    email = Email.objects(pk=pk).first()
    email.delete()


def add_person_phone(id):
    phone_number = input("New phone number: ")
    description = input("Description: ")
    person = Person.objects(pk=ObjectId(id)).first()
    phone = Phone(phone_number=phone_number, description=description, person=person)
    phone.save()


def add_person_email(id):
    email = input("New email: ")
    description = input("Description: ")
    person = Person.objects(pk=ObjectId(id)).first()
    em = Email(email=email, description=description, person=person)
    em.save()


def update_contact(id):
    person = Person.objects(pk=ObjectId(id)).first()

    fn = input(f'first_name [{person.first_name}]:')
    if fn:
        person.first_name = fn

    ln = input(f'last_name [{person.last_name}]:')
    if ln:
        person.last_name = ln

    for phone in Phone.objects(person=person.pk).all():
        ph = input(f'phone_number [{phone.phone_number}/del]:')
        if ph == 'del':
            remove_phone_number(phone.pk)
            continue
        if ph:
            phone.phone_number = ph
        desc = input(f'phone description [{phone.description}]:')
        if desc:
            phone.description = desc
        phone.save()

    while True:
        if input("add phone number [y/n]") == 'y':
            add_person_phone(id)
        else:
            break

    for email in Email.objects(person=person.pk).all():
        em = input(f'email [{email.email}/del]:')
        if em == 'del':
            remove_email(email.pk)
            continue
        if em:
            email.email = em
        desc = input(f'email description [{email.description}]:')
        if desc:
            email.description = desc
        email.save()

    while True:
        if input("add email [y/n]") == 'y':
            add_person_email(id)
        else:
            break

    bd = input(f'Birth date [{person.birth_date}]:')
    if bd:
        person.birth_date = datetime.strptime(bd, "%d.%m.%y")

    pn = input(f'post [{person.post_name}]:')
    if pn:
        person.post_name = pn

    co = input(f'Company name [{person.work_place}]:')
    if co:
        person.work_place = co

    person.save()
    return (person.pk, person.first_name, person.last_name,
            [(ph.phone_number, ph.description) for ph in Phone.objects(person=person.pk).all()],
            [(em.email, em.description) for em in Email.objects(person=person.pk).all()],
            person.post_name, person.work_place,
            person.birth_date.strftime('%d.%m.%y') if isinstance(person.birth_date, datetime) else None)


def get_contacts():
    persons = Person.objects().all()
    return [(person.pk, person.first_name, person.last_name,
            [(ph.phone_number, ph.description) for ph in Phone.objects(person=person.pk).all()],
            [(em.email, em.description) for em in Email.objects(person=person.pk).all()],
            person.post_name, person.work_place,
             person.birth_date.strftime('%d.%m.%y') if isinstance(person.birth_date, datetime) else None)
            for person in persons]


def get_contact(id):
    person = Person.objects(pk=ObjectId(id)).first()
    return (person.pk, person.first_name, person.last_name,
            [(ph.phone_number, ph.description) for ph in Phone.objects(person=person.pk).all()],
            [(em.email, em.description) for em in Email.objects(person=person.pk).all()],
            person.post_name, person.work_place,
            person.birth_date.strftime('%d.%m.%y') if isinstance(person.birth_date, datetime) else None)


def remove_contact(id):
    person = Person.objects(pk=ObjectId(id)).first()
    person.delete()

