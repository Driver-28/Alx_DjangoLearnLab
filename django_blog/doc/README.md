# Features
- Create, read, update, and delete blog posts.
- Only authenticated users can create posts.
- Only the post author can edit or delete their post.
- All posts are visible to everyone.

## URLs
- `/` → List all posts
- `/post/new/` → Create a post (Login required)
- `/post/<id>/` → View post details
- `/post/<id>/edit/` → Edit a post (Author only)
- `/post/<id>/delete/` → Delete a post (Author only)

## Setup
1. Clone the repository.
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`
4. Start the server: `python manage.py runserver`

## Comment System

### Features:
- Users can comment on blog posts.
- Only authenticated users can add comments.
- Only the comment author can edit or delete their comment.

### URL Structure:
- Create Comment: `/posts/<post_id>/comments/new/`
- Edit Comment: `/comments/<comment_id>/edit/`
- Delete Comment: `/comments/<comment_id>/delete/`

