import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)

st.title("My ToDo App")
# st.subheader("This is my ToDo app.")
# st.write("This app is to increase your productivity")\

for index, todo in enumerate(todos):
    todo = todo.strip()
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(label = "Enter a ToDo", placeholder = "Add new ToDo...",
              on_change= add_todo, key= 'new_todo')