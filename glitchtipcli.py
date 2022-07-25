import email
import os
from pprint import PrettyPrinter, pprint
from rich.console import Console
from rich.table import Table
from unicodedata import name
from wsgiref import headers
from dotenv import load_dotenv
import pyfiglet
from pyfiglet import Figlet
from tabulate import tabulate
import json
import emoji
import click
import requests


# Adding commandline auto completion


# loading the env file
load_dotenv()

__author__ = "Mark Freer CS-SRE"

# Uses dotenv ro load creds file

API_KEY = os.getenv("PROJECT_API_KEY")


# Load ASCII art for terminal

result = pyfiglet.figlet_format("Glitchtip-Cli", font="slant")
print(result)


@click.group()
def main():
    """
    A Glitchtip Commandline tool to query the Glitchtip Error tracking software API.

    Glitchtip API Documentation https://app.glitchtip.com/docs/#operation/api_0_organizations_teams_create
    """
    pass


# ================== The team listing sections============================
@main.command()
def list_teams():
    """This returns the list of Glitchtip teams"""
    url_format = "https://glitchtip.stage.devshift.net/api/0/teams/"

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url_format, headers=my_headers)

    print(tabulate(response.json(), headers="firstrow", tablefmt="fancy_grid"))
    print(
        emoji.emojize(
            "The request was a successfull, here is your Team List! :rocket:"
        )
    )


# ================== The Members listing Section =========================


@main.command()
@click.argument("id")
def list_memebers(id):

    url_format = "https://glitchtip.stage.devshit.net/api/0/teams/cssre-admins/members/{id}/"

    id = "+".join(id.split())

    id = {"id": id}

    my_headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(url_format, headers=my_headers, json=id)
    if response.status_code == 200:

        print(tabulate(response.json(), headers="keys", tablefmt="fancy_grid"))
        print(
            emoji.emojize(
                "The request was a successfull, here is the list of memebers associated wiht your Glicthtip org :rocket:"
            )
        )

    elif response.status_code == 404:

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

        print(tabulate(response.json(), headers="keys", tablefmt="fancy_grid"))
        print(
            emoji.emojize(
                "The request was a successfull, your project does exist in Glitchtip Error tracking software! :rocket:"
            )
        )

    elif response.status_code == 404:

        print("The Glitchtip project name was not found")
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

    print(tabulate(response.json(), headers="keys", tablefmt="fancy_grid"))
    print(
        emoji.emojize(
            "The request was a successful, Here is your Glitchtip organization list! :rocket:"
        )
    )


# ================== This is the Create Teams Section ====================


@main.command()
@click.argument("team")
def create_team(team):
    """Creates a new Team in Glitchtip under your organizations ID"""

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
                tablefmt="fancy_grid",
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
    """Creates a new Glitchtip Organization"""

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
                "The request was a successfull, you created a new organization! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no organization created")

    # Code here will react to failed requests


@main.command()
@click.argument("project")
def create_project(project):
    """Creates a new Glitchtip Project"""

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
                "The request was a successfull, you created a new project! :rocket:"
            )
        )

    # Code here will only run if the request is successful
    elif response.status_code == 400:
        print("Result not found!, no project was created")

    # Code here will react to failed requests

# Create superuser in Glitchtip options 

@main.command()
@click.argument("name")
@click.argument("email")
@click.argument("org_id")
def create_user(name, email, org_id):
    """Creates a new Glitchtip User associated with an organization"""

    # API DOCs url endpoint https://app.glitchtip.com/api/0/users/ or https://app.glitchtip.com/api/0/organizations/{organization_slug}/users/{id}/teams/{members_team_slug}/

    url_format = (
        "https://glitchtip.stage.devshift.net/api/0/users/"
    )

    name = "+".join(name.split())
    email = "+".join(email.split())
    ID = str(org_id)
    
    query_params = {
    "isSuperuser": True,
    "emails": [{'email':email}],
    "id": ID,
    "isActive": True,
    "hasPasswordAuth": True,
    "name": name,
    "email": email
}

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
                "The request was a successfull, you created a new project! :rocket:"
            )
        )

    # Code here will only not successful and return http 400 response
    elif response.status_code == 400:
        print(ID)
        print (response.json())
        print("Result not found!, no user was created")


if __name__ == "__main__":
    main()
