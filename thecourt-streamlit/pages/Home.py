
import streamlit as st
import time
from PIL import Image #convert library image

image_path = 'pages/static/THE COURT LOGO.png'
image = Image.open(image_path)

#st.title('WELCOME TO :red[THE COURT STARTS] WEBSITE')
st.markdown(
    '''
    <h1 style="text-align: center; font-size: 37px;">WELCOME TO THE COURT STATS WEBSITE</h1>
    ''',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
   st.image(image)

with col2:
    st.markdown('<div style="text-align: justify; font-family: Arial, sans-serif;">'
                '<br>'
                '<br>'
                '<h5 style="font-family: Arial, sans-serif; font-style: italic;">'
                'Exploring Insights, Unveiling Patterns: Your Gateway to Data Analysis Excellence'
                '</h5>'
                '</div>', unsafe_allow_html=True)



# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1, text=progress_text)

st.subheader('TO OUR CLUB')
st.markdown(
    '''
    <p align="justify">THE COURT merupakan media informasi dan penyedialayanan teknologi IT untuk bidang 
    sports analytics khususnya di Indonesia dengan mengolaborasikan data olahraga dengan teknologi informasi 
    yang massive dan progressive kepada Sports Teams, Sports Media, Sport Fans dan Governing Bodies. Kami 
    memberikan solusi dalam bentuk Analytics Consulting, Data as a Service dan Partner Collaboration dengan 
    sistem kerja yang agile dan comprehensive.</p>
    ''',
    unsafe_allow_html=True
)
st.subheader('VISI THE COURT')
st.markdown(
    '''
    <p align="justify">THE COURT memiliki visi menjadi perusahaan pionir pada bidang sports analytics 
    di Indonesia dalam menciptakan inovasi dan transformasi untuk industri olahraga.</p>
    ''',
    unsafe_allow_html=True
)

st.subheader('MISI THE COURT')
st.markdown(
    '''
    <h4 style="text-align: center;">SPORTS ANALYTICS CONSULTANT</h4>
    <p align="center">THE COURT menjadi penyedia jasa layanan konsultasi sports analytics dan sports data
    management dengan penerapan teknologi Modern Data Infrastructure</p>

    <h4 style="text-align: center;">SPORTS DATA WAREHOUSE</h4>
    <p align="center">THE COURT menghimpun berbagai data olahraga dari berbagai sumber data dengan penerapan
    arsitektur IT yang mumpuni</p>

    <h4 style="text-align: center;">SPORTS ANALYTICS TECH DEV</h4>
    <p align="center">THE COURT menjadi developer dalam pengembangan teknologi sports analytics terbaru</p>

    <h4 style="text-align: center;">SPORTS ANALYTICS MEDIA</h4>
    <p align="center">THE COURT menjadi media dalam memberikan informasi dan edukasi terkait perkembangan
    teknologi di bidang sports analytics</p>
    ''',
    unsafe_allow_html=True
)

st.subheader('WHO WE HELP')
tab1, tab2, tab3, tab4 = st.tabs(["SPORTS MEDIA", "SPORTS TEAM", "SPORTS FANS", "GOVERNING BODIES"])
with tab1:
   #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Media</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/who_help/sports media.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Media</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Menjadi “partner” atau penyuplai data bagi media-media olahraga dalam membuat 
    sebuah konten maupun infografis yang berkaitan dengan data & statistic.</p>
    ''',
    unsafe_allow_html=True
    )

with tab2:
   #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Team</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/who_help/sports team.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Team</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Percaya diri untuk bisa menjadi konsultan data & statistic untuk meningkatkan 
    performa tim maupun individu didalamnya bagi klub-klub olahraga.</p>
    ''',
    unsafe_allow_html=True
    )

with tab3:
   #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Fans</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/who_help/sports fans.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Fans</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Antusias untuk menjadi platform yang bisa bekerjasama dengan berbagai fansbase 
    klub maupun pemain olahraga untuk menyajikan data & statistic.</p>
    ''',
    unsafe_allow_html=True
    )

with tab4:
   #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Governing Bodies</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/who_help/governing bodies.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Governing Bodies</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Dengan talenta yang ada, kami mampu bekerjasama dengan federasi olahraga dalam
    pengimplementasian teknologi di dalam maupun luar lapangan</p>
    ''',
    unsafe_allow_html=True
    )

