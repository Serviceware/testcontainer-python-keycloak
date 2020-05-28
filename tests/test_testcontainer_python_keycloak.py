from testcontainer_python_keycloak import KeycloakContainer


def test_keycloak_token():

    config = KeycloakContainer()

    with config as container:
        # creates a realm with a user with same name
        result = container.create_realm("foo")
        assert result["url"] is not None

        # get a access token
        token = container.get_access_token(realm="foo", username="foo", password="test")
        assert token is not None
