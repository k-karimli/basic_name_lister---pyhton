import streamlit as st

if "names" not in st.session_state:
    st.session_state.names = []

st.title("📋 Adlar Siyahısı")

st.subheader("Siyahı")
for i, name in enumerate(st.session_state.names, start=1):
    st.write(f"{i}. {name}")

st.subheader("Yeni ad əlavə et")
new_name = st.text_input("Əlavə etmək istədiyiniz adı yazın:")
if st.button("Əlavə et") and new_name:
    st.session_state.names.append(new_name)
    st.experimental_rerun()

st.subheader("Ad sil")
remove_index = st.number_input(
    "Silinməli adın sıra nömrəsini daxil edin:",
    min_value=1,
    max_value=len(st.session_state.names) if st.session_state.names else 1,
    step=1,
    format="%d"
)
if st.button("Sil") and st.session_state.names:
    del st.session_state.names[remove_index - 1]
    st.experimental_rerun()

st.subheader("Ad dəyiş")
change_index = st.number_input(
    "Dəyişiləcək adın sıra nömrəsini daxil edin:",
    min_value=1,
    max_value=len(st.session_state.names) if st.session_state.names else 1,
    step=1,
    format="%d"
)
new_name_change = st.text_input("Yeni adı daxil edin:")
if st.button("Dəyiş") and new_name_change:
    st.session_state.names[change_index - 1] = new_name_change
    st.experimental_rerun()
