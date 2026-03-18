import streamlit as st
import random
from datetime import date

# --- PAGE CONFIG ---
st.set_page_config(page_title="오늘의 픽셀 운세", page_icon="🔮")

# --- DATA: 무작위 운세 문구 리스트 ---
# 라이브러리 설치를 안 하므로, 미리 정의된 문구에서 랜덤 추출합니다.
fortunes_list = [
    "오늘은 생각지 못한 곳에서 행운이 찾아옵니다. 주위를 잘 살펴보세요!",
    "작은 오해가 생길 수 있으니, 말과 행동에 신중을 기하는 것이 좋습니다.",
    "그동안 노력했던 일들이 결실을 맺는 날입니다. 자신감을 가지세요!",
    "오늘은 새로운 사람을 만나기에 아주 좋은 날입니다. 적극적으로 움직이세요.",
    "건강 운이 약간 저조합니다. 무리하지 말고 충분한 휴식을 취하세요.",
    "금전적인 부분에서 기쁜 소식이 들려옵니다. 복권 한 장 어떠세요?",
    "결정을 내리기 힘든 문제가 있다면, 오늘은 잠시 미루는 것이 현명합니다.",
    "친한 친구와의 대화에서 중요한 힌트를 얻게 될 것입니다.",
    "오늘은 파란색 계열의 옷이 행운을 가져다줍니다.",
    "뜻밖의 칭찬을 듣게 되어 하루 종일 기분이 좋아질 것입니다.",
    "묵묵히 자신의 길을 가면 결국 성공합니다. 조급해하지 마세요.",
    "오늘은 집에서 조용히 취미 생활을 즐기는 것이 이득입니다."
]

# --- UI: MAIN TITLE ---
st.title("🔮 오늘의 운세: 픽셀 카드를 뒤집어라!")
st.subheader(f"{date.today().strftime('%Y년 %m월 %d일')}의 운세")
st.write("나의 별자리와 띠를 선택하고, 운세 카드를 터치해 보세요.")

# --- UI: SELECTION ---
col1, col2 = st.columns(2)

with col1:
    zodiac_signs = ["양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리", 
                    "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"]
    user_zodiac = st.selectbox("🌠 나의 별자리", zodiac_signs)

with col2:
    animal_signs = ["쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠", 
                    "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"]
    user_animal = st.selectbox("🐾 나의 띠", animal_signs)

st.divider()

# --- LOGIC: FORTUNE GENERATION (Session State 사용) ---
# 사용자가 입력을 바꿀 때마다 운세가 계속 바뀌지 않도록 '오늘의 운세'를 세션에 고정합니다.
if 'today_fortune' not in st.session_state:
    # 띠와 별자리를 조합하여 유일한 값을 만들고, 이를 무작위 시드로 사용하여
    # 같은 날, 같은 조합이면 항상 같은 운세가 나오도록 설정할 수 있습니다. (구현 생략 - 완전 무작위)
    st.session_state['today_fortune'] = random.choice(fortunes_list)

# 별자리나 띠가 바뀌면 운세를 다시 생성하도록 버튼을 추가할 수도 있습니다.
# (이 코드에서는 완전 무작위로 세션에 저장된 것만 보여줍니다.)


# --- UI:
