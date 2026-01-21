import streamlit as st
from markov import generate_text, build_markov_chains, get_random_starter_words

st.title("Markov Chains with Strings aka Inspirational Quote Generator")

if "random_starter_words" not in st.session_state:
    st.session_state.random_starter_words = get_random_starter_words()

if "word_chains" not in st.session_state:
    st.session_state.word_chains = build_markov_chains()

st.write(st.session_state.random_starter_words)

result = st.text_input(
    label="Enter a starter word from the options above",
)
num_words = st.number_input(label="Num. Words to Generate", max_value=20)

if st.button("Generate Text"):
    st.write(generate_text(st.session_state.word_chains, start_word=result, length=num_words))