import unittest
from app.models import Movie
from app.models import Review,User
from app import db

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993)
        self.user_Melo = User(username = 'Melo',password = 'melo', email = 'melo@gmail.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_melo )


    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_Melo)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)

    def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)