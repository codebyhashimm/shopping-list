import streamlit as st
import json
import os

FILE_NAME = "shopping_list.json"

# ---------- LOAD DATA ----------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {"shopping_list": [], "checked_items": []}

# ---------- SAVE DATA ----------
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump({
            "shopping_list": st.session_state.shopping_list,
            "checked_items": list(st.session_state.checked_items)
        }, f)

# ---------- INIT SESSION ----------
data = load_data()

if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = data["shopping_list"]

if "checked_items" not in st.session_state:
    st.session_state.checked_items = set(data["checked_items"])

# ---------- UI ----------
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
                save_data()
                st.success("item added")

# DELETE ITEM
elif menu == "Delete item":
    with st.form("delete_form", clear_on_submit=True):
        user_item = st.text_input("Enter item to delete")
        submitted = st.form_submit_button("Delete")

        if submitted:
            if user_item in st.session_state.shopping_list:
                st.session_state.shopping_list.remove(user_item)
                st.session_state.checked_items.discard(user_item)
                save_data()
                st.error("item removed")
            else:
                st.warning("Item not found")

# SHOW LIST
elif menu == "Show list":
    if len(st.session_state.shopping_list) == 0:
        st.info("Your list is empty")
    else:
        st.subheader("Your Shopping List:")

        for item in st.session_state.shopping_list:
            checked = item in st.session_state.checked_items

            new_value = st.checkbox(item, value=checked, key=item)

            if new_value:
                st.session_state.checked_items.add(item)
            else:
                st.session_state.checked_items.discard(item)

        # Save checkbox changes
        save_data()
