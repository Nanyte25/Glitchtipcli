from cProfile import label
from datetime import date
import email
import os
from pprint import PrettyPrinter, pprint
from rich.console import Console
from rich.progress import track
from rich.table import Table
from unicodedata import name
from wsgiref import headers
from dotenv import load_dotenv
import pyfiglet
from pyfiglet import Figlet
from tabulate import tabulate
from yaspin import yaspin
from random import randint
import tkinter as tk
import json
import emoji
import click
import requests
import time
from tkinter import *
from PIL import Image
import ascii_magic
from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
from rich.traceback import install

# working with a framework (click, django etc), you may only be interested
# in seeing the code from your own application within the traceback.

install(suppress=[click])


# Adding command line auto completion


# loading the env file
load_dotenv()

__author__ = "Mark Freer CS-SRE"

# Uses .env and load credentials file

API_KEY = os.getenv("PROJECT_API_KEY")


# Load ASCII art for terminal

result = pyfiglet.figlet_format("Glitchtip", font="slant", width=100)

print(result)


# Markdown doc generations for Glitchtip

#console = Console()
# with open('docs/Banner.md') as md:
#    markdown = Markdown(md.read())
#    console.print(markdown)


# Create a photoimage object of the image in the path
#my_art = ascii_magic.from_image_file('images/glitchtip.png', columns=45)

# ascii_magic.to_terminal(my_art)

print(
    "GT, [bold blue]Open Source Error Tracking Software[/bold blue]!",
    ":coffee:",
    "[u]By[/u]",
    "[i]Mark Freer[/i]")


@click.group()
def main():
    """
    A Glitch-tip Command line tool to query the Glitch-tip Error tracking software API.
    """


# ================== The team listing sections============================
@main.command()
def list_teams():
    """This returns the list of glitchtip teams"""

    # https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/teams/
    # and
    # https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/members/
    # and https://app.glitchtip.com/docs/#operation/api_0_teams_members_list

    url_format = "https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/teams"

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url_format, headers=my_headers)

    with yaspin(text="Loading team data from Glitchtip", color="yellow") as spinner:
        time.sleep(2)  # time consuming code

    success = randint(0, 1)

    if success:
        spinner.ok("✅ ")
    else:
        spinner.fail("\u2638 ")

    print(tabulate(response.json(), headers="firstrow", tablefmt="fancy_grid"))
    print(
        emoji.emojize(
            "The request was a successful, here is your Team List! :rocket:"
        )
    )


# ================== The Members listing Section =========================


@main.command()
@click.argument("members")
def list_members(members):
    """This returns the list of glitchtip projects members"""

    # They API docs state to use this endpoint
    # https://app.glitchtip.com/api/0/teams/{team_pk}/members/

    url_format = "https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/members/"

    members = "+".join(members.split())

    params = {"slug": members}

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(
        url_format,
        headers=my_headers,
        json=params,
        timeout=(
            2,
            5))

    if response.status_code == 200:
        for i in track(
                range(20),
                description="Processing members data from glitchtip..."):
            time.sleep(0.1)  # Simulate work being done

        print(tabulate(response.json(), headers="keys", tablefmt="grid"))
        print(
            emoji.emojize(
                "The request was a successful, here is the list of members associated with your Glitch-tip org :rocket:"
            )
        )

    elif response.status_code == 404:
        print(response.json())

        print("The Glitchtip project name was not found")
        # Code here will react to failed requests


# ================== This is the Project listing Section =================


@main.command()
@click.argument("projectname")
def list_projects(projectname):
    """This returns the list of glitchtip projects"""

    url_format = "https://glitchtip.stage.devshift.net/api/0/projects/"

    projectname = "+".join(projectname.split())

    pro_params = {"p": projectname}

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url_format, headers=my_headers, params=pro_params)
    if response.status_code == 200:

        for i in track(
                range(10),
                description="Processing  project data from glitchtip..."):
            time.sleep(0.5)  # Simulate work being done

        print(tabulate(response.json(), headers="keys", tablefmt="grid"))
        print(
            emoji.emojize(
                "The request was a successfull, your project does exist in Glitchtip Error tracking software! :rocket:"
            )
        )

    elif response.status_code == 404:

        print("The glitchtip project name was not found")
        # Code here will react to failed requests


