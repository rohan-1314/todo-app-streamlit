import streamlit as st
import functions as fn

todos = fn.get_todo()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    fn.write_todo(todos)

def complete():
    if st.session_state[unique_val] == True:
        fn.write_todo(todos)


st.title('My Todo App')

st.subheader("This is Rohan's todo app")
st.write('This app increases your productivity.')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new todo...', on_change=add_todo, key='new_todo')

