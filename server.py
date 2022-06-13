from flask import Flask, render_template ,request, redirect
app = Flask(__name__)

# some code for the routes andd endpoints
list_todos = [{
    "todo": "learn Templates in flask",
    "status": "in progres",
},
    {
    "todo": "learn Objests Orientation Programing",
    "status": "complete"
},
    {
    "todo": "learn Deployment",
    "status": "cancel"
}]

app.route("/")
@app.route("/todos")
def get_all_todos():
    return render_template("index.html", first_name="Lenddy", list_todos=list_todos)


@app.route("/todo/new")
def display_create_todo():
    return render_template("todoForm.html")

@app.route("/todo/new", methods = ["POST"])
def create_todo():
    # requeste is a objetc and form is a attribute
    new_todo ={
        # create a dictionary  and put request.form follow by the [ " " ] and them put the argument that you want to ruquest  
        "todo": request.form["todo"],
        "status": request.form["status"]
    } 
    # after we are finish with the dictionary we have to append() the list_todos to the new_list
    list_todos.append(new_todo)
    # then return redirect (  " existing raute that we want "  )
    return redirect("/todos")




if __name__ == "__main__":
    app.run(debug=True)










    '''
Get = read and display
URL of the route to display all: the name of the list or dictionary that we are about to diaply 
example: "/ todos"
example: "/ users"
funtion: get_all_todos()
URL of the route display one: the name of teh list in singular  that we are sbout to display follow by the id
example: "/todo/<int:id>"
example: "/users/<int:id> "
untion:get_todo_by_id(id)
post = create
funtion: create_todo()
URL of the route to create something new the name of the list in singular the we about to create follow by the keyword new
example: "/todo/new"
example: "/user/new"
put = update
the URL of the route to update someting existing: the name of the list in singular that we are about to update, follow by the id followed by the keyword /update or edit
funtion: funtion: update_todo_user_by_id
example : "/todo/<int:id/update>"
example: "/usere <int:id>/update"
funtion: update_todo_by_id(id)
delete = remove
the URL of the route to delete someting existing: the name of the list in singular that we are about to delete, follow by the id followed by the keyword /delete or remove
example : "/todo/<int:id/delete>"
example: "/usere <int:id>/remove"
funtion: delete_todo_by_id(id)
'''