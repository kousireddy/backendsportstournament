# SportsTournaments APP ...
## Django REST FRAMEWORK
1.Clone Repository

   ```bash
   git clone https://github.com/kousireddy/backendsportstournament
   cd sportstournaments
   ```

2.Virtual Environment
```
python -m venv venv
source ./.venv/Scripts/activate
cd sportstournaments
```

## Features
- Models
   - sportstournaments
   - teams
   - players
   - matches
   - matchResults
- User Authentication
- RESTful API using Django REST Framework
- Token-based authentication

## Requirements
- Python 3.13.3
- Django 5.2.3
- djangorestframework 
- djangorestframework_simplejwt 
- mysql
- SQLite (default) / PostgreSQL (optional)


## Installation
```bash
py -m pip install Django
```
```bash
pip install djangorestframework
```
```bash
pip install mysqlclient
```
```bash
pip install djangorestframework-simplejwt
```
(OR)

## Requirements.txt
```
pip install -r requirements.txt
```
### MYSQL
- Create Database tounamentdatabase
```
py manage.py migrate
```

### Run Server
```
python manage.py runserver
```

## End Points

| Method | Endpoint           | Description             | Auth Required |
|--------|--------------------|-------------------------|---------------|
| POST   | /api/register/     | Register new user       | No            |
| POST   | /api/token/        | Login and get token     | No            |
| GET    | /api/tournament/   | List all tournaments         | Yes           |
| POST |   /api/tournament/  | create new tournament| Yes |
| GET    | /api/tournament/<id>/   | Retrieve a specific tournament| Yes           |
| PUT | /api/tournament/<id>/   |update a speacific tournament | Yes|
|DELETE  |/api/tournament/<id>|delete a speacific tournament|Yes|
| GET | /api/teams/           | List all Teams      | Yes |
| POST |   /api/teams/  | create new team| Yes |
| POST | /api/teams/<id>           |Retrieve specific team | Yes |
| PUT | /api/team/<id>/   |update a speacific team | Yes|
|DELETE  |/api/team/<id>|delete a speacific team|Yes|
| GET | /api/players/           | List all players     | Yes |
| POST |   /api/players/  | create new player| Yes |
| POST | /api/players/<id>           |Retrieve specific player| Yes |
| PUT | /api/players/<id>/   |update a speacific player | Yes|
|DELETE  |/api/players/<id>|delete a speacific player|Yes|
| GET | /api/matches/           | List all matches      | Yes |
| POST |   /api/matches/  | create new match| Yes |
| POST | /api/matches/<id>           |Retrieve specific match | Yes |
| PUT | /api/matches/<id>/   |update a speacific match | Yes|
|DELETE  |/api/matches/<id>|delete a speacific match|Yes|
| GET | /api/matchresults/           | List all matchresults      | Yes |
| POST |   /api/matchresults/  | create new matchresult| Yes |
| POST | /api/matchresults/<id>           |Retrieve specific matchresults | Yes |
| PUT | /api/matchresults/<id>/   |update a speacific matchresults | Yes|
|DELETE  |/api/matchresults/<id>|delete a speacific matchresults|Yes|




### Register
```http
POST /api/register/

Body : raw 
{
   "username" : <your_username>
   "password" : <insert_password>
   "email"    : <email> //optional
}
```

### token
```
POST /api/token/

- > copy access token
Authorization: Auth type Bearer Token <your_token>

```
### endpoints
```http
127.0.0.1:8000/api/<enter_end_point>
```

### Response
```
[
  {
    "id": ,
      
      //fields those are specified in model
  }
]
```

## Error Responses

| Status Code | Meaning             | Cause                                       |
|-------------|---------------------|---------------------------------------------|
| 400         | Bad Request          | Missing or invalid data in the request      |
| 401         | Unauthorized         | No token or invalid token provided          |
| 403         | Forbidden            | Authenticated but not allowed               |
| 404         | Not Found            | Resource not found                          |
| 405         | Method Not Allowed   | Method not allowed on this endpoint         |
| 500         | Internal Server Error| Server crashed or unhandled exception       |

## Success Responses

| Status Code | Meaning            | When It Occurs                              |
|-------------|--------------------|---------------------------------------------|
| 200         | OK                 | Successful GET or PUT request               |
| 201         | Created            | New resource created                        |
| 204         | No Content         | Successful DELETE request                   |
