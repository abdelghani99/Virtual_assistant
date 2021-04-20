import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import hashlib
import sqlite3

import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()




#for password encrypting
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False


# Data_base
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()



# Data_base queries
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data





def main():

	st.title("Welcome to the Virtual Platform of the International Master of Biometrics and Intelligent Vision !")

	menu = ["Home","SignIn","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		components.html(
                             """
                         <html>
                           <head>
                                   <title>Your Website</title>
                           </head>
                           <body>
                               <script type="text/javascript" src="https://hosted.us.uneeq.io/deploy/b627d925-ce31-4e86-8410-4284cbc0f37d"></script>
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
                           <body>
                               <script type="text/javascript"
                                  id="botcopy-embedder-d7lcfheammjct"
                                  class="botcopy-embedder-d7lcfheammjct" 
                                  data-botId="607ea73de7e5640009900608">
                                                                                                   
                                  var s = document.createElement('script'); 
                                  s.type = 'text/javascript'; s.async = true; 
                                  s.src = 'https://widget.botcopy.com/js/injection.js'; 
                                  document.getElementById('botcopy-embedder-d7lcfheammjct').appendChild(s);
                               </script>
                           </body>
                         </html>
                               """, width= 600, height= 900
		
			
)
		
		
		
		
		
		
		
		
		
		
		
		
		

	elif choice == "SignIn":
		

		username = st.sidebar.text_input("User")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Access"):
			
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Services",["About our university","About our master","Program", "Apply", "Schedule M1", "Schedule M2", "News", "Contact"])
				if task == "About our master":
					st.subheader("It's about, Artificial Intelligence, Computer Vision,  Data Science, for bioengineering applications")

				elif task == "About our university":
					st.subheader(" is a public university located in Créteil, Île-de-France, France. It was inaugurated in 1970. The university offers training in law, arts and humanities, sciences and technology, economics and development, administration and exchange, educational science, as well as social sciences.")
				elif task == "Program":
					st.subheader("You can find the program by consulting the following link: https://www.international-master-biometrics-intelligent-vision.org/master-1")
			        #elif task == "Apply":
					#st.subheader("You can apply by completing the following form: https://www.international-master-biometrics-intelligent-vision.org/apply-now")
			        #elif task == "Schedule M1":
					#st.subheader("You can consult the Master 1 schedule here: https://www.international-master-biometrics-intelligent-vision.org/schedule-master-1")
			        #elif task == "Schedule M2":
					#st.subheader("You can consult the Master 2 schedule here: https://www.international-master-biometrics-intelligent-vision.org/schedule-master-2")
			        #elif task == "News":
					#st.subheader("Check out our latest events: https://www.international-master-biometrics-intelligent-vision.org/blog")
			        #elif task == "Contact":
					#st.subheader("You can find the contact of the head of our master and the administrative assistant here: https://www.international-master-biometrics-intelligent-vision.org/copy-of-contact")
			
			
			
			else:
				st.warning("Incorrect user or password, please try again")





	elif choice == "SignUp":
		st.subheader("You can register !")
		new_user = st.text_input("User")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("Congrats. You are a member now!")
			st.info("You can sign in now using your own identifiers")



if __name__ == '__main__':
	main()
