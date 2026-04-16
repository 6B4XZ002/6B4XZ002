import streamlit as st

# 頁面設定
st.set_page_config(
    page_title="Huang Hsin - 個人簡歷",
    page_icon="🩺",
    layout="wide"
)

# 自訂 CSS（提升質感）
st.markdown("""
<style>
.main {
    background-color: #f8f9fb;
}
.title {
    font-size: 42px;
    font-weight: 700;
    color: #2c3e50;
}
.subtitle {
    font-size: 20px;
    color: #7f8c8d;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.highlight {
    color: #1abc9c;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown('<div class="title">Huang Hsin</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">個管師｜健麗醫護理之家</div>', unsafe_allow_html=True)

st.write("---")

# ===== 基本資料 =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📌 基本資料")

col1, col2 = st.columns(2)

with col1:
    st.write("📧 Email：zzz53032@gmail.com")
    st.write("📱 電話：0907097069")

with col2:
    st.write("🏢 公司：健麗醫護理之家")
    st.markdown("🌐 [官方 Facebook](https://www.facebook.com/profile.php?id=100086103357951)")

st.markdown('</div>', unsafe_allow_html=True)

# ===== 公司介紹 =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🏥 公司介紹")

st.write("""
健麗醫護理之家致力於提供專業、溫馨且高品質的長期照護服務，
結合醫療與生活照護，打造安心舒適的照護環境。
""")

st.markdown('</div>', unsafe_allow_html=True)

# ===== 服務項目 =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("💼 主要服務項目")

services = [
    "🩺 專業護理照護",
    "👵 長期照護服務",
    "🛏 失能／失智照護",
    "💊 藥物管理與健康監測",
    "🏃 復健與功能訓練",
    "🍱 營養餐食與生活照顧",
    "👨‍⚕️ 醫療團隊定期巡診",
]

for s in services:
    st.write(f"- {s}")

st.markdown('</div>', unsafe_allow_html=True)

# ===== 宣傳標語 =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("✨ 我們的理念")

st.markdown("""
> 💚 **用心照護每一天，守護長者的尊嚴與健康**  
> 💚 **專業 × 愛心 × 安心的全方位照護服務**
""")

st.markdown('</div>', unsafe_allow_html=True)

# ===== Footer =====
st.write("---")
st.caption("© 2026 Huang Hsin | 個人履歷網站")