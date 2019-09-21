from tmdb.views import Movie


class TestMovie:
    def test_get_upcoming_list_with_errors(self, mocker):
        mocker.patch('tmdb.services.tmdb.TMDBService.get_upcoming_movie_list', return_value={'errors': 'Error'})

        page = 1
        expected = { 'items': [], 'page': 1, 'total_pages': 1, 'total_results': 0 }

        result = Movie.get_upcoming_list(page)

        assert result == expected

    def test_get_upcoming_list_without_errors(self, mocker):
        page = 1
        movie = {'key': 'value'}
        mock_service = {
            'results':[movie],
            'page': page,
            'total_pages': 1,
            'total_results': 0,
        }
        mocker.patch('tmdb.services.tmdb.TMDBService.get_upcoming_movie_list', return_value=mock_service)
        mocker.patch('tmdb.views.movie.Movie.build_movie', side_effect=lambda x: x)

        expected = {'items': [movie], 'page': 1, 'total_pages': 1, 'total_results': 0}

        result = Movie.get_upcoming_list(page)

        assert result == expected

    def test_build_movie_with_all_attr(self, mocker):
        genres = {1: 'Action', 2: 'Drama'}
        mocker.patch('tmdb.views.genre.Genre.get_genre_by_id', side_effect=lambda x: genres[x])
        mocker.patch('tmdb.services.tmdb.TMDBService.get_image_url', side_effect=lambda x: x)
        poster = 'poster'
        backdrop = 'backdrop'

        movie = {
            'poster_path': poster,
            'backdrop_path': backdrop,
            'genre_ids': genres.keys(),
            'title': '',
            'release_date': '',
            'overview': '',
        }
        expected = {
            'poster': poster,
            'backdrop': backdrop,
            'genres': list(genres.values()),
            'title': '',
            'release_date': '',
            'overview': '',
        }

        result = Movie.build_movie(movie)

        assert result == expected

    def test_build_movie_without_poster_attr(self, mocker):
        mocker.patch('tmdb.services.tmdb.TMDBService.get_image_url', side_effect=lambda x: x)
        backdrop = 'backdrop'

        movie = {
            'backdrop_path': backdrop,
            'genre_ids': [],
            'poster_path': '',
            'title': '',
            'release_date': '',
            'overview': '',
        }

        result = Movie.build_movie(movie)

        assert result.get('poster') is None

    def test_build_movie_without_backdrop_attr(self, mocker):
        mocker.patch('tmdb.services.tmdb.TMDBService.get_image_url', side_effect=lambda x: x)
        poster = 'poster'

        movie = {
            'poster_path': poster,
            'genre_ids': [],
            'backdrop_path': '',
            'title': '',
            'release_date': '',
            'overview': '',
        }

        result = Movie.build_movie(movie)

        assert result.get('backdrop') is None
