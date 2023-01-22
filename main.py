import datetime
import requests
import streamlit as st


def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}


def main():
    st.title("Mag Mutual UI")
    session = requests.Session()

    url = 'https://www.streamlit.io/'
    if st.button('Clear'):
        st.write('')
    with st.form("Get All Users"):
        submitted = st.form_submit_button('Get All Users')
        if submitted:
            data = fetch(session, f"http://localhost:10000/users")
            if data:
                st.table(data['users'])
            else:
                st.error("Error")
    with st.form("Get Users by Date"):
        st.title("GetUsers by Date")
        fromDate = st.date_input("When\'s fromDate birthday", datetime.date(2019, 7, 6))
        toDate = st.date_input("When\'s toDate birthday", datetime.date(2019, 7, 6))
        st.write('fromDate  & toDate:', fromDate, toDate)
        submitted = st.form_submit_button("Submit")
        if submitted:
           st.write("Result")
           data = fetch(session, f"http://localhost:10000/users/byDate?fromDate={fromDate}&toDate={toDate}")
           if data:
              st.table(data['users'])
           else:
              st.error("Error")
    st.button('Get Users by ID')
    st.button('Get Users by Profession')


if __name__ == '__main__':
    main()
