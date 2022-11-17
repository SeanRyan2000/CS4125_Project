from model.Movie import NewReleaseMovie, ChildrensMovie, StandardMovie

class MovieFactory:

    def createMovie(self, request):

        movie = None

        if request.get('type') == 'NewReleaseMovie':
            movie = NewReleaseMovie.NewReleaseMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))
        elif request.get('type') == 'ChildrensMovie':
            movie = ChildrensMovie.ChildrensMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))
        elif request.get('type') == 'StandardMovie':
            movie = StandardMovie.StandardMovie(request.get('title'), request.get('movie_length'), request.get('tickets'))

        return movie
