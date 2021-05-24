# urlshorter
Simple REST API. Django Rest Framework.
___
Python 3.7.5
Django 3.2.3
Django REST Framework 3.12.4
___

Link
GET /api/links
GET /api/links/{id}
GET /api/links/?long_url=__
GET /api/links/?short_url=__
POST /api/links
PUT /api/links/{id}/
PATCH /api/links/{id}/
DELETE /api/links/{id}/
*with slash at the end

Redirection from short_url to long_url
GET /{short_url}
