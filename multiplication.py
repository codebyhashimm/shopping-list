import streamlit as st

# Session state
if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []

st.title("🛒 Shopping List Manager")

menu = st.radio("Choose an option:", ["Add item", "Delete item", "Show list"])

# ADD ITEM
if menu == "Add item":
    with st.form("add_form", clear_on_submit=True):
        user_item = st.text_input("Enter item to add")
        submitted = st.form_submit_button("Add")

        if submitted:
            if user_item.strip() == "":
                st.warning("Please enter something")
            elif user_item in st.session_state.shopping_list:
                st.warning("Item already in list")
            else:
                st.session_state.shopping_list.append(user_item)
                st.success(f"{user_item} added!")

# DELETE ITEM
elif menu == "Delete item":
    with st.form("delete_form", clear_on_submit=True):
        user_item = st.text_input("Enter item to delete")
        submitted = st.form_submit_button("Delete")

        if submitted:
            if user_item in st.session_state.shopping_list:
                st.session_state.shopping_list.remove(user_item)
                st.success(f"{user_item} removed!")
            else:
                st.warning("Item not found")

# SHOW LIST
elif menu == "Show list":
    with st.form("show_form"):
        submitted = st.form_submit_button("Show list")

        if submitted:
            if len(st.session_state.shopping_list) == 0:
                st.info("Your list is empty")
            else:
                st.subheader("Your Shopping List:")
                for i, item in enumerate(st.session_state.shopping_list, start=1):
                    st.write(f"{i}. {item}")