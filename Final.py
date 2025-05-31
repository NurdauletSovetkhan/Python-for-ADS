import json
import random
import streamlit as st
from quiz_helper import load_questions, get_random_questions
from helper import (
    show_recursion,
    show_asymptotic,
    show_arrays,
    show_linked_lists,
    show_stack_queue,
    show_heap,
    show_hash_tables_trees,
    show_sorting,
    show_searching,
    show_graphs,
)

# Set up Streamlit page configuration
st.set_page_config(page_title="ADS Helper", layout="wide")

# Create three main tabs for the app
tab1, tab2, tab3 = st.tabs(["📚 Conspects", "📝 Past Quizzes", "🎮 Take a Quiz"])

# ----------------- TAB 1: Conspects (Notes & Code Samples) -----------------
with tab1:
    st.title("📚 ADS Conspects")

    # Sidebar for topic and language selection
    st.sidebar.title("🧭 Navigation")
    topic = st.sidebar.radio("📘 Choose Topic", [
        "Show Everything",
        "1. Recursion",
        "2. Asymptotic Analysis",
        "3. Arrays",
        "4. Linked Lists",
        "5. Stack & Queue",
        "6. Heap",
        "7. Hash Tables & Trees",
        "8. Sorting",
        "9. Searching",
        "10. Graphs & Traversals",
    ])

    language = st.sidebar.selectbox("💻 Code Language", ["Python", "C++", "Java"])

    # Show selected topic(s) in the chosen language
    if topic == "Show Everything":
        show_recursion(language)
        show_asymptotic(language)
        show_arrays(language)
        show_linked_lists(language)
        show_stack_queue(language)
        show_heap(language)
        show_hash_tables_trees(language)
        show_sorting(language)
        show_searching(language)
        show_graphs(language)
    elif topic == "1. Recursion":
        show_recursion(language)
    elif topic == "2. Asymptotic Analysis":
        show_asymptotic(language)
    elif topic == "3. Arrays":
        show_arrays(language)
    elif topic == "4. Linked Lists":
        show_linked_lists(language)
    elif topic == "5. Stack & Queue":
        show_stack_queue(language)
    elif topic == "6. Heap":
        show_heap(language)
    elif topic == "7. Hash Tables & Trees":
        show_hash_tables_trees(language)
    elif topic == "8. Sorting":
        show_sorting(language)
    elif topic == "9. Searching":
        show_searching(language)
    elif topic == "10. Graphs & Traversals":
        show_graphs(language)

# ----------------- TAB 2: Past Quizzes -----------------
with tab2:
    st.title("📝 Past Quizzes")

    # Hide sidebar for cleaner look in this tab

    # Load quiz questions from JSON files
    with open("mid.json") as f:
        mid_data = json.load(f)
    with open("end.json") as f:
        end_data = json.load(f)

    # Choose which quiz to display
    section = st.radio("📂 Select Quiz", ["Midterm Questions", "Final Questions"], horizontal=True)
    shuffle = st.checkbox("🔀 Shuffle Questions", value=True)
    questions = mid_data if section == "Midterm Questions" else end_data

    # Shuffle questions if selected
    if shuffle:
        random.shuffle(questions)

    # Display each question with options and expandable answer
    for i, q in enumerate(questions, 1):
        st.markdown(f"### ❓ Q{i}: {q['question']}")
        for idx, opt in enumerate(q["options"], 1):
            st.write(f"{idx}. {opt}")
        with st.expander("🔎 Show Answer"):
            st.success(f"✅ Correct Answer: **{q['answer']}**")
        st.markdown("---")

# ----------------- TAB 3: Take a Quiz -----------------
with tab3:

    # Load quiz questions from JSON files
    with open("mid.json") as f:
        mid_questions = json.load(f)
    with open("end.json") as f:
        end_questions = json.load(f)

    st.title("🎮 Take a Quiz")
    
    # Reset all session state if requested
    if st.button("🔄 Try Again (Reset All)"):
        for key in ["submitted", "quiz_answers", "quiz", "shuffled_questions", "num_questions_prev"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()  # полностью перезапускает таб


    # Select quiz source and number of questions
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("📚 Question Source", ["Midterm", "Final", "Both"])
    with col2:
        num_questions = st.selectbox("🔢 Number of Questions", [5, 10, 15, 20, 25, 30, 35, 40])

    # Reset quiz state if number of questions changes
    if "num_questions_prev" not in st.session_state or st.session_state.num_questions_prev != num_questions:
        st.session_state.num_questions_prev = num_questions
        st.session_state.submitted = False
        st.session_state.quiz_answers = [None] * num_questions
        # Select questions based on source
        if source == "Midterm":
            questions = mid_questions
        elif source == "Final":
            questions = end_questions
        else:
            questions = mid_questions + end_questions
        shuffled = questions.copy()
        random.shuffle(shuffled)
        st.session_state.shuffled_questions = shuffled
        st.session_state.quiz = shuffled[:num_questions]

    # Initialize quiz state if not already set
    if "quiz" not in st.session_state:
        if source == "Midterm":
            questions = mid_questions
        elif source == "Final":
            questions = end_questions
        else:
            questions = mid_questions + end_questions
        shuffled = questions.copy()
        random.shuffle(shuffled)
        st.session_state.shuffled_questions = shuffled
        st.session_state.quiz = shuffled[:num_questions]
        st.session_state.quiz_answers = [None] * num_questions
        st.session_state.submitted = False
        st.session_state.num_questions_prev = num_questions

    quiz = st.session_state.quiz

    # Ensure quiz answers and submission state are initialized
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = [None] * num_questions
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # Display each quiz question with answer options
    for idx, q in enumerate(quiz):
        container = st.container()
        with container:
            st.subheader(f"{idx + 1}. {q['question']}")
            selected = st.radio(
                "Select an answer:",
                q["options"],
                index=q["options"].index(st.session_state.quiz_answers[idx]) if st.session_state.quiz_answers[idx] in q["options"] else 0,
                key=f"q_{idx}",
                label_visibility="collapsed",
            )
            st.session_state.quiz_answers[idx] = selected
            st.markdown("---")

    # Show submit or try again button depending on state
    if not st.session_state.submitted:
        if st.button("✅ Submit Quiz"):
            st.session_state.submitted = True
    else:
        if st.button("🔄 Try Again"):
            st.session_state.submitted = False
            st.session_state.quiz_answers = [None] * num_questions
            # Re-shuffle questions for a new quiz
            if source == "Midterm":
                questions = mid_questions
            elif source == "Final":
                questions = end_questions
            else:
                questions = mid_questions + end_questions
            shuffled = questions.copy()
            random.shuffle(shuffled)
            st.session_state.shuffled_questions = shuffled
            st.session_state.quiz = shuffled[:num_questions]

    # Show quiz results after submission
    if st.session_state.submitted:
        st.header("🎯 Results")
        correct = 0
        wrong_list = []

        # Check each answer and collect incorrect ones
        for idx, q in enumerate(quiz):
            if st.session_state.quiz_answers[idx] == q["answer"]:
                correct += 1
            else:
                wrong_list.append((idx + 1, q))

        percent = (correct / num_questions) * 100
        st.success(f"✅ You got {correct} out of {num_questions} correct! ({percent:.2f}%)")

        # Show incorrect answers with correct ones for review
        if wrong_list:
            st.warning("❌ Incorrect Answers:")
            for i, q in wrong_list:
                st.markdown(f"""
                **{i}. {q['question']}**  
                Your answer: `{st.session_state.quiz_answers[i-1]}`  
                Correct answer: ✅ `{q['answer']}`  
                """)