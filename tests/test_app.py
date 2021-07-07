def test_app_is_created(
    app,
):  ## o pytest faz uma injeção de dependencia, pegando o app do conftest.py
    assert app.name == "delivery.app"


def test_config_is_loaded(config):  # fixture da lib pytest-flask
    assert config["DEBUG"] is False


# def test_request_returns_404(client):  # fixture da lib pytest-flask
#     assert client.get("/").status_code == 404
