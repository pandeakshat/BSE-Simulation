import streamlit as st

def main():
    st.title("Under Construction")
    st.write("This page is currently under construction.")

    # Add links to other Streamlit pages
    st.markdown("## Navigation")
    page = st.selectbox("Go to", ["Home", "About", "Contact"])
    if page == "Home":
        st.write("Go to the [Home](http://localhost:8501/) page.")
    elif page == "About":
        st.write("Go to the [About](http://localhost:8501/about) page.")
    elif page == "Contact":
        st.write("Go to the [Contact](http://localhost:8501/contact) page.")

if __name__ == "__main__":
    main()
