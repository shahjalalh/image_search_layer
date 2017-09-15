# Image Search Abstraction Layer #

-----

## Install
In the terminal
```

$ cd urlshortner_microservice
$ pip install -r requriements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

```

## User stories:
1. I can get the image URLs, alt text and page urls for a set of images relating to a given search string.
2. I can paginate through the responses by adding a ?offset=2 parameter to the URL.
3. I can get a list of the most recently submitted search strings.


## Example usage:
1. http://localhost:8000/api/imagesearch/lolcats?offset=2
2. http://localhost:8000/api/latest/imagesearch

Have fun... :)
