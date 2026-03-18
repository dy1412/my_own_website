import streamlit as st
import random
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 운세는?", page_icon="🃏")

# 2. 제목 변경
st.title("🔮 오늘의 운세는?")
st.write(f"오늘은 {date.today().strftime('%Y년 %m월 %d일')}입니다.")

# 3. 데이터 준비 (랜덤 문구)
fortunes = [
    "✨ 오늘은 생각지도 못한 행운이 넝쿨째 굴러들어올 날입니다!",
    "🏃 적극적으로 움직이세요. 가만히 있으면 기회를 놓칠 수 있습니다.",
    "🎁 소중한 사람에게 작은 선물을 해보세요. 배가 되어 돌아옵니다.",
    "🧘 마음의 여유가 필요한 날입니다. 따뜻한 차 한 잔 어떠세요?",
    "💰 금전운이 상승하고 있습니다! 계획했던 소비를 해도 좋은 날입니다.",
    "🤫 비밀을 잘 지켜야 합니다. 구설수에 오를 수 있으니 조심하세요.",
    "🌈 고민하던 문제가 말끔히 해결될 징조가 보입니다.",
    "🍀 파란색 아이템이 행운을 가져다줄 거예요.",
    "💡 새로운 아이디어가 샘솟는 날입니다. 메모를 잊지 마세요!",
    "🍎 건강을 위해 가벼운 산책을 추천합니다. 몸이 가벼워질 거예요."
]

# 4. 입력 섹션
st.divider()
col1, col2 = st.columns(2)
with col1:
    user_zodiac = st.selectbox("🌠 별자리 선택", 
        ["양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리", "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"])
with col2:
    user_animal = st.selectbox("🐾 띠 선택", 
        ["쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠", "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"])

st.divider()

# 5. 카드 뒤집기 로직 (세션 상태 활용)
if 'flipped' not in st.session_state:
    st.session_state.flipped = False # 카드가 뒤집혔는지 여부
    st.session_state.selected_fortune = random.choice(fortunes) # 뽑힌 운세

st.write("▼ 아래 버튼을 클릭해서 운세를 확인하세요!")

# 6. 카드 UI 구현
# 버튼을 카드처럼 크게 디자인합니다.
if not st.session_state.flipped:
    # 카드 앞면 (클릭 전)
    if st.button(f"✨\n\n{user_zodiac} & {user_animal}\n\n당신의 운세는?\n\n(클릭해서 뒤집기)", use_container_width=True, type="primary"):
        st.session_state.flipped = True
        st.rerun()
else:
    # 카드 뒷면 (클릭 후)
    st.balloons() # 축하 효과
    st.success("운세를 확인해보세요!")
    
    # 결과 창 디자인
    st.markdown(f"""
        <div style="
            background-color: #ffffff;
            border: 5px solid #FF4B4B;
            border-radius: 20px;
            padding: 50px;
            text-align: center;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        ">
            <h2 style="color: #FF4B4B;">🍀 오늘의 결과</h2>
            <hr>
            <h1 style="font-size: 1.5rem; color: #31333F;">{st.session_state.selected_fortune}</h1>
            <p style="color: #888; margin-top: 20px;">{user_zodiac} {user_animal}님, 좋은 하루 되세요!</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("본 운세는 재미로만 즐겨주세요. 모든 선택은 당신의 몫입니다!")
