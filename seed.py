from api.models import Post
from api import db, app

with app.app_context():
    Post.query.delete()

    titles = [
        'A new morning',
        'A wonderful morning'
    ]
    descriptions = [
        'A new morning details',
        'A wonderful morning details',
    ]
    posts = []
    for i in range(2):
        print('****Hello*****')
        post = Post(
            title = titles[i],
            description = descriptions[i],
        )
        posts.append(post)
    db.session.add_all(posts)
    db.session.commit()

