import datetime

from mongoengine import (
    DateTimeField,
    Document,
    EmailField,
    EmbeddedDocument,
    ListField,
    StringField,
)


class Accounts(EmbeddedDocument):
    username = StringField(
        required=True,
        unique=True,
    )


class User(Document):
    email = EmailField(
        required=True,
        unique=True,
    )
    password = StringField(
        required=True,
    )
    accounts = ListField()
    modified_at = DateTimeField(default=datetime.datetime.now)
    created_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)
