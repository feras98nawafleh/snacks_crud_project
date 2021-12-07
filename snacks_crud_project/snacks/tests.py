from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin", email="fero.nofal@gmail.com", password="admin"
        )
        self.snacks = Snack.objects.create(
            title="hotdog", purchaser=self.user, description="NewYork hotdog",
        )
        Snack.objects.create(
            title="pizza", purchaser=self.user, description="Italian Pizza",
        )
        Snack.objects.create(
            title="hommos", purchaser=self.user, description="Arabic Hommos",
        )


    def test_string_representation(self):
        self.assertEqual(str(self.snacks), "hotdog")

    def test_snack_content(self):
        self.assertEqual(f"{self.snacks.title}", "hotdog")
        self.assertEqual(f"{self.snacks.purchaser}", "admin")
        self.assertEqual(self.snacks.description, "NewYork hotdog")

    def test_snack1_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hommos")
        self.assertTemplateUsed(response, "snack_list.html")
    def test_snack2_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pizza")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack1_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/wrong url/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "hotdog")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack2_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="2"))
        no_response = self.client.get("/wrong url/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "pizza")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "faheta",
                "purchaser": self.user.id,
                "description": "delicious",
            }, follow=True
        )

        # self.assertRedirects(response, reverse("snack_detail", args="3"))
        self.assertContains(response, "delicious")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="5"),
            {"name": "Updated name","rating":"3","purchaser":self.user.id}
        )
        # self.assertRedirects(response, reverse("snack_detail", args="5"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)