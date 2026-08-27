import streamlit as st

# ============================================================
# 🎓 SKILLSWAP
# Student-to-Student Skill Exchange Platform
# ============================================================

st.set_page_config(
    page_title="SkillSwap",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# SAMPLE STUDENT DATA
# ============================================================

if "students" not in st.session_state:
    st.session_state.students = [
        {
            "name": "Aditi",
            "teach": "Canva",
            "learn": "Python",
            "level": "Beginner",
            "mode": "Online",
            "type": "Skill Exchange",
            "fee": "Free",
            "phone": "9876543210",
            "email": "aditi@example.com",
            "credits": 3
        },
        {
            "name": "Rahul",
            "teach": "Python",
            "learn": "Graphic Design",
            "level": "Intermediate",
            "mode": "Offline",
            "type": "Skill Exchange",
            "fee": "Free",
            "phone": "9876543211",
            "email": "rahul@example.com",
            "credits": 5
        },
        {
            "name": "Sneha",
            "teach": "German",
            "learn": "Photography",
            "level": "Intermediate",
            "mode": "Online",
            "type": "Teach for Free",
            "fee": "Free",
            "phone": "9876543212",
            "email": "sneha@example.com",
            "credits": 4
        },
        {
            "name": "Arjun",
            "teach": "Photography",
            "learn": "Video Editing",
            "level": "Advanced",
            "mode": "Offline",
            "type": "Paid Mentoring",
            "fee": "₹100/session",
            "phone": "9876543213",
            "email": "arjun@example.com",
            "credits": 7
        },
        {
            "name": "Meera",
            "teach": "Excel",
            "learn": "Python",
            "level": "Beginner",
            "mode": "Online",
            "type": "Teach for Free",
            "fee": "Free",
            "phone": "9876543214",
            "email": "meera@example.com",
            "credits": 2
        }
    ]

if "connection_requests" not in st.session_state:
    st.session_state.connection_requests = []


# ============================================================
# HEADER
# ============================================================

st.title("🎓 SkillSwap")
st.subheader("Learn. Teach. Connect.")
st.write(
    "A student-to-student platform for exchanging skills, "
    "finding learning partners, and connecting with peers."
)

st.divider()


# ============================================================
# NAVIGATION
# ============================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Home",
    "➕ Add Your Skill",
    "🔄 Find Skill Swap",
    "🤝 Request to Connect",
    "👥 Browse Students",
    "⭐ Skill Credits"
])


# ============================================================
# HOME
# ============================================================

with tab1:

    st.header("Welcome to SkillSwap! 👋")

    st.markdown("""
### 🔄 Skill Exchange
Teach one skill and learn another.

**No fee required.**

### 🆓 Teach for Free
Share your knowledge with other students.

### 💰 Paid Mentoring
Advanced students can offer paid mentoring sessions.

---

### 🌟 Why SkillSwap?

📚 **Peer Learning**  
🤝 **Student Connections**  
⭐ **Motivation & Accountability**  
🌱 **Explore New Skills**

---

> **"The internet helps you learn a skill.
> SkillSwap helps you find someone to learn it with."**
""")


# ============================================================
# ADD YOUR SKILL
# ============================================================

with tab2:

    st.header("Create Your Skill Profile")

    st.write(
        "Tell other students what you can teach "
        "and what you want to learn."
    )

    name = st.text_input(
        "👤 Your Name",
        placeholder="Enter your name"
    )

    teach = st.text_input(
        "🟢 Skill You Can Teach",
        placeholder="Example: Python"
    )

    learn = st.text_input(
        "🔵 Skill You Want to Learn",
        placeholder="Example: Canva"
    )

    level = st.selectbox(
        "📊 Skill Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    mode = st.selectbox(
        "🌐 Preferred Mode",
        ["Online", "Offline", "Both"]
    )

    participation = st.selectbox(
        "💡 Participation Type",
        [
            "Skill Exchange",
            "Teach for Free",
            "Paid Mentoring"
        ]
    )

    fee = ""

    if participation == "Paid Mentoring":
        fee = st.text_input(
            "💰 Fee",
            placeholder="Example: ₹100/session"
        )

    phone = st.text_input(
        "📱 Phone Number",
        placeholder="Enter your phone number"
    )

    email = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    if st.button("➕ Create Profile", type="primary"):

        if not name or not teach or not phone or not email:

            st.warning(
                "Please enter your name, skill, phone number and email."
            )

        else:

            if participation in ["Skill Exchange", "Teach for Free"]:
                final_fee = "Free"
            else:
                final_fee = fee if fee else "Fee not specified"

            new_student = {
                "name": name,
                "teach": teach,
                "learn": learn if learn else "None",
                "level": level,
                "mode": mode,
                "type": participation,
                "fee": final_fee,
                "phone": phone,
                "email": email,
                "credits": 0
            }

            st.session_state.students.append(new_student)

            st.success("Profile created successfully! 🎉")

            st.markdown(f"""
### 👤 {name}

🟢 **Can Teach:** {teach}

🔵 **Wants to Learn:** {learn if learn else "Not specified"}

📊 **Level:** {level}

🌐 **Mode:** {mode}

💡 **Participation:** {participation}

💰 **Fee:** {final_fee}

---

Your profile is now available to other students.

🔒 Contact details are shown when a student requests a connection.
""")


