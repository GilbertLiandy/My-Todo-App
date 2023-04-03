import streamlit as st
import functions

todos = functions.getTodos()

def addTodo():
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    functions.writeTodos(todos)

todos = functions.getTodos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo",
              placeholder="Add new todo...",
              on_change=addTodo, key='newTodo')
