from django.test import TestCase


class Tests(TestCase):
    # Test register 
    def test_register(self):
        resp = self.client.get('/users/signup/')
        self.assertEqual(resp.status_code, 200)

    # Test login
    def test_login(self):
        resp = self.client.get('/users/login/')
        self.assertEqual(resp.status_code, 200)

    # Test sha256 hash key generation
    def test_cpf_public_key(self):
        self.assertEqual(
            'cf95d40076ab9d0731768b75b457a2147df333d0e726ceb002844bf8f4383960', 
            'cf95d40076ab9d0731768b75b457a2147df333d0e726ceb002844bf8f4383960'
            )
        self.assertNotEqual(
            '06236408726', 
            'cf95d40076ab9d0731768b75b457a2147df333d0e726ceb002844bf8f4383960'
            )

    # Test our service page
    def test_our_service(self):
        resp = self.client.get('/users/trust/service/')
        self.assertEqual(resp.status_code, 200)