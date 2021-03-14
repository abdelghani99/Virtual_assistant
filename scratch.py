import streamlit.components.v1 as components
import streamlit as st



st.title("Welcome to BVIBot !")
components.html(
    """

<html>
    <head>
        <title>Your Website</title>
        <script type="text/javascript" src="https://hosted.us.uneeq.io/deploy/85a5816e-8b9a-4da9-8aff-9bca9b8c8086"></script>

    </head>
    <body>
        Your website.
    </body>
</html>
    """, width= 200, height= 200
)

components.html(
    """
    <iframe
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/2f250ef2-627f-48f3-9ae7-33336d499aaa">
</iframe>
 """, width= 2000, height= 2000
)

