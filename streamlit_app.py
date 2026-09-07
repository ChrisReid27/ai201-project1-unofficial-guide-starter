"""Streamlit query interface for the Howard study-spots guide."""

from __future__ import annotations

import streamlit as st

from generate import answer_question


st.set_page_config(page_title="Howard Study Spots Guide", page_icon="📚")
st.title("Howard Study Spots Guide")
st.write("Ask about study locations on Howard's campus or around Washington, DC.")

question = st.text_area(
    "Question",
    placeholder="Where can I study quietly on a weekend afternoon?",
    height=100,
)
top_k = st.number_input(
    "Retrieved context chunks",
    min_value=1,
    max_value=10,
    value=5,
    step=1,
)

if st.button("Ask", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching the study guide..."):
            try:
                answer = answer_question(question, top_k=int(top_k))
            except (RuntimeError, ValueError) as error:
                st.error(str(error))
            else:
                st.markdown(answer)
