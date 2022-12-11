import datetime

from mongoengine import (
    BooleanField,
    DateTimeField,
    Document,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    ObjectIdField,
    StringField,
)


class Accounts(EmbeddedDocument):
    username = StringField(
        required=True,
        unique=True,
    )
    biography = StringField(max_length=300)
    alias = StringField(max_length=300)
    links = ListField(
        ObjectIdField()
    )  # TODO: Add DB field to ObjectIdField -> Link
    active = BooleanField(default=True)


class User(Document):
    email = EmailField(
        required=True,
        unique=True,
    )
    password = StringField(required=True)
    accounts = ListField(EmbeddedDocumentField(Accounts))
    modified_at = DateTimeField(default=datetime.datetime.now)
    created_at = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)
