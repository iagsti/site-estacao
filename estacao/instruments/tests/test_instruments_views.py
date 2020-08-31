from django.test import TestCase
from django.shortcuts import resolve_url as r

from estacao.instruments.models import Instruments


class InstrumentsGetTest(TestCase):
    def setUp(self):
        self.make_instruments()
        self.resp = self.client.get(r('instruments:instruments_index'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'instruments.html')

    def test_extend_main_template(self):
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_context_has_instruments(self):
        instruments = self.resp.context['instruments']
        expected = Instruments.objects.all()
        self.assertListEqual(list(expected), list(instruments))

    def test_page_title(self):
        expected = 'Instrumentos'
        self.assertContains(self.resp, expected)

    def test_template_has_instrument_data(self):
        """Templte should render template title"""
        content = ('Instrument 1', 'Instrument text')
        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def make_instruments(self):
        instrument = dict(title='Instrument 1', text='Instrument text',
                          image='https://picsum.photos/200/300')
        Instruments.objects.create(**instrument)
        return instrument
