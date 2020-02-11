from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.utils.translation import gettext as _

class ContactViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('contact:contact_index'))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render contact_index.html template"""
        self.assertTemplateUsed(self.resp, 'contact_index.html')

    def test_template_main(self):
        """It should render main.html template"""
        self.assertTemplateUsed(self.resp, 'main.html')
    
    def test_page_title(self):
        """It should render the page title"""
        expected = _('Informações para contato')
        self.assertContains(self.resp, expected)

    def test_page_content(self):
        """Template should render page content"""
        content = [_('Informações Gerais'), _('Telefone/Fax'), _('Endereço')]

        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def make_contact(self):
        contact = dict(general_info='e-mail: test@email.com',
                        phone='(11)2222-2222', address=_('Rua Test'))

        return contact
