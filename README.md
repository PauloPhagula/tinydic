# TinyDIC [![Build Status](https://travis-ci.org/dareenzo/tinydic.svg?branch=master)](https://travis-ci.org/dareenzo/tinydic)

Tiny Python Dependency Injection Container.

## Why *TinyDIC*?

I was looking for a Dependency Injection Container in Python, googled a
bit, but only found solutions which were huge and use constructs -- such as
decorators and so on -- which I'm not so fond of, or at least don't
find a good justification for their use, for such a simple and small
thing as an DIC.

So, inspired (or copying) the PHP [Twittee IoC](https://github.com/fabpot-graveyard/twitte)
written by [Fabien Potencier](http://fabien.potencier.org) of [symfony](http://symfony.com) fame, I
wrote this small class.

I've had lots of help on [Stackoverflow reviews](http://codereview.stackexchange.com/questions/146964/simple-python-ioc) ... 
to setup this -- thanks you so much!

Last but not least, I've to say that this is a very tiny thing meant for small personal projects so I don't recommend production use. 
For something more proper and mature I recommend you check [Pymple](https://github.com/BernhardPosselt/pymple)

## Installation

```sh
pip install tinydic
```

## Usage

```python
from tinydic import Container


class MailService:

    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server
 
    def send_mail(self, to, subject, contents):
        # uses stored settings to send email
        pass


def email_validator_service(container):
    def functor(email):
        return container.MAIL_REGEX.match(email)
    return functor


class MailClient:

    def __init__(self, mail_service, validate_email):
        self.mail_service = mail_service
        self.validate_email = validate_email

    def send_mail(self, to, message):
        if self.validate_email(to):
            self.mail_service.send_mail(a, b)

# create container
container = Container()

# register constants / params
container.MAIL_REGEX = 'ugly long regex here'
container.username = 'spam' # container.register('username', 'spam', constant = True)
container.password = 'eggs'
container.server = 'foo.bar.com'

# register objects / services
container.mail_service = lambda c: MailService(c.username, c.password, c.server))
# container.register('mail_service', lambda c: MailService(c.usernme, c.password, c.server), False)
container.email_validator = email_validator_service
container.client = lambda c: MailClient(c.mail_service, c.email_validator)

container.client.send_mail('eggs@foo.bar.com', 'yo')
```


