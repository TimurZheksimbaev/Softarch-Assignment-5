#!/usr/bin/env python3
import click
import requests
import json
import os

API_URL = "http://127.0.0.1:8000"
USER_FILE = "user_info.json"


def save_user_info(user_info):
    with open(USER_FILE, "w") as f:
        json.dump(user_info, f)


def load_user_info():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return None


@click.command(name="register-user")
@click.option("--username", prompt="Username", help="Username for registration")
def register_user(username):
    payload = {"username": username}
    response = requests.post(f"{API_URL}/users/", json=payload)

    if response.status_code == 200:
        user_info = response.json()
        save_user_info(user_info)
        click.echo(f"User '{username}' registered successfully! ID saved locally.")
    elif response.status_code == 400:
        click.echo(f"Error: {response.json()['detail']}")
    else:
        click.echo("Failed to register user. Try again.")


def is_user_registered(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    return response.status_code == 200


@click.command(name="write-message")
@click.option("--content", prompt="Message", help="Content of the message")
def post_message(content):
    user_info = load_user_info()
    user_id = user_info["id"]

    if not is_user_registered(user_id):
        click.echo("Error: User not found. Please register a user first.")
        return


    payload = {"user_id": user_id, "content": content}
    response = requests.post(f"{API_URL}/messages/", json=payload)

    if response.status_code == 200:
        click.echo("Message posted successfully!")
    elif response.status_code == 400:
        click.echo(f"Error: {response.json()['detail']}")
    else:
        click.echo("Failed to post message. Try again.")


@click.command(name="get-messages")
def view_feed():
    response = requests.get(f"{API_URL}/messages/")

    if response.status_code == 200:
        messages = response.json()
        if messages:
            click.echo("Last 10 Messages:")
            for message in messages:
                click.echo(f"Message ID {message['id']}: {message['content']}")
        else:
            click.echo("No messages available.")
    else:
        click.echo("Failed to fetch messages.")


@click.command(name="like-message")
@click.option("--message-id", prompt="Message ID", help="ID of the message to like")
def like_message(message_id):
    user_info = load_user_info()

    if not user_info:
        click.echo("Error: No registered user found. Please register a user first.")
        return

    user_id = user_info["id"]


    payload = {"user_id": user_id, "message_id": int(message_id)}
    response = requests.post(f"{API_URL}/likes/", json=payload)

    if response.status_code == 200:
        click.echo("Message liked successfully!")
    elif response.status_code == 404:
        click.echo(f"Error: {response.json()['detail']}")
    else:
        click.echo("Failed to like message. Try again.")


@click.group()
def cli():
    pass


cli.add_command(register_user)
cli.add_command(post_message)
cli.add_command(view_feed)
cli.add_command(like_message)

if __name__ == "__main__":
    cli()
