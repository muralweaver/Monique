# Kuvha PRM
Personal contacts manager. A place for notes, but for the people I keep in touch with.

- [Introduction](#introduction)
  - [Features](#This-api-functions-include)
  - [Who is it for?](#who-is-it-for)
  - [What Kuvha isn't](#what-kuvha-isnt)
  - [Getting started](#getting-started)
  - [Open thank you to open source](#open-thank-you-to-open-source)
  - [Kuvha API Documentation](#api-doc)


## Introduction

Kuvha is an open-source web application tool to organize the interactions with people you keep in touch with. Think of it as a [CRM](https://en.wikipedia.org/wiki/Customer_relationship_management).


### Who is it for?

In today's digital age, it's easy to lose touch. This project is to help people stay attentive and stay on top of the people that matter in order to be a better friend, mentor, sibling, sales person, networker.

> Your professional and personal life usually have a pretty clear line drawn between them. Yet sometimes, the tools you use in your professional life, such as a day planner and address book, could benefit you personally or even vice-versa.  
[Nicole Malczan](https://www.engagebay.com/blog/personal-crm/)


### What Kuvha isn't

 * Kuvha is not a social network and **never will be**. It's not meant to be social. In fact, it's for your eyes only.
 * Kuvha is not a smart assistant - it won't guess what you want to do.
 * Kuvha is not a tool that will scan your data and do nasty things with it.

## Getting started

### Prerequirements

### Download the code
- Clone this repo to your local drive.

### Local installation
- Open terminal window and navigate to your kuvha local drive directory
- Create new python virtual environment by running python3 -m venv venv
- Activate new virtual environment by running source venv/bin/activate
- Install project dependencies by running pip install -r requirements.txt

### Take it for a spin
- Make sure your python virtual environment activated source venv/bin/activate
- Start django application python3 manage.py runserver
- Done - try out the different API calls

### This api functions include:

- [x] Add contacts
  - [ ] Bulk add contacts
- [ ] Manage contacts
- [ ] Define relationships between contacts
- [ ] Reminders
- [ ] Auto reminders for birthdays
- [ ] Stay in touch with a contact by sending reminders at a given interval
- [x] Ability to add notes to a contact
- [ ] Ability to indicate how you've met someone
- [ ] Management of activities done with a contact
- [ ] Management of addresses and all the different ways to contact someone
- [ ] Space to write notes about your friends’ work, family, pets, gift ideas, money they owe you, and set reminders about important dates.
- [x] Basic journal e.g. how the day went
- [ ] Upload documents and photos
- [ ] Export and import of data
- [ ] Export a contact as vCard
- [ ] Ability to define custom activity types
- [ ] Multi users
- [ ] Labels to organize contacts
- [ ] Multi languages


## Open thank you to open source

Kuvha uses a lot of open source projects. The vision and generosity of the open source community has let us explore potential applications, ideas, algorithms and designs … for free! The hope is that by providing Kuvha as a free, open source project it will help other people the same way those free open source softwares have helped make this possible. 


Inspired by and obviously heavily referenced by the awesome open-source web application [Monica](https://github.com/monicahq)

## API Documentation
The complete documentation explains every API endpoint and gives you the ability to try them without writing any code.

https://documenter.getpostman.com/view/10061488/TVRg69Dd

## Useful Links

- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Adding Object Level Permissions](https://dragonprogrammer.com/object-level-permissions-drf/)
- [DRF File Upload](https://medium.com/@jxstanford/django-rest-framework-file-upload-e4bc8de669c0)
