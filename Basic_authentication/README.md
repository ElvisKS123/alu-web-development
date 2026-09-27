# Basic_authentication

Flask API implementing Basic Authentication, task-by-task (0–11):

0. Simple base API (`models/`, `api/v1/app.py`, `/api/v1/status`)
1. `401 Unauthorized` error handler + `/api/v1/unauthorized`
2. `403 Forbidden` error handler + `/api/v1/forbidden`
3. `Auth` class template (`api/v1/auth/auth.py`)
4. `Auth.require_auth` (slash tolerant, excluded paths)
5. `Auth.authorization_header` + `before_request` filtering wired into `api/v1/app.py`
6. `BasicAuth` class (empty), selected via `AUTH_TYPE=basic_auth`
7. `BasicAuth.extract_base64_authorization_header`
8. `BasicAuth.decode_base64_authorization_header`
9. `BasicAuth.extract_user_credentials`
10. `BasicAuth.user_object_from_credentials`
11. `BasicAuth.current_user` (full Basic Auth pipeline)

## Setup

```
pip3 install -r requirements.txt
```

## Run the server

```
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

Add `AUTH_TYPE=basic_auth` to enable Basic Authentication on all routes
except `/api/v1/status/`, `/api/v1/unauthorized/`, `/api/v1/forbidden/`.

## Try it

```
curl "http://0.0.0.0:5000/api/v1/status"

curl "http://0.0.0.0:5000/api/v1/users"
# {"error": "Unauthorized"}

curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64(email:password)>"
```

## Test scripts

`main_0.py` through `main_6.py` reproduce the sample outputs from each task
in the assignment (run them with `./main_X.py` or `python3 main_X.py`).