st.markdown(
    '''
    <br>
    <br>
    <p align="center" style="font-size: 20px;"><em><strong><span style="text-transform: uppercase;">Dengan banyaknya database yang kami punya dan orang-orang bertalenta didalamnya, 
    kami percaya diri untuk bisa menjadi solusi bagi permasalahan olahraga yang berkaitan dengan data 
    & statistic.</span></strong></em></p>
    <br>
    <br>
    ''',
    unsafe_allow_html=True
)

st.subheader('CARA KAMI BEKERJA')
col1, col2, col3 = st.columns(3)
with col1:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Media</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/cara_bekerja/data collection.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">DATA COLLECTION</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Data di ambil secara mentah dari berbagi sumber yang telah ada. Pengkoleksian data
    dilakukan lewat berbagai cara, baik melalui Pemograman Komputer ataupun dihimpun secara Manual oleh 
    team kam</p>
    ''',
    unsafe_allow_html=True
    )

with col2:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Team</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/cara_bekerja/data manipulation.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">DATA MANIPULATION</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Data yang mentah perlu di manipulasi agar menghasilkan suatu informasi tertentu.
    Manipulasi yang dilakukan termasuk penentuan Metric, pembersihan Data, hingga kalkulasi Data.</p>
    ''',
    unsafe_allow_html=True
    )

with col3:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Fans</h5></div>', unsafe_allow_html=True)
    st.image("pages/static/cara_bekerja/product serving.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">PRODUCT SERVING</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Data yang telah bersih dan berisi informasi dapat disajikan secara Visualisasi Grafis,
    Dashboard Analytic, dan Machine Learning untuk menemukan pola kejadian data.</p>
    ''',
    unsafe_allow_html=True
    )

st.subheader('DATA KAMI')
st.image("pages/static/DATA KAMI.jpg") 
st.markdown(
    '''
    <p align="justify">Kami menghimpun berbagai macam data olahraga dari berbagai
    macam liga di seluruh dunia. Terhitung hingga kini, terdapat 8 liga di dunia yang THE COURT olah
    menjadi sebuah insight dan informasi.</p>
    ''',
    unsafe_allow_html=True
)

st.subheader('SERVICE PRODUCT')
col1, col2, col3 = st.columns(3)
with col1:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Media</h5></div>', unsafe_allow_html=True)
    #st.image("pages/static/data collection.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Analytics Consulting</h5></div>', unsafe_allow_html=True)
  

with col2:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Team</h5></div>', unsafe_allow_html=True)
    #st.image("pages/static/data manipulation.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Data as a Service</h5></div>', unsafe_allow_html=True)

with col3:
    #st.markdown('<div style="text-align: left;"><h5 style="margin-bottom: 0; font-size: 16px;">Sports Team</h5></div>', unsafe_allow_html=True)
    #st.image("pages/static/data manipulation.jpg")
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">Partner Collaboration</h5></div>', unsafe_allow_html=True)

st.subheader('THE COURT GALERY')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
with tab1:
    st.image("pages/static/gallery/1.png")
with tab2:
    st.image("pages/static/gallery/2.png")
with tab3:
    st.image("pages/static/gallery/3.png")
with tab4:
    st.image("pages/static/gallery/4.png")
with tab5:
    st.image("pages/static/gallery/5.png")
with tab6:
    st.image("pages/static/gallery/6.png")
with tab7:
    st.image("pages/static/gallery/7.png")
with tab8:
    st.image("pages/static/gallery/8.png")
with tab9:
    st.image("pages/static/gallery/9.png")
with tab10:
    st.image("pages/static/gallery/10.png")
with tab11:
    st.image("pages/static/gallery/11.png")
with tab12:
    st.image("pages/static/gallery/12.png")

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

st.markdown(
    '''
    <br>
    <br>
    <h1 style="text-align: center; font-size: 20px;">FOR MORE INFO ABOUT OUR PORTOFOLIO</h1>
    ''',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">CONTACT US</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">+62 888-1852-534</p>
    ''',
    unsafe_allow_html=True
    )

with col2:
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">SEND US AN EMAIL</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">thecourt.chart@gmail.com</p>
    ''',
    unsafe_allow_html=True
    )

with col3:
    st.markdown('<div style="text-align: center;"><h5 style="margin-bottom: 0; font-size: 16px;">CHECK OUR SOCIAL MEDIA</h5></div>', unsafe_allow_html=True)
    st.markdown(
    '''
    <p align="center">Instagram, Linkedin, Tiktok @thecourt.stats</p>
    ''',
    unsafe_allow_html=True
    )