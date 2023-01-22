import datetime
import logging as log
import requests
import streamlit as st

url = 'http://localhost:10000/users'


def fetch(session, url):
    try:
        result = session.get(url)
        if result.status_code == 200:
            return result.json(), None
        else:
            return {}, result.text
    except Exception as err:
        log.error(err)
        return {}, err


def fetch_post(session, url, body):
    try:
        result = session.post(url, json=body)
        print(result)
        return result.json(), None
    except Exception as err:
        log.error(err)
        return {}, err


def main():
    st.title("Mag Mutual UI")
    session = requests.Session()

    if st.button('Clear'):
        st.write('')
    with st.form("Get All Users"):
        st.title("Get All Users")
        submitted = st.form_submit_button('Get All Users')
        if submitted:
            data, err = fetch(session, f"{url}")
            if data:
                st.table(data['users'])
            else:
                st.error(err)
    with st.form("Get Users by Date"):
        st.title("Get Users by Date")
        from_date = st.date_input("When\'s fromDate birthday", datetime.date(2022, 2, 16))
        to_date = st.date_input("When\'s toDate birthday", datetime.date(2022, 2, 25))
        submitted = st.form_submit_button("Submit")
        if submitted:
            data, err = fetch(session, f"{url}/byDate?fromDate={from_date}&toDate={to_date}")
            if data:
                st.table(data['users'])
            else:
                st.error(err)
    with st.form("Get Users by Id"):
        st.title("Get Users by Id")
        user_id = st.number_input('Insert a number', value=100)
        submitted = st.form_submit_button("Submit")
        if submitted:
            data, err = fetch(session, f"{url}/id/{user_id}")
            if data:
                st.table(data['users'])
            else:
                st.error(err)
    with st.form("Get Users by Profession"):
        st.title("Get Users by Profession")
        profession = st.text_input('Insert a number', "firefighter")
        submitted = st.form_submit_button("Submit")
        if submitted:
            json_data = {"profession": profession}
            print(json_data)
            data, err = fetch_post(session, f"{url}/byProfession", json_data)
            if data:
                st.table(data['users'])
            else:
                st.error(err)


if __name__ == '__main__':
    main()
