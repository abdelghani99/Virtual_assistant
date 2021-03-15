import streamlit.components.v1 as components
import streamlit as st



st.title("Welcome to the Virtual Platform of the International Master of Biometrics and Intelligent Vision !")
components.html(
    """

<html>
    <head>
        <title>Your Website</title>

    </head>
    <body>
     <script type="text/javascript" src="https://hosted.us.uneeq.io/deploy/85a5816e-8b9a-4da9-8aff-9bca9b8c8086"></script>
    </body>
</html>
    """, width= 600, height= 800
)

components.html(
  """

<html>
    <head>
        <title>Your Website</title>

    </head>
    <body style="display:flex;display-direction:row;justify-content:flex-end;">
                <iframe
                        allow="microphone;"
                        width="350"
                        height="430"
                        src="https://console.dialogflow.com/api-client/demo/embedded/2f250ef2-627f-48f3-9ae7-33336d499aaa">
                 </iframe>
        </div>
    </body>
</html>
    """, width= 1100, height= 500
)


