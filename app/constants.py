"""Static strings and configuration values used across the app."""

APP_NAME = "MLH Fellow"
APP_DESCRIPTION = "My Personal Portfolio"

# Each entry drives both the navbar rendering and the route's page title.
# 'key' must match the active_page value passed from the route.
NAV_LINKS = [
    {"label": "Home",       "href": "/",           "key": "home"},
    {"label": "About",      "href": "/about",       "key": "about"},
    {"label": "Experience", "href": "/experience",  "key": "experience"},
    {"label": "Projects",   "href": "/projects",    "key": "projects"},
    {"label": "Hobbies",    "href": "/hobbies",     "key": "hobbies"},
]

PAGE_TITLES = {
    "home":       APP_NAME,
    "about":      "About",
    "experience": "Experience",
    "projects":   "Projects",
    "hobbies":    "Hobbies",
}

HOBBIES = [
    {
        "name": "Hobby One",
        "description": "A short description of this hobby and why you enjoy it.",
        "image": "img/hobby1.jpg",
    },
    {
        "name": "Hobby Two",
        "description": "A short description of this hobby and why you enjoy it.",
        "image": "img/hobby2.jpg",
    },
    {
        "name": "Hobby Three",
        "description": "A short description of this hobby and why you enjoy it.",
        "image": "img/hobby3.jpg",
    },
]
