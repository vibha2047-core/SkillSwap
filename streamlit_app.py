import gradio as gr

# ============================================================
# 🎓 SKILLSWAP
# Student-to-Student Skill Exchange Platform
# ============================================================

# ------------------------------------------------------------
# SAMPLE STUDENT DATA
# ------------------------------------------------------------

students = [
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


# ============================================================
# CONNECTION REQUESTS
# ============================================================

connection_requests = []


# ============================================================
# HOME
# ============================================================

def home():

    return """
# 🎓 SkillSwap

### Learn. Teach. Connect.

**SkillSwap** is a student-to-student learning platform where
students can exchange knowledge, find learning partners,
or offer free/paid mentoring.

---

### 🔄 Skill Exchange

Teach one skill and learn another.

**No fee required.**

### 🆓 Teach for Free

Share your knowledge with other students.

### 💰 Paid Mentoring

Students with advanced skills can offer paid sessions.

---

### 🌟 Why SkillSwap?

📚 Peer Learning  
🤝 Student Connections  
⭐ Motivation & Accountability  
🌱 Explore New Skills

---

> **"The internet helps you learn a skill.
> SkillSwap helps you find someone to learn it with."**
"""


# ============================================================
# ADD SKILL
# ============================================================

def add_skill(
    name,
    teach,
    learn,
    level,
    mode,
    participation,
    fee,
    phone,
    email
):

    if not name or not teach or not phone or not email:

        return """
## ⚠️ Missing Information

Please enter:

- Your name
- Skill you can teach
- Phone number
- Email
"""

    # Determine fee
    if participation == "Skill Exchange":
        final_fee = "Free"

    elif participation == "Teach for Free":
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

    students.append(new_student)

    return f"""
# ✅ Profile Created!

### 👤 {name}

🟢 **Can Teach:** {teach}

🔵 **Wants to Learn:** {learn if learn else "Not specified"}

📊 **Level:** {level}

🌐 **Mode:** {mode}

💡 **Participation:** {participation}

💰 **Fee:** {final_fee}

📧 **Email:** {email}

📱 **Phone:** {phone}

---

Your profile is now available to other students.

🔒 Your contact details will **not be shown publicly**.
They are revealed only after a connection request.
"""


# ============================================================
# FIND MATCHES
# ============================================================

def find_matches(wanted_skill, my_skill):

    if not wanted_skill:

        return """
## 🔍 Enter a skill

Enter the skill you want to learn.
"""

    wanted_skill = wanted_skill.lower().strip()

    if my_skill:
        my_skill = my_skill.lower().strip()

    perfect_matches = []
    other_matches = []


    for index, student in enumerate(students):

        teaches = student["teach"].lower()
        wants = student["learn"].lower()

        # Student teaches what I want
        if wanted_skill in teaches:

            # PERFECT TWO-WAY MATCH
            if my_skill and my_skill in wants:

                perfect_matches.append(
                    (index, student)
                )

            else:

                other_matches.append(
                    (index, student)
                )


    result = ""


    # --------------------------------------------------------
    # PERFECT MATCHES
    # --------------------------------------------------------

    if perfect_matches:

        result += """
# 🔥 Perfect Skill Swaps

These students can teach what you want
AND want to learn what you can teach.

"""

        for index, student in perfect_matches:

            result += f"""
### 👤 {student["name"]}

🔄 **Perfect Skill Swap**

🟢 Teaches: **{student["teach"]}**

🔵 Wants to Learn: **{student["learn"]}**

📊 Level: {student["level"]}

🌐 Mode: {student["mode"]}

💰 Fee: {student["fee"]}

🆔 Student ID: `{index}`

---
"""


    # --------------------------------------------------------
    # OTHER MATCHES
    # --------------------------------------------------------

    if other_matches:

        result += """
# 🟡 Other Students Who Can Help

These students teach the skill you want,
but there is no two-way skill match.

"""

        for index, student in other_matches:

            result += f"""
### 👤 {student["name"]}

🟢 Teaches: **{student["teach"]}**

🔵 Wants to Learn: **{student["learn"]}**

📊 Level: {student["level"]}

🌐 Mode: {student["mode"]}

💰 Fee: {student["fee"]}

🆔 Student ID: `{index}`

---
"""


    if not perfect_matches and not other_matches:

        result = f"""
# 😕 No Match Found

We couldn't find anyone currently teaching:

**{wanted_skill.title()}**

Try another skill.
"""


    return result


# ============================================================
# REQUEST CONNECTION
# ============================================================

def request_connection(student_id):

    try:

        student_id = int(student_id)

    except:

        return """
⚠️ Please enter the Student ID shown in the search results.
"""


    if student_id < 0 or student_id >= len(students):

        return """
⚠️ Student ID not found.
"""


    student = students[student_id]

    connection_requests.append(student["name"])


    return f"""
# 🤝 Connection Request Sent!

Your request has been sent to:

### 👤 {student["name"]}

🟢 **Teaches:** {student["teach"]}

🔵 **Wants to Learn:** {student["learn"]}

---

### 📩 Contact Details

📧 **Email:** {student["email"]}

📱 **Phone:** {student["phone"]}

You can now contact the student and
arrange a learning session.

---

🔒 **Privacy Note:**
In a real application, contact details would
only become visible after the other student
accepts the request.
"""


# ============================================================
# BROWSE STUDENTS
# ============================================================

def browse_students():

    result = "# 👥 Students on SkillSwap\n\n"

    for index, student in enumerate(students):

        result += f"""
### 👤 {student["name"]}

🟢 **Can Teach:** {student["teach"]}

🔵 **Wants to Learn:** {student["learn"]}

📊 **Level:** {student["level"]}

🌐 **Mode:** {student["mode"]}

💡 **Type:** {student["type"]}

💰 **Fee:** {student["fee"]}

⭐ **Skill Credits:** {student["credits"]}

🆔 **Student ID:** `{index}`

🔒 Contact details hidden

---

"""

    return result


# ============================================================
# SKILL CREDITS
# ============================================================

def credits_info():

    return """
# ⭐ Skill Credits

Skill Credits encourage students to
share their knowledge.

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

⭐ +1 Skill Credit

↓

Use the credit to request help
with **Python**

---

**Skill Credits are not money.**

They represent participation in
the SkillSwap community.
"""


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(
    title="SkillSwap",
    theme=gr.themes.Soft()
) as app:

    gr.Markdown("""
# 🎓 SkillSwap
### *Learn. Teach. Connect.*

Student-to-student knowledge exchange platform.
""")


    # ========================================================
    # HOME
    # ========================================================

    with gr.Tab("🏠 Home"):

        gr.Markdown(home())


    # ========================================================
    # ADD SKILL
    # ========================================================

    with gr.Tab("➕ Add Your Skill"):

        gr.Markdown("""
## Create Your Skill Profile

Tell other students what you can teach
and what you want to learn.
""")

        name = gr.Textbox(
            label="👤 Your Name",
            placeholder="Enter your name"
        )

        teach = gr.Textbox(
            label="🟢 Skill You Can Teach",
            placeholder="Example: Python"
        )

        learn = gr.Textbox(
            label="🔵 Skill You Want to Learn",
            placeholder="Example: Canva"
        )

        level = gr.Dropdown(
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ],
            label="📊 Skill Level",
            value="Beginner"
        )

        mode = gr.Dropdown(
            [
                "Online",
                "Offline",
                "Both"
            ],
            label="🌐 Preferred Mode",
            value="Online"
        )

        participation = gr.Dropdown(
            [
                "Skill Exchange",
                "Teach for Free",
                "Paid Mentoring"
            ],
            label="💡 Participation Type",
            value="Skill Exchange"
        )

        fee = gr.Textbox(
            label="💰 Fee (Paid Mentoring only)",
            placeholder="Example: ₹100/session"
        )

        phone = gr.Textbox(
            label="📱 Phone Number",
            placeholder="Enter your phone number"
        )

        email = gr.Textbox(
            label="📧 Email",
            placeholder="Enter your email"
        )

        add_button = gr.Button(
            "➕ Create Profile",
            variant="primary"
        )

        add_output = gr.Markdown()

        add_button.click(
            add_skill,
            inputs=[
                name,
                teach,
                learn,
                level,
                mode,
                participation,
                fee,
                phone,
                email
            ],
            outputs=add_output
        )


    # ========================================================
    # FIND MATCH
    # ========================================================

    with gr.Tab("🔄 Find Skill Swap"):

        gr.Markdown("""
## 🔍 Find Your Learning Partner

Enter both skills to find a two-way exchange.
""")

        my_skill = gr.Textbox(
            label="🟢 I Can Teach...",
            placeholder="Example: German"
        )

        wanted_skill = gr.Textbox(
            label="🔵 I Want to Learn...",
            placeholder="Example: Python"
        )

        find_button = gr.Button(
            "🔍 Find My Match",
            variant="primary"
        )

        match_output = gr.Markdown()

        find_button.click(
            find_matches,
            inputs=[
                wanted_skill,
                my_skill
            ],
            outputs=match_output
        )


    # ========================================================
    # CONNECT
    # ========================================================

    with gr.Tab("🤝 Request to Connect"):

        gr.Markdown("""
## 🤝 Connect With a Student

Enter the **Student ID** shown in your search results.

Your request will be sent to that student.
""")

        student_id = gr.Textbox(
            label="Student ID",
            placeholder="Example: 1"
        )

        connect_button = gr.Button(
            "🤝 REQUEST TO CONNECT",
            variant="primary"
        )

        connection_output = gr.Markdown()

        connect_button.click(
            request_connection,
            inputs=student_id,
            outputs=connection_output
        )


    # ========================================================
    # BROWSE
    # ========================================================

    with gr.Tab("👥 Browse Students"):

        browse_button = gr.Button(
            "🔄 Refresh Students",
            variant="primary"
        )

        browse_output = gr.Markdown()

        browse_button.click(
            browse_students,
            outputs=browse_output
        )


    # ========================================================
    # SKILL CREDITS
    # ========================================================

    with gr.Tab("⭐ Skill Credits"):

        gr.Markdown(credits_info())


# ============================================================
# LAUNCH
# ============================================================

app.launch(share=True)
