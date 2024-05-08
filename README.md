# STRIKE_EXAM

# Requirements :
Python3 --version 3.9.6
Django --version 4.1.13
Django Rest Framework  via pip install djangorestframework
Bootstrap, jQuery and Popper.js have already been linked via base.html sheet

# HOW TO USE
- Create user via sign up button
- If already created, please use the login button instead
- Creat your tasks : Title, Description, Level of Importance (urgent?, important?)  NOTE: Date to be completed could only be created & updated via API only but will appear on the Web once created 
- The task could be updated as well :: Title, Description and Level of Importance only
- Once the task is done, hit the complete button and the task will move from required tasks mode to complete tasks mode
- The task also could be deleted both in required tasks mode and complete tasks mode



# HOW TO USE API

# SIGN UP && RECIEVE TOKEN :
curl -X "POST" http://localhost/api/signup -H 'Content-Type: application/json' -d '{"username":"{your username}", "password":"{your password}"}'

# RECIEVE TOKEN via Login:
curl -X "POST" http://localhost/api/login -H 'Content-Type: application/json' -d '{"username":"{your username}", "password":"{your password}"}'

# CREATE task:
curl -X "POST"  http://localhost/api/tasks -H 'Authorization:Token {your token}' -H 'Content-Type: application/json' -d '{"title":"{your title}", "description":"{your description}", "datetobecomplete" : "{date yyyy-mm-dd}",  "urgent":{true or false}, "important":{true or false}' 

# VIEW current tasks:
curl -X "GET"  http://localhost/api/tasks -H 'Authorization:Token {your token}' 

# UPDATE task:
curl -X "PUT"  http://localhost/api/tasks/{task-ID} -H 'Authorization:Token {your token}' -H 'Content-Type: application/json' -d '{"title":"{your title}", "description":"{your description}", "datetobecomplete" : "{date yyyy-mm-dd}",  "urgent":{true or false}, "important":{true or false}'

# COMPLETE task:
curl -X "PUT"  http://localhost/api/tasks/{task-ID}/complete -H 'Authorization:Token {your token}'

# DELETE task:
curl -X "DELETE"  http://localhost/api/tasks/{task-ID} -H 'Authorization:Token {your token}'
