def test_add():
    pass


# Adding a test for project list in glitchtip.
def list_projects():
    response = runner.invoke(list_projects)
    assert response.exit_code == 0
    assert "Here\'s is a list of glitchtip projects:" in response.output
    
