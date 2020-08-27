![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Panda_icon.svg/240px-Panda_icon.svg.png)

# Monique [Work in progress]

A Personal Relationship Management tool

...

## Developer Installation

### Brief Explanation on Django

Django runs on an MVT (Model View Template) system which is different from MVC (Model View Controller) that powers Laravel.

**Model:** The model in Django sets out the schema for our database. With Django’s ORM, you can declare the fields, field types and any extra data for instance Meta information.

**View:** The View in Django, is where you set all of your code logic and algorithms. With the View, you can get some results from the database or manipulate some data. The view basically expects a request and a response. The response is usually a HTTP redirect, HTTP error (404), MimeTypes or a call to load a template.

**Template:** The template in Django is the plain HTML code with Django’s Template Language in it. DTL (Django Template Language) is the language you’ll be using to dynamically write your template. You can do almost everything you’d with python and any other language.

**Settings:** The settings file in Django, holds all the settings of your web app. It includes the secret key, templates directories, middlewares (security), static files (css,js), database settings and so on.

**Url:** This does the same thing as routing in Angular or Laravel. It helps to connect the view to a url.
> [Oyetoke Tobi Emmanuel](https://medium.com/fbdevclagos/how-to-build-a-todo-app-with-django-17afdc4a8f8c)



```...```

## API Documentation

<!--**The rest of this document describes how to use some parts of Monique's API**-->

#### Contacts

The Contact object is the core of what Monique is all about. The API allows you to create, delete and update your contacts. You can retrieve individual contacts as well as a list of all your contacts.

#### Journal entries

The Journal object allows to enter information that are not linked to a specific contact. You can use this to store general notes, or to use it like a personal diary.

List all the entries in your journal
```
GET /api/journal
```
**Response**
```
...  
{
        "id": 9,
        "account": 1,
        "title": "Title",
        "body": "Body",
        "date_created": "2020-08-17T18:38:49.009371Z",
        "date_modified": "2020-08-17T18:38:49.009240Z"
    },
    {
        "id": 11,
        "account": 1,
        "title": "Just another winter",
        "body": "Christmas has just past and tomorrow is New Years' Eve. We had a quiet Christmas, actually it got messed up. My father-in-law decided to act like an ass. So I had a bad start to the holidays. Now I find I have a reacurring bladder infection. I am now on my second round of antibiotics. I am still waiting for a break in my writing career. I was sent an email to write articles so I decided to go for it. The only problem is the pay is not great, but at this point I will do it. I am still waiting for a reply. As for New Year's I don't know what we are doing. I just hope this year brings some good fortune.",
        "date_created": "2020-08-18T11:43:08.767002Z",
        "date_modified": "2020-08-18T11:43:08.765903Z"
    }
]
```
Get a specific journal entry
```
GET /api/journal/:id
```

Create a journal entry
```
POST /api/journal/
```
**Response**
```
{
    "id": 11,
    "title": "Just another winter",
    "body": "Christmas has just past and tomorrow is New Years' Eve. We had a quiet Christmas, actually it got messed up. My father-in-law decided to act like an ass. So I had a bad start to the holidays. Now I find I have a reacurring bladder infection. I am now on my second round of antibiotics. I am still waiting for a break in my writing career. I was sent an email to write articles so I decided to go for it. The only problem is the pay is not great, but at this point I will do it. I am still waiting for a reply. As for New Year's I don't know what we are doing. I just hope this year brings some good fortune.",
    "date_created": "2020-08-18T11:43:08.767002Z",
    "date_modified": "2020-08-18T11:43:08.765903Z"
}
```
<!--Self describing APIs
The browsable API that REST framework provides makes it possible for your API to be entirely self describing. The documentation for each API endpoint can be provided simply by visiting the URL in your browser.-->

### Authentication & Permissions

The Django’s built-in authentication system is great. For the most part we can use it out-of-the-box, saving a lot of development and testing effort. But we found ourselves needing to do some fine adjustment to fit our Web application i.e. storing a bit more data related to our User model.

#### Token Authentication
This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.
 
A user enters the name and password into the client, the client then sends these credentials to the server, the server authenticates the client credentials (i.e. username and password) and then it generates and returns an access token. This access token is used to identify a user and assure authenticity of the user.  
```
POST /auth/
```
**Response**
```
{
    "token": "4397258009e0a7d5b2678cd064e7b351b800a0e2",
    "id": 1
}
```
#### Permissions

Permissions are run at the very start of the view, before any code within the view is executed. Therefore, a user must be both authenticated and authorised before the API can fulfil the user’s request unless a permission class which allows unrestricted access, regardless of if the request was authenticated or unauthenticated is explicitly used on a view.
 
Some requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; `GET`, `HEAD` or `OPTIONS`.

> Together with authentication and throttling, permissions determine whether a request should be granted or denied access. - [DRF documentation](https://www.django-rest-framework.org/api-guide/permissions/)

##### Object Level Permissions
123....

##### User
The user represents the user you are currently logged in for each API call.

## Useful Links

- [Monica API Documentation](https://www.monicahq.com/api/overview)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Adding Object Level Permissions](https://dragonprogrammer.com/object-level-permissions-drf/)
- [DRF File Upload](https://medium.com/@jxstanford/django-rest-framework-file-upload-e4bc8de669c0)

Inspired by [Monica](https://github.com/monicahq)