# ================== This is the Organizations listing Section ===========
@main.command()
@click.argument("organizations")
def list_organizations(organizations):
    """This returns the list of glitchtip Organization people are members"""

    url_format = "https://glitchtip.stage.devshift.net/api/0/organizations/"
    organizations = "+".join(organizations.split())

    org_params = {"o": organizations}

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url_format, headers=my_headers, params=org_params)

    for i in track(range(10), description="Processing data from glitchtip..."):
        time.sleep(0.1)  # Simulate work being done

    print(tabulate(response.json(), headers="keys", tablefmt="fancy_grid"))
    print(
        emoji.emojize(
            "The request was a successful, Here is your Glitchtip organization list! :rocket:"
        )
    )

# ================== This is the User listing Section ===========


@main.command()
@click.argument("users")
def list_users(users):
    """This returns the list of glitchtip specific org users"""

    url_format = "https://glitchtip.stage.devshift.net/api/0/users/"
    users = "+".join(users.split())

    users_params = {"u": users}

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(
        url_format,
        headers=my_headers,
        params=users_params)

    for i in track(range(10), description="Processing data from glitchtip..."):
        time.sleep(0.1)  # Simulate work being done

    print(tabulate(response.json(), headers="keys", tablefmt="fancy_grid"))
    print(
        emoji.emojize(
            "The request was a successful, Here is your Glitchtip Users list for your organizations! :rocket:"
        )
    )


## ================== This is the Create Teams Section =========================================##


