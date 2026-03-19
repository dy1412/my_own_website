import streamlit as st
import random
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 운세", page_icon="🔮", layout="centered")

# 2. 모던 스타일 적용 (라벤더 + 은하 + 카드 + 버튼)
st.markdown("""
<style>
/* 전체 앱 배경: 라벤더 + 은하 느낌 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #E6E6FA, #D8BFD8);
    background-size: cover;
}

/* 사이드바 배경 */
[data-testid="stSidebar"] {
    background-color: #D8BFD8;
}

/* 제목과 텍스트 */
h1, h2, h3, h4, p, span, div {
    color: #2E0854;  /* 진한 보라 */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* 운세 카드 */
.fortune-card {
    background: rgba(255,255,255,0.85);
    border-radius: 30px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 0 25px rgba(138,43,226,0.5), 0 0 15px rgba(75,0,130,0.2) inset;
    margin-bottom: 30px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.fortune-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 40px rgba(138,43,226,0.7), 0 0 20px rgba(75,0,130,0.3) inset;
}

/* 버튼 스타일 */
.stButton>button {
    background: linear-gradient(90deg, #9370DB, #BA55D3);
    color: #fff;
    font-weight: bold;
    border-radius: 20px;
    padding: 15px 0;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    box-shadow: 0 0 15px #BA55D3, 0 0 15px #9370DB;
    transform: scale(1.08);
}

/* 카드 안 텍스트 */
.fortune-card h2 {
    font-size: 2rem;
    color: #8A2BE2;
    margin-bottom: 10px;
}

.fortune-card h3 {
    font-size: 1.3rem;
    color: #4B0082;
    line-height: 1.6;
}

.fortune-card p {
    font-size: 1.1rem;
    color: #2E0854;
}
</style>
""", unsafe_allow_html=True)

# 3. 제목
st.markdown("<h1 style='text-align:center;'>🔮 오늘의 운세</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>오늘은 <b>{date.today().strftime('%Y년 %m월 %d일')}</b>입니다.</p>", unsafe_allow_html=True)

# 4. 운세 데이터
if 'selected_fortune' not in st.session_state:
    fortunes = {
        "행운": [
            "오늘은 생각지도 못한 곳에서 기분 좋은 소식이 들려옵니다. 💌",
            "잃어버렸던 물건을 찾거나 뜻밖의 선물을 받을 운세입니다. 🎁",
            "오늘 하루는 모든 일이 술술 풀리는 '프리패스'의 날! 🎫",
        ],
        "조언": [
            "오늘은 말 한마디에 천 냥 빚을 갚거나 만들 수 있으니 입조심! 🙊",
            "급할수록 돌아가세요. 서두르면 실수가 따르기 마련입니다. 🐢",
            "타인의 일에 간섭하기보다는 자신의 내실을 기할 때입니다. 🧘",
        ],
        "사랑": [
            "짝사랑하던 사람에게서 먼저 연락이 올지도 모릅니다. 📱",
            "연인과 깊은 대화를 나누며 서로의 소중함을 확인합니다. 💬",
            "오늘은 소개팅하기에 아주 좋은 날입니다. 인연이 기다립니다. 💘",
        ],
        "일/자기계발": [
            "막혔던 프로젝트에 번뜩이는 영감이 떠오릅니다. 💡",
            "오늘은 집중력이 최고조에 달해 업무 효율이 폭발합니다. ⚡",
            "상사나 선배로부터 기분 좋은 칭찬을 듣게 됩니다. 👍",
        ]
    }
    st.session_state.all_fortunes = fortunes
    st.session_state.selected_fortune = None
    st.session_state.flipped = False

# 5. 이름 / 별자리 / 띠 입력
st.divider()
user_name = st.text_input("👤 당신의 이름을 입력하세요", value="여행자")
col1, col2 = st.columns(2)
with col1:
    user_zodiac = st.selectbox("🌠 별자리 선택", [
        "양자리","황소자리","쌍둥이자리","게자리","사자자리","처녀자리",
        "천칭자리","전갈자리","사수자리","염소자리","물병자리","물고기자리"
    ])
with col2:
    user_animal = st.selectbox("🐾 띠 선택", [
        "쥐띠","소띠","호랑이띠","토끼띠","용띠","뱀띠","말띠",
        "양띠","원숭이띠","닭띠","개띠","돼지띠"
    ])
st.divider()

# 6. 카드 클릭 UI
st.markdown(f"<h3 style='text-align:center;'>🃏 {user_name}님, 카드를 클릭해 오늘의 운세를 확인하세요!</h3>", unsafe_allow_html=True)

if not st.session_state.flipped:
    if st.button(f"🧧 운세 확인", use_container_width=True):
        fortune_category = random.choice(list(st.session_state.all_fortunes.keys()))
        st.session_state.selected_fortune = random.choice(st.session_state.all_fortunes[fortune_category])
        st.session_state.lucky_number = random.randint(1,99)
        st.session_state.lucky_color = random.choice(["보라","파랑","핑크","흰색","은색"])
        st.session_state.flipped = True
        st.rerun()
    st.caption("카드를 클릭하면 오늘의 맞춤 운세와 행운 숫자가 공개됩니다.")
else:
    st.balloons()
    st.markdown(f"""
        <div class="fortune-card">
            <h2>🍀 오늘의 운세</h2>
            <p><b>{user_name}</b>님 ({user_zodiac} / {user_animal})의 운세</p>
            <hr>
            <h3>{st.session_state.selected_fortune}</h3>
            <p>🎲 행운 숫자: <b>{st.session_state.lucky_number}</b>  
               🎨 행운 색상: <b>{st.session_state.lucky_color}</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔄 다시 뽑기", use_container_width=True):
        st.session_state.flipped = False
        st.session_state.selected_fortune = None
        st.rerun()

st.divider()
st.caption(f"본 운세는 재미로만 즐겨주세요. 모든 선택은 {user_name}님의 몫입니다! ✨")
