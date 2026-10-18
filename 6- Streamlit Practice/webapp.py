import streamlit as st
import pandas as pd
import seaborn as sns

df = pd.read_csv('tips.csv')

st.title('Hallo Leute von Heute!')
st.header('Wie kann man diese Model benutzen?')
st.subheader('Das Ziel erklaren!')
st.text('jede muss vor der Nutzung gut uber das Problem nachdenken.')
st.write('"WIE ICH SELBST!!!"')

st.subheader('Das DataFrame')
st.text('Schau mal das DataFrame:')

st.text('dataframe von streamlit:')
st.dataframe(df)

st.text('dataframe von "write":')
st.write(df)

st.markdown('**keiner Unterschid!**')
st.text('**kann man den text betonen?**')
st.markdown('''##### Aber mit Markdown kann man:
**betonen**''')

st.subheader('Aber nun es ist so weit einige sinvolle Functions kennenlernen')

st.metric('das accuracy von Model', '97.23%', '+2.23%')
st.bar_chart(sorted(df.tip))
st.line_chart(sorted(df.tip))
catplot = sns.catplot(df, x='sex', y='tip')
st.pyplot(catplot)

st.write('--------------------------')

st.header('Wie mussen Datei erhaltet werden?')
st.text('''
''')
slider = st.slider('das Slider ist so:', 20, 100, 30)
num = st.number_input('die nummer eingeben:', value=1000.0)
box = st.selectbox('die richtige option auswahlen:', ['gut', 'na ja'])
text = st.text_input('Den Text eingeben:')
agree = st.checkbox('bestatigen sie bitte')
filee = st.file_uploader('CSV Datei muss hochgeladen werden:', type='csv')

clicked = st.button('sag vorher!')


st.header('Erweiterte Einstellung')
st.markdown('**sidebar** ist hinzufugt')
para = st.sidebar.slider('parameter', 0, 10)
andi = st.sidebar.checkbox('andicators')
st.markdown('#### nun mehr als 1 columns')
col1, col2, col3 = st.columns(3)
col1.metric('erste metric', '22.34%')
col2.markdown('**-->**')
col3.metric('nechste metric', '86.23%', '63.85%')

st.write('---')

tab1, tab2 = st.tabs(["داده", "نتیجه"])  # تب
with tab1:
    st.dataframe(df)

with st.expander("توضیحات بیشتر"):    # بخش باز/بسته‌شونده
    st.write("...")

st.warning('Achtung!')
st.error('Problem!')
st.success('Erledigt!')

