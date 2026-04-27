streamlit_code = '''import streamlit as st
import pandas as pd

st.set_page_config(page_title="理財風險評估問卷", layout="centered")

st.title("💰 理財規劃風險評估 (KYC)")
st.write("請根據您的實際情況填寫，系統將自動計算評估結果。")

# 定義計分邏輯
questions = {
    "Q3: 學經歷符合項數": {"0項": 5, "1項": 4, "2項": 3, "3項": 2, "4項": 1},
    "Q4: 一般金融商品投資經驗": {"無經驗": 5, "1年以內": 4, "1年以上未滿3年": 3, "3年以上未滿5年": 2, "5年以上": 1},
    "Q5: 複雜商品投資經驗": {"無經驗": 5, "1年以內": 4, "1年以上未滿3年": 3, "3年以上未滿5年": 2, "5年以上": 1},
    "Q6: 個人總資產": {"小於300萬": 4, "300萬元以上未滿1000萬元": 3, "1000萬元以上未滿3000萬元": 2, "3000萬元以上": 1},
    "Q7: 家庭年收入": {"小於100萬": 4, "100萬元以上未滿300萬元": 3, "300萬元以上未滿500萬元": 2, "500萬元以上": 1},
    "Q8: 對投資配息的期待": {"不要求": 1, "年配": 2, "半年配": 3, "月配息": 4},
    "Q9: 偏好的投資期間": {"1年以下": 5, "1年以上未滿3年": 4, "3年以上未滿5年": 2, "5年以上": 1},
    "Q10: 緊急預備金保留比例": {"保留100%": 5, "保留約50%": 4, "保留約25%": 3, "保留10%以下": 1},
    "Q11: 願意承擔的風險報酬比率": {"僅承擔5%": 5, "僅承擔10%": 3, "僅承擔25%": 1},
    "Q12: 期望投資損益比率": {"5%;5%": 5, "10%;10%": 4, "15%;15%": 3, "20%;20%": 2},
    "Q13: 短期下跌20%的反應": {"全部出清": 5, "部分調整": 2, "持續追低": 1}
}

with st.form("kyc_form"):
    st.subheader("基本資料")
    st.selectbox("Q1: 資金來源", ["薪資所得", "繼承或贈與", "儲蓄", "退休金"])
    st.selectbox("Q2: 職業", ["政府機關", "金融服務業", "專業人士", "服務業", "學生/家管", "其他"])

    st.divider()
    st.subheader("風險評估題目")

    # 建立評分區
    answers = {}
    for q_text, options in questions.items():
        answers[q_text] = st.radio(q_text, list(options.keys()))

    submitted = st.form_submit_button("送出並計算結果")

if submitted:
    total_score = sum(questions[q][ans] for q, ans in answers.items())

    # 風險分級邏輯 (範例)
    if total_score >= 40:
        category = "保守型"
        color = "green"
        desc = "您偏好資本保值，不願承擔資產大幅波動。建議配置於高評等債券、貨幣基金或儲蓄型商品。"
    elif 25 <= total_score < 40:
        category = "穩健型"
        color = "orange"
        desc = "您願意在控制風險的前提下追求長期增值。建議採取股債均衡配置，適度參與市場成長。"
    else:
        category = "積極型"
        color = "red"
        desc = "您追求高報酬並能忍受較大的市場波動。建議配置於成長型股票、衍生性商品或特定產業基金。"

    st.balloons()
    st.markdown(f"### 評估結果：<span style='color:{color}'>{category}</span>", unsafe_allow_html=True)
    st.write(f"**您的總分：{total_score}**")
    st.info(desc)
'''

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(streamlit_code)

print("檔案 app.py 已成功建立！")
