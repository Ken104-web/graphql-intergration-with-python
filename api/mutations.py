from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from api import db
from .models import Post

@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        # today = date.today()
        today = datetime(2023, 3, 3, 10, 10, 10)
        post = Post(
            title=title, description=description, created_at=today
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
              "success": False,
                "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload