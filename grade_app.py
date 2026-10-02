import streamlit as st
st.title("Student Grade Manager")
if "students" not in st.session_state:
    st.session_state.students = []
name = st.text_input("Student Name")
mark = st.number_input("Mark", min_value=0.0, max_value=100.0)
if st.button("Add Student"):
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"
    st.write("Grade:", grade)
    st.session_state.students.append(
    {"name": name, "mark": mark, "grade": grade}
)
    st.table(st.session_state.students)
    # Get marks from all students
marks = [student["mark"] for student in st.session_state.students]

# Calculate class average
average = sum(marks) / len(marks) if marks else 0

# Find the highest mark
highest = max(marks) if marks else 0

# Find the lowest mark
lowest = min(marks) if marks else 0

# Display average
st.metric("Average", round(average, 1))

# Display highest mark
st.metric("Highest", highest)

# Display lowest mark
st.metric("Lowest", lowest)