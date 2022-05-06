import streamlit as st
import webbrowser
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')

# SIDEBAR


def sidebar():
    st.sidebar.title("-Ana de Toro-")
    st.sidebar.write("A look into my personal art including paintings, photography and ceramics which I'm selling. "
                     "I have worked hard to create all these products with love by hand. Each piece is unique and one-of-a-kind, "
                     "so I hope you find the piece that speaks to you.")
    st.sidebar.markdown("#### Do you want help a local artist? :coffee:")
    link = '[Buy me a coffe](https://ko-fi.com/anadetoro)'
    st.sidebar.markdown(link, unsafe_allow_html=True)

sidebar()

# Style sidebar
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Menu option
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Projects", 'About', "Contact"],  # required
    icons=["house", 'brush', 'person', "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white"},  # fafad2
        "icon": {"color": "#eac248", "font-size": "18px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "#eac248",
        },
        "nav-link-selected": {"background-color": "#faf0d2", 'color': '#ea9a48'},
    },
)
# HOME
if selected == "Home":
    col1, col2 = st.columns((6, 4))
    col1.image('Captura.PNG')
    with col2:
        st.markdown("## - Ana's art and creations -")
        st.image('ceramica.PNG')

# PROJECTS

if selected == "Projects":
    st.title(f"{selected}")
    col0, cola = st.columns(2)
    with col0:
        initial = st.multiselect('What do you want to see?', ['Paints', 'Pottery', 'Photography'], ['Paints'])
        tick = st.checkbox('Show all')
    with cola:
        price = st.slider('Maximum price', 50, 200, 100)
        st.markdown('💵 Maximum of ' f'**{price}**' ' **kroner** 💵')

    # Columns;
    col1, col2 = st.columns((3, 7))
    col3, col4 = st.columns((3, 7))
    col5, col6 = st.columns((3, 7))
    col7, col8 = st.columns((3, 7))
    col9, col10 = st.columns((3, 7))
    col11, col12 = st.columns((3, 7))
    col13, col14 = st.columns((3, 7))
    col15, col16 = st.columns((3, 7))
    col17, col18 = st.columns((3, 7))
    col19, col20 = st.columns((3, 7))

    def blue():
        col1.image('paint1.PNG')
        col2.header('- Abstract -')
        col2.write('Here is a more abstract piece I have made with many colors.')
        pric = 100
        col2.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col2.button('Buy this item', key="<motomami>")

    def people():
        col3.image('people.PNG')
        col4.header('- People -')
        col4.write('I do personal paintings with people in them.')
        pric = 125
        col4.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col4.button('Buy this item', key="<bro>")

    def houses():
        col5.image('casas.PNG')
        col6.header('- Environment -')
        col6.write('''
                Here is my most recent artwork for sale. I enjoy doing paintings that portray     
                realism and represent beauty in everyday life.

                This piece portrays a beautiful house in nature.''')
        pric = 150
        col6.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col6.button('Buy this item', key="<klk>")

    if 'Paints' in initial:
        if tick:
            blue()
            people()
            houses()
        else:
            if 99 < price < 125:
                blue()
            elif 99 < price < 150:
                blue()
                people()
            elif 99 < price < 201:
                blue()
                people()
                houses()

    def candle():
        col7.image('candle.PNG')
        col8.header('- Candles -')
        col8.write('Here are my Candles. On these you can choose a particular color.')
        pric = 75
        col8.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col8.button('Buy this item', key='<klkkk>')

    def flowers():
        col9.image('flores.PNG')
        col10.header('- Flowers -')
        col10.write('Here are my rough pots. On these you can choose a particular pattern.')
        pric = 60
        col10.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col10.button('Buy this item', key='<klokk>')

    def ceramica():
        col11.image('ceramica.PNG')
        col12.header('- Pots -')
        col12.write('My newest art is pottery. Here are some of my smooth pots. I do both ringed and simple.')
        pric = 80
        col12.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col12.button('Buy this item',
                     key="<uniquevalueofsomesort>")  #:cart2: https://icons.getbootstrap.com/ no funciona porque es de css

    if 'Pottery' in initial:
        if tick:
            candle()
            flowers()
            ceramica()
        else:
            if 59 < price < 75:
                candle()
            elif 9 < price < 80:
                candle()
                flowers()
            elif 9 < price < 201:
                candle()
                flowers()
                ceramica()

    def nature():
        col13.image('nature.PNG')
        col14.header('- Nature -')
        col14.write('I do nature photos in the setting and lighting of your choice.')
        pric = 75
        col14.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col14.button('Buy this item', key="<keyky>")

    def personal():
        col15.image('personal.PNG')
        col16.header('- Self portrait -')
        col16.write(
            'I do self portrait photography. Some of this includes color photos I can take, including close-ups such as this.')
        pric = 100
        col16.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col16.button('Buy this item', key="<uniqrt>")

    def other():
        col17.image('other.PNG')
        col18.header('- Black and withe -')
        col18.write('I take black and white photos with high-quality lighting.')
        pric = 120
        col18.write('The **price** of this painting is ' f'**{pric}**' ' **kroner.**')
        col18.button('Buy this item', key="<keykey>")

    if 'Photography' in initial:
        if tick:
            nature()
            personal()
            other()

        else:
            if 74 < price < 100:
                nature()
            elif 74 < price < 120:
                nature()
                personal()
            elif 74 < price < 201:
                nature()
                personal()
                other()

# ABOUT
if selected == "About":
    st.title(f"{selected}")
    col9, col10 = st.columns((3, 7))
    with col9:
        st.image('yo.PNG')
    with col10:
        st.text("""
    My name is Ana de Toro, although sometimes I am all one name: anadetoro.
    I am a Virgo.
    I have always had green eyes.
    I like my hair because it looks like a jungle.
    I like second hand clothes and bright (not shiny) colors.
    I like cooking, the mole on my left wrist, walking to the rhythm 
    of music and hanging clothes with clothespins of the same color.
    Oh, and my favorite times are breakfast and after lunch coffee 🤤.
    The last book I read is Bomarzo, by Manuel Mujica Lainez.
    *and I usually work with my hair up and comfortable clothes.
        
    I'm not used to show myself in social networks, but this year
    I want to make myself more known,
    to be able to bring closer what I feel and express through art.
    """)
    st.subheader('My social media')
    col31, col32, col33, col34, col35, col36 = st.columns(6)
    with col31:
        link1 = '[My Instagram](https://www.instagram.com/anadetg/)'
        st.markdown(link1, unsafe_allow_html=True)
    with col32:
        link2 = '[My Real Webpage](https://www.anadetoro.com/)'
        st.markdown(link2, unsafe_allow_html=True)
    st.subheader('More about the investigation')
    with st.expander('Purpose investigation'):
        st.write('The purpose of this investigation is blablabla')

# CONTACT
if selected == "Contact":
    st.title(f"{selected} :envelope:")
    contact_form = """
    <form action="https://formsubmit.co/anacollados98@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)


    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style_form.css")

