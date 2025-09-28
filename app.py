import streamlit as st


if "names" not in st.session_state:
    st.session_state.names = []

st.title("📋 Names list")


st.subheader("List:")
for i, name in enumerate(st.session_state.names, start=1):
    st.write(f"{i}. {name}")


st.subheader("Add a new name")
new_name = st.text_input("new name:", key="add_name")
if st.button("Add"):
    if new_name:
        st.session_state.names.append(new_name)
        st.success(f"Added: {new_name}")
        st.rerun()  
    else:
        st.warning("Name can't be empty.")


if st.session_state.names:
    st.subheader("Remove Name")
    remove_name = st.selectbox("Choose name to delete:", st.session_state.names, key="remove_name")
    if st.button("Delete"):
        st.session_state.names.remove(remove_name)
        st.success(f"Deleted: {remove_name}")
        st.rerun()  


if st.session_state.names:
    st.subheader("Change name")
    selected_name = st.selectbox("Choose name to change:", st.session_state.names, key="change_name")
    new_name_value = st.text_input("Add name to change:", key="new_name_value")
    if st.button("Change"):
        if new_name_value:
            index = st.session_state.names.index(selected_name)
            st.session_state.names[index] = new_name_value
            st.success(f"'{selected_name}' → '{new_name_value}' changed")
            st.rerun()  
        else:
            st.warning("New name can't be empty")