# ============================================================
# FIND SKILL SWAP
# ============================================================

with tab3:

    st.header("🔍 Find Your Learning Partner")

    st.write(
        "Enter the skill you can teach and the skill you want to learn."
    )

    my_skill = st.text_input(
        "🟢 I Can Teach...",
        placeholder="Example: German"
    )

    wanted_skill = st.text_input(
        "🔵 I Want to Learn...",
        placeholder="Example: Python"
    )

    if st.button("🔍 Find My Match", type="primary"):

        if not wanted_skill:

            st.warning("Please enter a skill you want to learn.")

        else:

            wanted = wanted_skill.lower().strip()

            my = my_skill.lower().strip() if my_skill else ""

            perfect_matches = []
            other_matches = []

            for index, student in enumerate(st.session_state.students):

                teaches = student["teach"].lower()
                wants = student["learn"].lower()

                if wanted in teaches:

                    if my and my in wants:
                        perfect_matches.append((index, student))
                    else:
                        other_matches.append((index, student))

            if perfect_matches:

                st.subheader("🔥 Perfect Skill Swaps")

                st.write(
                    "These students can teach what you want "
                    "and want to learn what you can teach."
                )

                for index, student in perfect_matches:

                    with st.container(border=True):

                        st.markdown(
                            f"### 👤 {student['name']}"
                        )

                        st.write(
                            f"🔄 **Perfect Skill Swap**"
                        )

                        st.write(
                            f"🟢 Teaches: **{student['teach']}**"
                        )

                        st.write(
                            f"🔵 Wants to Learn: **{student['learn']}**"
                        )

                        st.write(
                            f"📊 Level: {student['level']}"
                        )

                        st.write(
                            f"🌐 Mode: {student['mode']}"
                        )

                        st.write(
                            f"💰 Fee: {student['fee']}"
                        )

                        st.code(
                            f"Student ID: {index}"
                        )

            if other_matches:

                st.subheader("🟡 Other Students Who Can Help")

                for index, student in other_matches:

                    with st.container(border=True):

                        st.markdown(
                            f"### 👤 {student['name']}"
                        )

                        st.write(
                            f"🟢 Teaches: **{student['teach']}**"
                        )

                        st.write(
                            f"🔵 Wants to Learn: **{student['learn']}**"
                        )

                        st.write(
                            f"📊 Level: {student['level']}"
                        )

                        st.write(
                            f"🌐 Mode: {student['mode']}"
                        )

                        st.write(
                            f"💰 Fee: {student['fee']}"
                        )

                        st.code(
                            f"Student ID: {index}"
                        )

            if not perfect_matches and not other_matches:

                st.info(
                    f"No student is currently teaching "
                    f"**{wanted_skill.title()}**."
                )


# ============================================================
# REQUEST CONNECTION
# ============================================================

with tab4:

    st.header("🤝 Connect With a Student")

    st.write(
        "Enter the Student ID shown in the search results."
    )

    student_id = st.number_input(
        "Student ID",
        min_value=0,
        step=1
    )

    if st.button("🤝 REQUEST TO CONNECT", type="primary"):

        if student_id >= len(st.session_state.students):

            st.error("Student ID not found.")

        else:

            student = st.session_state.students[student_id]

            st.session_state.connection_requests.append(
                student["name"]
            )

            st.success(
                f"Connection request sent to {student['name']}!"
            )

            st.subheader("📩 Contact Details")

            st.markdown(
                f"📧 **Email:** [{student['email']}](mailto:{student['email']})"
            )

            st.markdown(
                f"📱 **Phone:** [{student['phone']}](tel:{student['phone']})"
            )

            st.write(
                "You can now contact the student and arrange a learning session."
            )

            st.caption(
                "🔒 In a real application, contact details would "
                "only become visible after the other student accepts."
            )


# ============================================================
# BROWSE STUDENTS
# ============================================================

with tab5:

    st.header("👥 Students on SkillSwap")

    if st.button("🔄 Refresh Students"):

        st.rerun()

    for index, student in enumerate(st.session_state.students):

        with st.container(border=True):

            st.markdown(
                f"### 👤 {student['name']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"🟢 **Can Teach:** {student['teach']}"
                )

                st.write(
                    f"🔵 **Wants to Learn:** {student['learn']}"
                )

                st.write(
                    f"📊 **Level:** {student['level']}"
                )

                st.write(
                    f"🌐 **Mode:** {student['mode']}"
                )

            with col2:

                st.write(
                    f"💡 **Type:** {student['type']}"
                )

                st.write(
                    f"💰 **Fee:** {student['fee']}"
                )

                st.write(
                    f"⭐ **Skill Credits:** {student['credits']}"
                )

                st.code(
                    f"Student ID: {index}"
                )

            st.caption("🔒 Contact details hidden")


# ============================================================
# SKILL CREDITS
# ============================================================

with tab6:

    st.header("⭐ Skill Credits")

    st.write(
        "Skill Credits encourage students to share "
        "their knowledge."
    )

    st.markdown("""
### How it works:

🎓 Teach another student

↓

⭐ Earn Skill Credits

↓

📚 Use credits to learn from another student

---

### Example

You teach **Canva**

↓

⭐ **+1 Skill Credit**

↓

Use the credit to request help with **Python**

---

**Skill Credits are not money.**

They represent participation in the SkillSwap community.
""")
