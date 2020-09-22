from tmdb.views import HealthCheck


class TestHealthCheck:
    def test_get(self, mocker):
        expected = 'OK'
        mocker.patch('tmdb.views.HealthCheck.get', return_value=expected)
        response = HealthCheck.get()

        assert response == expected
