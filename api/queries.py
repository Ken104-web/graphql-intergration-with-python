from .models import Post

def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        payload = {
            'success': True,
            'posts': posts
        }
    except Exception as e:
        payload = {
            'success':False,
            'errors': [str(e)]
        }
    return payload