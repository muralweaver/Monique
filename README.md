![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Panda_icon.svg/240px-Panda_icon.svg.png)

# Monique [Work in progress]

A Personal Relationship Management tool

...


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
    "account": 1,
    "title": "Just another winter",
    "body": "Christmas has just past and tomorrow is New Years' Eve. We had a quiet Christmas, actually it got messed up. My father-in-law decided to act like an ass. So I had a bad start to the holidays. Now I find I have a reacurring bladder infection. I am now on my second round of antibiotics. I am still waiting for a break in my writing career. I was sent an email to write articles so I decided to go for it. The only problem is the pay is not great, but at this point I will do it. I am still waiting for a reply. As for New Year's I don't know what we are doing. I just hope this year brings some good fortune.",
    "date_created": "2020-08-18T11:43:08.767002Z",
    "date_modified": "2020-08-18T11:43:08.765903Z"
}
```

### Authentication & Permissions
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

##### User
The user represents the user you are currently logged in for each API call.

## Useful Links

- [Monica API Documentation](https://www.monicahq.com/api/overview)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [DRF File Upload](https://medium.com/@jxstanford/django-rest-framework-file-upload-e4bc8de669c0)

Inspired by [Monica](https://github.com/monicahq)
