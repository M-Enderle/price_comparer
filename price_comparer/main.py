import streamlit as st
from price_comparer import dm

def main():
    st.title("Price Comparer")

    cols = st.columns((4,1,1))
    cols[0].text_input("Search for an Item", label_visibility="collapsed", placeholder="Search for an item")
    cols[1].selectbox("Store", ["DM"], label_visibility="collapsed")
    cols[2].button("Search")



if __name__ == "__main__":
    main()