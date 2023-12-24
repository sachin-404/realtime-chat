# Django Chat Room

Welcome to the ChatRoom application! This project aims to provide a simple and efficient solution for creating real-time chat rooms accessible through a public URL. The application is built using Python, Django, Flask, and real-time duplex sockets (django-channels) for seamless communication. 

Users can easily create and join chat rooms through a public URL. The application leverages real-time duplex sockets to facilitate instant communication among users. Messages are sent and received in real-time, creating a dynamic and engaging chat experience.


## Getting Started

1. Clone the repository: `https://github.com/sachin-404/realtime-chat`
2. Set up your virtual environment: `python -m venv venv ` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`


## Preview

  ### Rooms
  ![Screenshot from 2023-12-24 14-16-54](https://github.com/sachin-404/realtime-chat/assets/96824004/4bc4aada-6879-4d4f-a1ca-51b794f84278)

  ### Chat
  ![Screenshot from 2023-12-24 16-25-00](https://github.com/sachin-404/realtime-chat/assets/96824004/ec1f5aa2-a653-420a-9530-1ed24c577de5)

  It uses NLTK to calculate the Figures of Speech used in the sentence every time a user sends a chat.
  For example:
  ```
  Sentence: Sure!! What is it??
  Figure of Speech: {Sure: JJ, What: WP, is: VBZ, it: PRP}

  Meaning of the tags:
  {
      'JJ': adjective,
      'WP': pronoun,
      'VBZ': verb, gerund,
      'PRP': personal pronoun
  }
  ```


  
