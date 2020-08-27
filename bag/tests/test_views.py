# from django.test import TestCase, Client
# from bag.models import Order


# class TestBagVeiws(TestCase):
#     def test_get_bag_view_when_empty(self):
#         response = self.client.get('/bag/review')
#         self.assertRedirects(response, '/products/skydive-packages')

#     # def test_get_bag_view_when_bag_is_full(self):
#     #     response = self.client.get('/bag/review')
#     #     session = client.session
#     #     session['bag'] = {'0': {'id': 1, 'tandom': 1}}
#     #     session.save()
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'view_bag')

#     def test_add_to_bag_view(self):
#         response = self.client.post('/', {'name': 'test'})
#         self.assertEqual(response.status_code, 200)

#     # def test_remove_from_bag_view(self):
#     #     client = Client()
#     #     session = self.client.session
#     #     session['bag'] = {'id': 0}
#     #     session.save()
#     #     bag.id = 0
#     #     response = self.client.get(f'/bag/remove/0/')
#     #     self.assertRedirects(response, '/products/skydive-packages')
#     #     existing_items = client.session
#     #     self.assertEqual(len(existing_items), 0)


#     def test_checkout_success_view(self):
#         response = self.client.get('/checkout_success/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home/index.html')
