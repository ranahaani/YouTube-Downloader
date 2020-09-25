from django.test import TestCase, RequestFactory
from endPoint import views
from endPoint.models import Employee


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.employee = {
            'eid': 'second',
            'ename': 'Hamza',
            'eemail': 'haaandddi@gmail.com',
            'econtact': '+9230442556'}

    def testCreate(self):
        response = self.factory.post('/create/', data=self.employee)

        self.assertEqual(response.status_code, 200)

    def testDelete(self):
        request = self.factory.get('/delete/')
        response = views.delete(request, 15)
        self.assertIn(response, "Deleted")

    def testUpdate(self):
        request = self.factory.get('/update/')
        request.POST = self.employee
        response = views.update(request, 18)
        self.assertIn(response, "Updated")
