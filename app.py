import streamlit as st

st.set_page_config(
    page_title="LinguaVerse",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8f3ff, #e9dcff, #ffffff);
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    text-align: center;
    padding: 20px 10px;
}
.hero h1 {
    color: #6841a5;
    font-size: 46px;
    font-weight: 700;
}
.hero p {
    color: #77638f;
    font-size: 17px;
}
.logo-card {
    background: white;
    border: 2px solid #e4d5ff;
    border-radius: 22px;
    padding: 25px 12px;
    text-align: center;
    min-height: 190px;
}
.logo-icon {
    font-size: 58px;
}
.logo-title {
    color: #6841a5;
    font-size: 20px;
    font-weight: 700;
}
.info-card {
    background: white;
    border: 1px solid #e5d9f8;
    border-radius: 18px;
    padding: 22px;
    margin-top: 18px;
}
.info-line {
    color: #513778;
    font-size: 16px;
    padding: 12px 4px;
    border-bottom: 1px solid #eee5fa;
}
.stButton > button {
    background: linear-gradient(90deg, #805ad5, #a47be5);
    color: white;
    border: none;
    border-radius: 14px;
    min-height: 52px;
    font-size: 19px;
    font-weight: 600;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown("""
    <div class="hero">
        <h1>📚✨ LinguaVerse ✨📚</h1>
        <p>Learn Words. Explore Stories. Grow Your English.</p>
        <p>Welcome to your English learning adventure!</p>
    </div>
    """, unsafe_allow_html=True)

    school_col, platform_col = st.columns(2, gap="large")

    with school_col:
        st.markdown("""
        <div class="logo-card">
            <div class="logo-icon">🏫</div>
            <div class="logo-title">شعار المدرسة</div>
            <p>الثانوية الخامسة بينبع البحر</p>
            <p>مكان الشعار الرسمي الذي سيُضاف لاحقًا</p>
        </div>
        """, unsafe_allow_html=True)

    with platform_col:
        st.markdown("""
        <div class="logo-card">
            <div class="logo-icon">📖✨⭐</div>
            <div class="logo-title">LinguaVerse</div>
            <p>English Learning Platform</p>
            <p>Learn • Discover • Achieve</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3 style="text-align:center;">معلومات المشروع</h3>
        <div class="info-line">
            🎓 <b>اسم الطالبة:</b> جنى سليم البرعي
        </div>
        <div class="info-line">
            👩‍🏫 <b>اسم المعلمة:</b> ليلى أحمد علاقي
        </div>
        <div class="info-line">
            🏫 <b>اسم المدرسة:</b> الثانوية الخامسة بينبع البحر
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center;color:#6841a5;font-size:17px;">
        Discover new words, enjoy English stories, and test your knowledge!
    </p>
    """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])

    with center:
        if st.button("🚀 Start Learning"):
            st.session_state.started = True
            st.rerun()

else:

    st.markdown("""
    <div class="hero">
        <h1>📚 LinguaVerse</h1>
        <p>Your journey to better English starts here!</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 العودة إلى الصفحة الرئيسية"):
        st.session_state.started = False
        st.rerun()

    page = st.radio(
        "اختاري القسم:",
        ["📘 Vocabulary", "📖 Stories", "📝 Quiz"],
        horizontal=True
    )

    if page == "📘 Vocabulary":
        st.header("📘 English Vocabulary")

        words = {
            "Explore": "يستكشف",
            "Discover": "يكتشف",
            "Journey": "رحلة",
            "Brave": "شجاع",
            "Achieve": "يحقق",
            "Curious": "فضولي",
            "Improve": "يحسّن",
            "Adventure": "مغامرة"
        }

        for word, meaning in words.items():
            st.write(f"**{word}** — {meaning}")

    elif page == "📖 Stories":
        st.header("📖 English Stories")

        stories = {
            "The Magical Library": (
                "A girl discovered a magical library. "
                "Every book took her to a new world.",
                "اكتشفت فتاة مكتبة سحرية، وكان كل كتاب "
                "يأخذها إلى عالم جديد."
            ),
            "A Trip to Japan": (
                "Sara traveled to Japan. She visited Tokyo "
                "and explored beautiful streets.",
                "سافرت سارة إلى اليابان، وزارت طوكيو "
                "واستكشفت شوارع جميلة."
            ),
            "The Space Adventure": (
                "A young astronaut traveled to Mars "
                "and discovered strange rocks.",
                "سافرت رائدة فضاء صغيرة إلى المريخ "
                "واكتشفت صخورًا غريبة."
            ),
            "The Brave Girl": (
                "Lina faced a difficult challenge. "
                "She stayed calm and solved the problem.",
                "واجهت لينا تحديًا صعبًا، وحافظت على "
                "هدوئها وحلّت المشكلة."
            ),
            "The Lost Treasure": (
                "Two friends found an old map "
                "and discovered a hidden treasure.",
                "وجد صديقان خريطة قديمة واكتشفا كنزًا مخفيًا."
            ),
            "A Day in London": (
                "Adam visited London and learned about "
                "British culture.",
                "زار آدم لندن وتعرّف على الثقافة البريطانية."
            ),
            "The Secret Garden": (
                "Maya found a secret garden and cared "
                "for its beautiful flowers.",
                "وجدت مايا حديقة سرية واعتنت بأزهارها الجميلة."
            ),
            "The Future City": (
                "A future city used clean energy "
                "to protect the environment.",
                "استخدمت مدينة مستقبلية الطاقة النظيفة "
                "لحماية البيئة."
            )
        }

        selected = st.selectbox("اختاري قصة:", list(stories.keys()))
        english, arabic = stories[selected]

        st.subheader("🌟 English")
        st.write(english)

        st.subheader("🌷 الترجمة العربية")
        st.write(arabic)

    elif page == "📝 Quiz":
        st.header("📝 English Quiz")

        questions = [
            ("What does Explore mean?", ["يستكشف", "ينام", "يكتب"], "يستكشف"),
            ("What does Brave mean?", ["خائف", "شجاع", "حزين"], "شجاع"),
            ("What does Discover mean?", ["يكتشف", "ينسى", "يغلق"], "يكتشف"),
            ("What does Journey mean?", ["حديقة", "رحلة", "نافذة"], "رحلة"),
            ("What does Improve mean?", ["يحسّن", "يخسر", "ينسى"], "يحسّن")
        ]

        with st.form("quiz_form"):
            answers = []

            for i, (question, options, correct) in enumerate(questions):
                st.write(f"**{i + 1}. {question}**")
                answers.append(
                    st.radio("اختاري الإجابة:", options, key=f"q{i}")
                )

            submitted = st.form_submit_button("Check Answers")

        if submitted:
            score = sum(
                answers[i] == questions[i][2]
                for i in range(len(questions))
            )
            st.subheader(f"نتيجتك: {score} / {len(questions)}")

            if score == len(questions):
                st.success("Excellent! 🎉")
            elif score >= 3:
                st.info("Good job! 🌟")
            else:
                st.warning("راجعي الكلمات وحاولي مرة أخرى 💪")

    st.caption("LinguaVerse — Learn something new every day! ✨")
