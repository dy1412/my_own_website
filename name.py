import streamlit as st
from openai import OpenAI

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="냉장고 파먹기 AI 셰프", page_icon="👨‍🍳")

st.title("👨‍🍳 냉장고 파먹기 AI 셰프")
st.subheader("남은 재료를 알려주시면 맛있는 레시피를 제안해 드려요!")

# 2. OpenAI API 키 설정 (보안을 위해 사이드바에서 입력받거나 환경변수 권장)
with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password")
    st.info("API 키가 없으면 작동하지 않습니다. [OpenAI 홈페이지](https://platform.openai.com/)에서 발급받으세요.")

# 3. 사용자 입력 섹션
ingredients = st.text_input("냉장고에 있는 재료를 쉼표(,)로 구분해서 입력하세요", placeholder="예: 계란, 양파, 스팸, 찬밥")

# 4. 레시피 생성 로직
if st.button("레시피 생성하기! 🪄"):
    if not api_key:
        st.error("API 키를 입력해 주세요!")
    elif not ingredients:
        st.warning("재료를 입력해 주세요!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            with st.spinner('AI 셰프가 고민 중입니다... 잠시만 기다려주세요!'):
                # AI에게 전달할 프롬프트 구성
                prompt = f"""
                당신은 세계적인 요리사입니다. 사용자가 가진 재료들만 활용하거나, 
                집에 흔히 있을법한 양념(간장, 설탕, 소금 등)만 추가해서 만들 수 있는 최고의 요리를 추천해주세요.
                
                입력된 재료: {ingredients}
                
                형식:
                1. 요리 이름
                2. 재료 목록 (사용자가 입력한 것 위주)
                3. 상세 조리 단계 (1, 2, 3...)
                4. 셰프의 팁 (한 줄)
                """

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo", # 또는 "gpt-4"
                    messages=[{"role": "user", "content": prompt}]
                )

                recipe = response.choices[0].message.content
                
                # 5. 결과 화면 출력
                st.success("짜잔! 오늘의 추천 요리입니다.")
                st.markdown("---")
                st.markdown(recipe)
                
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

# 하단 안내
st.markdown("---")
st.caption("남은 재료를 버리지 말고 맛있는 요리로 변신시켜 보세요! 🥗")
