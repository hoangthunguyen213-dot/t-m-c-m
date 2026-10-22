st.image("tam_cam.png", use_container_width=True)
import streamlit as st
import random

st.set_page_config(
    page_title="Tấm Cám - Giải cứu cây cau",
    page_icon="🌴",
    layout="centered"
)

# Giao diện
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff4dc, #e4f5df);
}
h1 {
    color: #a34c35;
    text-align: center;
}
.question {
    background: #fffaf0;
    padding: 18px;
    border-radius: 16px;
    border: 2px solid #f2c879;
}
</style>
""", unsafe_allow_html=True)

QUESTIONS = [
    {
        "q": "1. Khai triển (a + b)² bằng cách nào?",
        "options": [
            "A. a² + b²",
            "B. a² + 2ab + b²",
            "C. a² - 2ab + b²",
            "D. 2a + 2b"
        ],
        "answer": "B. a² + 2ab + b²",
        "explain": "(a + b)² = a² + 2ab + b²."
    },
    {
        "q": "2. Khai triển (a - b)² được kết quả nào?",
        "options": [
            "A. a² - b²",
            "B. a² + 2ab + b²",
            "C. a² - 2ab + b²",
            "D. a² + b²"
        ],
        "answer": "C. a² - 2ab + b²",
        "explain": "(a - b)² = a² - 2ab + b²."
    },
    {
        "q": "3. Công thức của a² - b² là gì?",
        "options": [
            "A. (a - b)²",
            "B. (a + b)²",
            "C. (a - b)(a + b)",
            "D. a² + 2ab + b²"
        ],
        "answer": "C. (a - b)(a + b)",
        "explain": "Hiệu hai bình phương: a² - b² = (a - b)(a + b)."
    },
    {
        "q": "4. Tính nhanh 21² - 19².",
        "options": [
            "A. 40",
            "B. 80",
            "C. 2",
            "D. 400"
        ],
        "answer": "B. 80",
        "explain": "21² - 19² = (21 - 19)(21 + 19) = 2 × 40 = 80."
    },
    {
        "q": "5. Khai triển (x + 3)² được gì?",
        "options": [
            "A. x² + 9",
            "B. x² + 6x + 9",
            "C. x² + 3x + 9",
            "D. x² - 6x + 9"
        ],
        "answer": "B. x² + 6x + 9",
        "explain": "(x + 3)² = x² + 2 × x × 3 + 3² = x² + 6x + 9."
    }
]

def start_game():
    st.session_state.question = 0
    st.session_state.lives = 3
    st.session_state.score = 0
    st.session_state.tree = 100
    st.session_state.finished = False
    st.session_state.review = []
    st.session_state.feedback = None
    st.session_state.answered = False

if "question" not in st.session_state:
    start_game()

st.title("🌴 TẤM CÁM: GIẢI CỨU CÂY CAU")
st.markdown(
    "<h3 style='text-align:center;'>Giúp Tấm giải câu đố để thoát khỏi Cám nhé!</h3>",
    unsafe_allow_html=True
)

st.markdown("### 🌸 Câu chuyện")
st.write(
    "Tấm đang mắc kẹt trên cây cau. Cám đang cưa cây! "
    "Trả lời đúng các câu hỏi hằng đẳng thức để giúp Tấm an toàn."
)

col1, col2, col3 = st.columns(3)
col1.metric("❤️ Mạng còn lại", st.session_state.lives)
col2.metric("⭐ Điểm", st.session_state.score)
col3.metric("🌳 Độ an toàn", f"{st.session_state.tree}%")

st.progress(st.session_state.tree / 100)

# Kết thúc trò chơi
if st.session_state.finished or st.session_state.lives <= 0:
    st.markdown("---")
    if st.session_state.lives <= 0:
        st.error("😱 Cây cau sắp đổ mất rồi! Bạn đã hết mạng.")
    else:
        st.success("🎉 Chúc mừng! Bạn đã hoàn thành thử thách và giúp Tấm an toàn!")
    st.write(f"Điểm cuối cùng: **{st.session_state.score}/{len(QUESTIONS)}**")

    with st.expander("📖 Xem lại đáp án"):
        for item in st.session_state.review:
            st.write(item)

    if st.button("🔄 Chơi lại", use_container_width=True):
        start_game()
        st.rerun()

else:
    q = QUESTIONS[st.session_state.question]

    st.markdown("---")
    st.markdown(
        f"<div class='question'><h3>{q['q']}</h3></div>",
        unsafe_allow_html=True
    )

    choice = st.radio(
        "Chọn đáp án của bạn:",
        q["options"],
        key=f"choice_{st.session_state.question}"
    )

    if not st.session_state.answered:
        if st.button("✨ Trả lời", use_container_width=True):
            correct = choice == q["answer"]

            if correct:
                st.session_state.score += 1
                st.session_state.feedback = (
                    True, "🎉 Chính xác! Tấm tạm thời an toàn!"
                )
            else:
                st.session_state.lives -= 1
                st.session_state.tree = max(
                    0, st.session_state.tree - 25
                )
                st.session_state.feedback = (
                    False, f"😮 Chưa đúng! Đáp án đúng là {q['answer']}"
                )

            st.session_state.review.append(
                f"Câu {st.session_state.question + 1}: "
                f"{'Đúng' if correct else 'Sai'}. "
                f"{q['explain']}"
            )
            st.session_state.answered = True
            st.rerun()

    if st.session_state.answered:
        correct, message = st.session_state.feedback

        if correct:
            st.success(message)
        else:
            st.error(message)

        st.info("💡 " + q["explain"])

        if st.session_state.lives <= 0:
            if st.button("Xem kết quả", use_container_width=True):
                st.session_state.finished = True
                st.rerun()
        elif st.button("➡️ Câu tiếp theo", use_container_width=True):
            st.session_state.question += 1
            st.session_state.answered = False
            st.session_state.feedback = None

            if st.session_state.question >= len(QUESTIONS):
                st.session_state.finished = True

            st.rerun()

st.markdown("---")
st.caption("📚 Ôn tập Toán: Ba hằng đẳng thức đáng nhớ đầu tiên")
