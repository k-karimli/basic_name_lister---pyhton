import streamlit as st


if "names" not in st.session_state:
    st.session_state.names = []

st.title("📋 Adlar Siyahısı")


st.subheader("Siyahı:")
for i, name in enumerate(st.session_state.names, start=1):
    st.write(f"{i}. {name}")


st.subheader("Ad əlavə et")
new_name = st.text_input("Əlavə etmək istədiyiniz adı yazın:", key="add_name")
if st.button("Əlavə et"):
    if new_name:
        st.session_state.names.append(new_name)
        st.success(f"Ad əlavə olundu: {new_name}")
        st.experimental_rerun()
    else:
        st.warning("Ad boş ola bilməz.")


if st.session_state.names:
    st.subheader("Ad sil")
    remove_name = st.selectbox("Silinəcək adı seçin:", st.session_state.names, key="remove_name")
    if st.button("Sil"):
        st.session_state.names.remove(remove_name)
        st.success(f"Ad silindi: {remove_name}")
        st.experimental_rerun()


if st.session_state.names:
    st.subheader("Ad dəyiş")
    selected_name = st.selectbox("Dəyişiləcək adı seçin:", st.session_state.names, key="change_name")
    new_name_value = st.text_input("Yeni adı daxil edin:", key="new_name_value")
    if st.button("Dəyiş"):
        if new_name_value:
            index = st.session_state.names.index(selected_name)
            st.session_state.names[index] = new_name_value
            st.success(f"'{selected_name}' → '{new_name_value}' dəyişdirildi.")
            st.experimental_rerun()
        else:
            st.warning("Yeni ad boş ola bilməz.")
