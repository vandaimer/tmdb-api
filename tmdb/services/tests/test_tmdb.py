from tmdb.services import TMDBService


class TestTMDBService:
    def test_get_image_url(self):
        image_hash = 'MY_IMAGE_TEST'
        expeected = f'{TMDBService.IMAGE_BASE_URL}/{image_hash}'
        result = TMDBService.get_image_url(image_hash)

        assert result == expeected

    def test_get_upcoming_movie_list(self, requests_mock):
        page = 1
        url = f'{TMDBService.MOVIE_BASE_URL}/upcoming'
        expected = {
            'results': {},
        }

        requests_mock.get(url, json=expected)
        response = TMDBService.get_upcoming_movie_list(page)

        assert response == expected

    def test_get_genre_list(self, requests_mock):
        url = TMDBService.GENRE_BASE_URL
        expected = {}

        requests_mock.get(url, json=expected)
        response = TMDBService.get_genre_list()

        assert response == expected
