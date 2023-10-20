from fastapi import FastAPI
import facebook_scraper as fbs

app = FastAPI()


@app.get("/get_group_with_cookies/{input_string}")
def get_group_with_cookies(input_string: str):
    result = fbs.get_group_info(input_string, cookies='cookies.json')
    return result


@app.get("/get_profile_with_cookies/{input_string}")
def get_profile_with_cookies(input_string: str):
    result = fbs.get_profile(input_string, cookies='cookies.json', friends=False)
    return result


@app.get("/get_page_with_cookies/{input_string}")
def get_page_with_cookies(input_string: str):
    result = fbs.get_page_info(input_string, cookies='cookies.json')
    return result


@app.get("/get_post_with_cookies/{input_string}")
def get_post_with_cookies(input_string: str):
    result = fbs.get_posts(post_urls=iter([input_string]))
    return result

#---------------------------------------------------------------------

@app.get("/get_group/{input_string}")
def get_group(input_string: str):
    result = fbs.get_group_info(input_string)
    return result


@app.get("/get_profile/{input_string}")
def get_profile(input_string: str):
    result = fbs.get_profile(input_string, friends=False)
    return result


@app.get("/get_page/{input_string}")
def get_page(input_string: str):
    result = fbs.get_page_info(input_string)
    return result


@app.get("/get_post/{input_string}")
def get_post(input_string: str):
    result = fbs.get_posts(post_urls=iter([input_string]))
    return result
