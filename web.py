import streamlit as st
import functions as fns

todos = fns.read_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    fns.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        fns.write_todos(todos )
        del st.session_state[item]
        st._rerun()

st.text_input(label="Add Todo:",
              label_visibility='hidden',
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")

