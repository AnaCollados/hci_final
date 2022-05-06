import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
    )

if selected=="Home":
    st.title(f"{selected}")
    with st.container():
        st.title("Ana's Art and Creations")  # how to put emojis?
        st.write("A look into my personal art including paintings, photography and ceramics which I'm selling. I have worked hard to create all these products with love by hand. Each piece is unique and one-of-a-kind, so I hope you find the piece that speaks to you")
        page_icon=":tada:"
    with st.container():
        st.write("---")
        left_column, right_column= st.columns(2)
    with left_column:
        st.header("About Me")
        st.write('##')
        st.write(
            """
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
            """
        )

    image='Art.png'

    with right_column:
        st.image(image)

# Present a button for these varibables to show

#my_code = 

#with st.expander("Show code"):
    #st.code(my_code, language="python")
    # how to put enter in markdown??
    # here we have to have the figure of the first plot

    with st.container():
        st.write("Want to see more? Here is a link to my instagram page showcasing my creative process and products")
        st.write("[Learn More >](https://www.instagram.com/anadetg/?fbclid=IwAR0qR3i0NxWrG1F7vHFmJbtZX3pS64vvX1mcJ5A55oVQd_6pa1KGTNayJxU)")

#uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])





from PIL import Image

#st.sidebar.write("About me, what I do, product examples, more info", width=180)
imageh='House.png'
if selected=="Projects":
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        st.header("My Paintings")
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imageh, caption='Environment Painting')
    with text_column:
        st.write(
            """
            Here is my most recent artwork for sale. I enjoy doing paintings that portray realism and represent beauty in everyday life

            This piece portrays a beautiful house in nature.


            150 DKK
            """
        )
    imagec='Colors.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagec, caption='Abstract Art')
    with text_column:
        st.write(
            """
            Here is a more abstract piece I have made with many colors.


            100 DKK
            """
        )

    imagep='People.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagep, caption='People Paintings')
    with text_column:
        st.write(
            """
            I do personal paintings with people in them. 

            125 DKK 
            """
        )

    
    
    imagef='Face.png'
    with st.container():
        st.write("---")
        st.header("My Photography")
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagef, caption='Color Photos')
    with text_column:
        st.write(
            """
            I do self-portraits. Some of this includes color photos I can take, including close-ups such as this.


            100 DKK
            """
        )
    imageb='Black.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imageb, caption='Black and White Photos')
    with text_column:
        st.write(
            """
            I take black and white photos with high-quality lighting.

            120 DKK
            """
        )
    imagen='Nature.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagen, caption='Nature Photos')
    with text_column:
        st.write(
            """
            I do nature photos in the setting and lighting of your choice.


            75 DKK
            """
        )
    images='Smooth_pots.png'
    with st.container():
        st.write("---")
        st.header("My Pottery")
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(images, caption='Smooth Pots')
    with text_column:
        st.write(
            """
            My newest art is pottery. Here are some of my smooth pots. I do both ringed and simple.

            80 DKK


            """
        )
    imager='Rough_pots.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imager, caption='Rough Pots')
    with text_column:
        st.write(
            """
            Here are my rough pots. On these you can choose a particular pattern.


            60 DKK
            """
        )
    imagep='Pink.png'
    with st.container():
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagep, caption='Candles')
    with text_column:
        st.write(
            """
            Here are my Candles. On these you can choose a particular color.


            75 DKK
            """
        )



if selected=="Contact":
    st.title(f"{selected}")
    with st.container():
        st.write("---")
        st.header("Reach Out to Me if Interested in a Product!")
        st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/alainamartine@gmail.com" method="POST">
        <input type="hidden" name="__captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
