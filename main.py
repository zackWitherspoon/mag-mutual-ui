import datetime
import logging as log
import requests
import streamlit as st


def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}


def fetch_post(session, url, body):
    try:
        result = session.post(url, json=body)
        print(result)
        return result.json(), result.status_code
    except Exception as err:
        print('ERROR!!!!!')
        print(err)
        return st.error(err), 400


def main():
    st.title("Mag Mutual UI")
    session = requests.Session()

    url = 'http://localhost:10000/users'
    if st.button('Clear'):
        st.write('')
    with st.form("Get All Users"):
        st.title("Get All Users")
        submitted = st.form_submit_button('Get All Users')
        if submitted:
            data = fetch(session, f"{url}")
            if data:
                st.table(data['users'])
            else:
                st.error("Error")
    with st.form("Get Users by Date"):
        st.title("Get Users by Date")
        fromDate = st.date_input("When\'s fromDate birthday", datetime.date(2022, 2, 16))
        toDate = st.date_input("When\'s toDate birthday", datetime.date(2022, 2, 25))
        submitted = st.form_submit_button("Submit")
        if submitted:
            data = fetch(session, f"{url}/byDate?fromDate={fromDate}&toDate={toDate}")
            if data:
                st.table(data['users'])
            else:
                st.error(data.reason)
    with st.form("Get Users by Id"):
        st.title("Get Users by Id")
        user_id = st.number_input('Insert a number', value=100)
        submitted = st.form_submit_button("Submit")
        if submitted:
            data = fetch(session, f"{url}/id/{user_id}")
            if data:
                st.table(data['users'])
            else:
                st.error(data.reason)
    with st.form("Get Users by Profession"):
        st.title("Get Users by Profession")
        profession = st.text_input('Insert a number', "firefighter")
        submitted = st.form_submit_button("Submit")
        if submitted:
            json_data = {"profession": profession}
            print(json_data)
            data, status_code = fetch_post(session, f"{url}/byProfession", json_data)
            if data:
                st.table(data['users'])
            else:
                st.error(status_code)


if __name__ == '__main__':
    main()
