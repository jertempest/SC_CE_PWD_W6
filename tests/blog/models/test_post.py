from model_bakery import baker
import pytest

from blog.models import Post

pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_those_with_published_status():
    published = baker.make('blog.Post', status= Post.PUBLISHED)
    
    baker.make('blog.Post', status=Post.DRAFT)
    
    expected = [published]
    
    result = list(Post.objects.published())
    
    assert result == expected
    