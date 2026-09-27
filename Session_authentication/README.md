# Session_authentication

Builds on `0x06. Basic authentication`, adding cookie-based Session
Authentication. Tasks 0–7:

0. `GET /api/v1/users/me` returns the authenticated user
   (`request.current_user` set in `before_request`)
1. `SessionAuth` class (empty), selectable via `AUTH_TYPE=session_auth`
2. `SessionAuth.create_session` — in-memory `user_id_by_session_id` store
3. `SessionAuth.user_id_for_session_id`
4. `Auth.session_cookie` — reads the `SESSION_NAME` cookie from a request
5. `before_request` updated: `/api/v1/auth_session/login/` excluded,
   401 only when both the auth header *and* the session cookie are missing
6. `SessionAuth.current_user` — resolves a `User` from the session cookie
7. `POST /api/v1/auth_session/login` — email/password login that creates
   a session and sets the cookie (`api/v1/views/session_auth.py`)

## Setup

```
pip3 install -r requirements.txt
```

## Run the server

```
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
```

(Use `AUTH_TYPE=basic_auth` instead to fall back to Basic Authentication.)

## Try it

```
# Log in, get a session cookie back
curl "http://0.0.0.0:5000/api/v1/auth_session/login" \
     -d "email=bob@hbtn.io" -d "password=H0lbertonSchool98!" -c cookies.txt

# Use the cookie to access a protected route
curl "http://0.0.0.0:5000/api/v1/users/me" -b cookies.txt
```

## Test scripts

`main_0.py` through `main_4.py` reproduce the sample outputs from each task
in the assignment (`./main_X.py` or `python3 main_X.py`).
