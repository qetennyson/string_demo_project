import streamlit as st
from markov import generate_text, build_markov_chains, get_random_starter_words, get_next_word_probabilities

st.title("'INSPIRATIONAL' Quote Generator")

if "random_starter_words" not in st.session_state:
    st.session_state.random_starter_words = get_random_starter_words()

if "word_chains" not in st.session_state:
    st.session_state.word_chains = build_markov_chains()

st.write(st.session_state.random_starter_words)

user_word = st.text_input(
    label="Enter a starter word from the options above",
    placeholder="Leave blank for random"
)

use_frequency_weighting = st.sidebar.checkbox("Use Frequency Weighting")

show_probabilities = st.sidebar.checkbox("Display Step-by-step Probability")

enable_bias = st.sidebar.checkbox("Enable Bias")

if enable_bias:
    favor_letter = st.text_input(
        label="Enter a letter to bias towards or leave blank"
    )

quote_length = st.number_input(
    label="Num. Words to Generate", 
    max_value=25, 
    min_value=8, 
    value=8,
    )


if st.button("Generate Quote"):
    result = generate_text(
        st.session_state.word_chains, 
        start_word=user_word, 
        length=quote_length,
        favor_letter=favor_letter if favor_letter != "" else None,
        user_frequency_weighting=use_frequency_weighting,
        verbose=show_probabilities

        )

    if show_probabilities:
        st.success(result['text'])

        st.write("### How the Quote was Generated ")
        for i, step in enumerate(result['steps']):
            with st.expander(f"Step {i+1}: '{step['selected_word']}'"):
                st.write("**Possible next words:**")

                sorted_options = sorted(
                    step['next_options'].items(),
                    key=lambda x: x[1],
                    reverse=True
                )
                for word, prob in sorted_options:
                    st.write(f"  * {word}: {prob:.1f}%")
    else:
        st.success(result)
        
        

