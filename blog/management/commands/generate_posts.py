from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Blog

fake = Faker()


class Command(BaseCommand):
    help = "Add random posts to the database"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help="Numbers of posts")

    def handle(self, *args, **options):
        count = options["number"]

        for i in range(count):
            post = Blog.objects.create(
                title=fake.word().capitalize(),
                content=fake.text(500),
            )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully created posts! Post id: {post.id}")
            )
