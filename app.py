import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog
from src.database.db import get_teacher_by_id, get_student_by_id


def _hydrate_session_from_url():
    """Restore login state after a page refresh.

    A successful login stores ``?u=<role>:<id>`` in the URL. On every render
    we re-read it and re-fetch the user from Supabase if the in-memory
    session was wiped (e.g. browser refresh, link share).
    """
    if st.session_state.get('teacher_data') or st.session_state.get('student_data'):
        return

    raw = st.query_params.get('u')
    if not raw or ':' not in raw:
        return

    role, uid = raw.split(':', 1)
    try:
        uid = int(uid)
    except ValueError:
        return

    if role == 't':
        teacher = get_teacher_by_id(uid)
        if teacher:
            st.session_state['login_type'] = 'teacher'
            st.session_state['teacher_data'] = teacher
            st.session_state['is_logged_in'] = True
            st.session_state['user_role'] = 'teacher'
    elif role == 's':
        student = get_student_by_id(uid)
        if student:
            st.session_state['login_type'] = 'student'
            st.session_state['student_data'] = student
            st.session_state['is_logged_in'] = True
            st.session_state['user_role'] = 'student'


def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    _hydrate_session_from_url()

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)


main()
