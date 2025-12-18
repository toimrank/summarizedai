import streamlit as st
import pandas as pd

st.title("Novartis and the NFL Get Proactive About Health")

st.text("Sports have a universal appeal that transcends boundaries. Each weekend, the NFL ignites millions of passionate fans from across the country, demonstrating the deep connection and power of community. At Novartis Pharmaceuticals Corporation, we share that same dedication in how we reimagine medicine that reached nearly 300 million patients worldwide in 2024 alone.")
st.text("Sports have a universal appeal that transcends boundaries. Each weekend, the NFL ignites millions of passionate fans from across the country, demonstrating the deep connection and power of community. At Novartis Pharmaceuticals Corporation, we share that same dedication in how we reimagine medicine that reached nearly 300 million patients worldwide in 2024 alone.")
st.text("Now, through a first-of-its-kind health partnership, Novartis and the NFL are harnessing the spirit of game day to advance better health decisions and early detection. Together, we aim to empower football fans everywhere to make proactive decisions about their health, understand screening guidelines, and build a playbook for a healthier future.")

st.image("https://www.novartis.com/us-en/sites/novartis_us/files/styles/cta_image/public/2025-07/victor-bulto.jpg.webp?itok=X1BtUdy_", use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:
    col1.title("Crucial Catch: An Important Initiative to Support Early Detection")
    col1.text("This football season, big plays won’t just be made on the field as Novartis, an official partner of the National Football League, joins as a sponsor of Crucial Catch in support of the American Cancer society. The partnership will expand the shared commitment to empower proactive health decisions and help more people detect cancer early by bringing educational resources and cancer screenings directly to communities throughout the United States.")
    st.button("Click Me")

with col2:
    col2.title("Commitment")    
    col2.text("The partnership will expand the shared commitment.")
    col2.image("https://www.novartis.com/us-en/sites/novartis_us/files/styles/crop_freeform/public/2025-09/NFL_CrucialCatch_stack_RGB.png.webp?itok=cHJZ6kk")

st.title("A Proactive Playbook")
st.text("While millions cheer on their favorite teams on the field, too many sideline their own well-being—skipping routine screenings or delaying crucial conversations with health care professionals about risks for certain conditions.")
st.image("https://www.novartis.com/us-en/sites/novartis_us/files/styles/crop_freeform/public/2025-07/prostate-cancer-with-actor-portrayal-title.png.webp?itok=GUtcMwtM")    

st.markdown("""
<a href="https://www.novartis.com/" target="_blank">
    <button style="padding:10px 20px; font-size:16px;">Novartis</button>
</a>
""", unsafe_allow_html=True)

df = pd.read_excel("Project-Management-Sample-Data.xlsx", 
        sheet_name="Project Management Data")
st.subheader("Test Data")
st.dataframe(df)

tab1, tab2 = st.tabs(["Tab1","Tab2"])
tab1.text("Give breasts the attention they deserve. Early detection for breast cancer changes the game, so let’s kick off a new era of breast health. Take the next step to schedule your routine screening or discover your risk for breast cancer.")
tab1.video("https://www.w3schools.com/html/mov_bbb.mp4")

tab2.text("Prostate cancer is the second leading cause of cancer death in men in the United States1. Too often men stay silent when dealing with a prostate cancer diagnosis. You can help make a difference. Speak up for yourself or your loved ones.")
tab2.image("https://www.novartis.com/us-en/sites/novartis_us/files/styles/cards_1_3/public/2025-07/nfl-player-health-and-safety_0.jpg.webp?itok=lxrYMSTi", caption="Public Health")

expander = st.expander("More Info")
expander.image("https://www.novartis.com/us-en/sites/novartis_us/files/styles/cards_1_3/public/2025-07/novartis-nfl-hall-of-fame-enshrinement-week.jpg.webp?itok=uT0QWH9G")
expander.text("Notably, the laboratory testing results are supported by recent on-field data. Players in top-performing helmets had a substantially lower rate of concussions than players wearing lesser-performing helmets. The 2024 season marked the largest safety improvement in helmets worn on-field since 2021, contributing to the fewest concussions in an NFL season on record.")
expander.text("As the NFL has continued to drive advancements in helmet technology, there are now 10 Guardian Cap Optional helmets available to players. These helmets provide as much – and in some cases more – protection than helmets paired with a Guardian Cap, affording players additional safety options as they make their helmet choice. Players in positions covered by the Guardian Cap requirement may instead choose to wear one of these helmets and forgo a Guardian Cap for practices.")