@main.command()
@click.argument("team")
def create_team(team):
    """Creates a new Team in glitchtip under your organizations ID"""

    url_format = "https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/teams/"
    team = "+".join(team.split())

    query_params = {"slug": team}

    my_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.post(url_format, json=query_params, headers=my_headers)
    print(response.status_code)

    if response.status_code == 200:
        print("The request was a success!")
        print(
            tabulate(
                response.json(),
                headers="firstrow",
                tablefmt="grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successfull, here is your Team list! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!")

    # Code here will react to failed requests


@main.command()
@click.argument("org")
def create_organization(org):
    """Creates a new glitchtip organization"""

    # https://app.glitchtip.com/api/0/organizations/

    url_format = "https://glitchtip.stage.devshift.net/api/0/organizations/"
    org = "+".join(org.split())

    query_params = {"name": org}

    my_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.post(url_format, headers=my_headers, json=query_params)

    if response.status_code == 200:
        print("The request was a success!")
        print(
            tabulate(
                response.json(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, you created a new organization! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no organization created")

    # Code here will react to failed requests

##============================= Create Projects section ===============================###


@main.command()
@click.argument("project")
def create_project(project):
    """Creates a new glitchtip Project"""

    # https://app.glitchtip.com/api/0/projects/{project_pk}/teams/

    url_format = (
        "https://glitchtip.stage.devshift.net/api/0/projects/{project}/teams/"
    )
    project = "+".join(project.split())

    query_params = {"slug": project}

    my_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.post(url_format, headers=my_headers, json=query_params)

    if response.status_code == 200:
        print("The request was a success!")
        print(
            tabulate(
                response.json(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, you created a new project! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no project was created")

    # Code here will react to failed requests


## ================ EMAIL Validation Section ========================================= ##

def validate_email(ctx, param, value):
    if not re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            value):
        raise click.UsageError('Incorrect email address given')
    else:
        return value

## ============================== Create user section ================================ ##


# Create superuser in Glitchtip options

@main.command()
@click.option('--name', prompt='Your name please')
@click.option('--email', prompt='Your email please', callback=validate_email)
@click.option('--org_id', prompt='Your organization ID please')
def create_user(name, email, org_id):
    """Creates a new glitchtip User associated with an organization"""

    # API DOCs url endpoint https://app.glitchtip.com/api/0/users/ or https://app.glitchtip.com/api/0/organizations/{organization_slug}/users/{id}/teams/{members_team_slug}/  https://app.glitchtip.com/api/0/organizations/{organization_slug}/members/{id}/
    # 'https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/members/'+org_id

    # Not sure what the backend api call is here more investigations is needed
    # and perhaps an upstream changes.
    url_format = 'https://glitchtip.stage.devshift.net/api/0/users/'

    name = "+".join(name.split())
    email = "+".join(email.split())
    org_id = str(org_id)

    query_params = {
        "isSuperuser": False,
        "emails": [{'email': email}],
        "id": org_id,
        "isActive": True,
        "hasPasswordAuth": False,
        "name": name,
        "email": email
    }

    my_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.post(url_format, headers=my_headers, data=query_params)

    if response.status_code == 200:
        print("The request was a success!")
        print(response.json())
        print(
            tabulate(
                response.data(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful you created a new project! :rocket:"
            )
        )

    # Code here will only not successful and return http 400 response
    elif response.status_code == 400:
        print("Result not found!, no user was created")


##### Deleting a Glitchtip organization #################################


@main.command()
@click.argument("org")
def delete_organization(org):
    """Delete a glitchtip organization"""

    # The Glitchtip API state use this request type
    # https://app.glitchtip.com/api/0/organizations/{slug}/ ref:
    # https://app.glitchtip.com/docs/#operation/api_0_organizations_partial_update

    url_format = 'https://glitchtip.stage.devshift.net/api/0/organizations/' + org
    org = "+".join(org.split())

    payload = json.dumps({"slug": org})

    my_headers = {
        'Accept': 'application/json',
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.delete(url_format, headers=my_headers, data=payload)
    for i in track(
            range(10),
            description="Hold on we are deleting the Org from Glitchtip..."):
        time.sleep(0.1)  # Simulate work being done

    if response.status_code == 200:

        print("The request was a success!")
        print(
            tabulate(
                response.data(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, you deleted the glitchtip organization! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no organization was Deleted")

##---------------- Main Deleting Project Section ---------------- ###


@main.command()
@click.argument("project")
def delete_project(project):
    """Delete a glitchtip project"""

    # The Glitchtip API state using this request type
    # https://app.glitchtip.com/api/0/organizations/{slug}/ ref:
    # https://app.glitchtip.com/docs/#operation/api_0_organizations_partial_update

    url_format = 'https://glitchtip.stage.devshift.net/api/0/organizations/' + project
    project = "+".join(project.split())

    payload = json.dumps({"slug": project})

    my_headers = {
        'Accept': 'application/json',
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.delete(url_format, headers=my_headers, data=payload)
    for i in track(
            range(10),
            description="Hold on we are deleting the project from Glitchtip organization..."):
        time.sleep(0.1)  # Simulate work being done

    if response.status_code == 200:

        print("The request was a success!")
        print(
            tabulate(
                response.data(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, you deleted the glitchtip project! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no project was Deleted")

##---------------- Main Deleting Project Section ---------------- ###


@main.command()
@click.argument("id")
def delete_team(id):
    """Delete a glitchtip team"""

    # The Glitchtip API state use this request type
    # https://app.glitchtip.com/api/0/organizations/{organization_slug}/teams/{id}/
    # ref:
    # https://app.glitchtip.com/docs/#operation/api_0_organizations_partial_update

    url_format = 'https://glitchtip.stage.devshift.net/api/0/organizations/cssre-admins/teams/' + \
        id  # please update you API token organizations ID here
    id = "+".join(id.split())

    payload = json.dumps({"slug": id})

    my_headers = {
        'Accept': 'application/json',
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.delete(url_format, headers=my_headers, data=payload)
    for i in track(
            range(10),
            description="Hold on we are deleting the team from Glitchtip organization..."):
        time.sleep(0.1)  # Simulate work being done

    if response.status_code == 200:

        print("The request was a success!")
        print(
            tabulate(
                response.data(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, you deleted the glitchtip team! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no team was Deleted")


##---------------- Get the List of API token active ---------------- ###

@main.command()
@click.argument("token_id")
def list_tokens(token_id):
    """Get the list of Glitchtip API tokens"""

    # API Documentation https://app.glitchtip.com/api/0/api-tokens/{id}/

    url_format = 'https://glitchtip.stage.devshift.net/api/0/api-tokens/' + token_id
    token_id = "+".join(token_id.split())

    query_params = {
        "scopes": "org:read",
        "label": "cssre-new",
        "token": "7756d670924af8fef750ad316c61c6dbb615388a2758f7a1a738f3a56451789c",
        "id": token_id}

    my_headers = {
        "content-type": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    response = requests.get(url_format, headers=my_headers, json=query_params)

    if response.status_code == 200:
        for i in track(
                range(20),
                description="Processing  API token data from glitchtip..."):
            time.sleep(0.5)  # Simulate work being done

        print("The request was a success!")
        print(
            tabulate(
                response.json(),
                headers="firstrow",
                tablefmt="fancy_grid",
                showindex="always",
            )
        )
        print(
            emoji.emojize(
                "The request was a successful, here is the list of API tokens and there ID's ! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no API Token was found")

    # Code here will react to failed requests


if __name__ == "__main__":
    main()
