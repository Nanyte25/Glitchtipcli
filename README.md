# Glitchtipcli
Glitch-tip Error tracking software command-line tool in python click

## To run Glitchtip commandline tool local setup.

- Step 1. Clone this repository and run the following command and setup a virtual environment.

```
mkdir -p env

source env/bin/activate


```


- Step 2. Install all the python package requirements.


```
sudo pip install -r requirements.txt

```

- Step 3. Setup and `.env` file in the root of the source codes directory.

- Step 4. Generate a Gltich-tip API Token from either. Login into your Hosted or self hosted Glitch-Got:tip instances in the appropriate organization.

[Glihctip Staging](https://glitchtip.stage.devshift.net)
[Glitchtip Production](https://gltichtip.devshift.net)

-Step 5

**Goto** --> **Profile** --> **Auth Tokens**

- Click Create button and give your `Auth Token` a name and apply the appropriate permissions.

![alt text](images/auth_token.png "Glitchtip Auth Token")

- Step 6. Add the appropriate environment variable your `DOTENV` file

Example

```

PROJECT_API_KEY='Your API TOKEN Here'
STAGING_URL='Staging'
PRODUCTION_URL='Production'

```

```
python glitchtipcli.py
   _________ __       __    __  _             _________
  / ____/ (_) /______/ /_  / /_(_)___        / ____/ (_)
 / / __/ / / __/ ___/ __ \/ __/ / __ \______/ /   / / /
/ /_/ / / / /_/ /__/ / / / /_/ / /_/ /_____/ /___/ / /
\____/_/_/\__/\___/_/ /_/\__/_/ .___/      \____/_/_/
                             /_/

Usage: glitchtipcli.py [OPTIONS] COMMAND [ARGS]...

  A Glitchtip Commandline tool to query the Glitchtip Error tracking software
  API.

  Glitchtip API Documentation
  https://app.glitchtip.com/docs/#operation/api_0_organizations_teams_create

Options:
  --help  Show this message and exit.

Commands:
  create-organization  Creates a new Glitchtip Organization
  create-project       Creates a new Glitchtip Project
  create-team          Creates a new Team in Glitchtip under your...
  create-user          Creates a new Glitchtip User associated with an...
  list-memebers
  list-organizations   This returns the list of glitchtip Organization...
  list-projects        This returns the list of glitchtip projects
  list-teams           This returns the list of Glitchtip teams

```
