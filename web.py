import streamlit as st
import functions 
import time

now = time.strftime("%b %d, %Y %I:%M %p")

todos = functions.read_todos()

def add_todos():
    todo = st.session_state["new_todo"].title() + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This app is to increase your productivity")
st.write(now)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        

st.text_input(label="", placeholder="Add new todo.....",
              on_change=add_todos, key="new_todo")


