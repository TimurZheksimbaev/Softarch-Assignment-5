# Twitter-like Application

Team Members
1. Amir Gubaidullin - am.gubaidullin@innopolis.university 
2. Timur Zheksimbaev - t.zheksimbaev@innopolis.university 
3. Shamil Kashapov - s.kashapov@innopolis.university 
4. Evgeny Spiridonov - e.spiridonov@innopolis.university 
5. Kirill Arkhipov - k.arkhipov@innopolis.university



This is a simple Twitter-like system where users can:
- Register with a username.
- Post short messages (up to 400 characters).
- View the latest 10 messages (feed).
- Like messages.

## Features
- **User Registration**: Users register with a username (no password is required).
- **Message Posting**: Registered users can post short messages.
- **Feed**: The public feed displays the latest 10 messages.
- **Like Messages**: Users can like messages posted by others.

The application is built using `FastAPI` for the backend, with a simple CLI using `Click` python library for interaction.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/TimurZheksimbaev/Softarch-Assignment-5.git
    cd Softarch-Assignment-5
    ```
2. Run Docker
   ```bash
   docker build -t twitter-softarch .
   docker run -p 8000:8000 twitter-softarch
   ```

## Usage 

- To register a new user, run:

    ```bash
    twitter-cli register-user
    ```
  
- To write message, run: 
   ```bash
    twitter-cli write-message
    ```
- To view the feed, run:

    ```bash
    twitter-cli get-messages
    ```
- To like a message, run:

    ```bash
    twitter-cli like-message
    ```

