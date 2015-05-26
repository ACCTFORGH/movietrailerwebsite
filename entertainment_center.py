import media
import fresh_tomatoes as fresh

#Instantiate the movie class
BatmanvsSuperman = media.movie(title = 'Batman vs Superman',
                               poster_image_url = 'http://t0.gstatic.com/images?q=tbn:ANd9GcSb0Y7'
                                                  '-yhSfUlu85u2RcdZArCg6UYCxkNsOducy4f-RMHD9fdkl',
                               trailer_youtube_url = 'https://www.youtube.com/watch?v=xe1LrMqURuw')

AntMan = media.movie(title= 'Ant-Man',
                     poster_image_url='http://t3.gstatic.com/images?q=tbn:'
                                      'ANd9GcRvTs_PtoegY0eToOxODXT12cfV-AipOD6GftFO0ze7wbociMNB',
                     trailer_youtube_url='https://www.youtube.com/watch?v=pWdKf3MneyI')

Youth = media.movie(title='Youth',
                    poster_image_url='https://scontent.cdninstagram.com/hphotos-xaf1'
                                     '/t51.2885-15/e15/11195769_453524401465169_161925955_n.jpg',
                    trailer_youtube_url='https://www.youtube.com/watch?v=SN6mB_31uPA')

fresh.open_movies_page([BatmanvsSuperman, AntMan, Youth])