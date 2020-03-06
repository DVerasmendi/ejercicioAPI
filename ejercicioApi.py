
import requests, json, getpass

apiURL="http://ljavierrodriguez.pythonanywhere.com"
urlLogin=apiURL+"/api/login/"
urlPosts=apiURL+"/api/posts/"
urlRegister=apiURL+"/api/register/"
current_user={}
posts=[]

def getLogin(url, username,password):
    global current_user
    headers={
        'Content-Type':'application/json'
    }
    
    data= {
        "username":username,
        "password":password
    }
      
    req= requests.post(url=url, headers=headers, data=json.dumps(data))
    
    current_user=  req.json()
    print(current_user["username"], " ", current_user["token"])
    print(current_user["username"], " Usuario creado con exito!")

    
def getPosts(url):
    global current_user, posts
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + current_user["token"]
    }
    req = requests.get(url=url, headers=headers)
    print(req)
    posts = req.json()
    for x in posts:
        print()
        print(posts)
    
    
def savePost(url, title, content):
    global current_user, posts
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + current_user["token"]
    }
    data = {
        "title": title,
        "content": content,
        "user_id": current_user["id"]
    }
    req = requests.post(url=url, headers=headers, data=json.dumps(data))

    if req.status_code == 201:
        posts.append(req.json())
    else:
        print("Error de envio")
        
      

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    #initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Crear un usuario y loggear.
        2. Recibir los posts previos
        3. Crear un Post
        4. Exit
    """)
        response = input()
        if response == "4":
            stop = True
        ###################################
        elif response == "1":
            print("Ingresa tus datos")
            username = input()
            print("Ingresa tu contraseña")
            password=input()
            getLogin(urlRegister, username, password)
        ###################################
        elif response == "2":
            print("Recibiendo POST...")
            getPosts(urlPosts)
        ###################################
        elif response == "3":
            print("Ingresa tu Title")
            title=input()
            print("Ingresa tu Content")
            content=input()
            savePost(urlPosts, title, content)
        ###################################
        else:
            print("Invalid response, asking again...")