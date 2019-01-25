from django.test import TestCase
from django.shortcuts import resolve_url


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('core:home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET / must use index.html"""
        self.assertTemplateUsed(self.response, 'core/index.html')

    def test_html(self):
        """HTML must contain input tags"""
        html_tags = (
            ('<form', 1),
            ('<input', 2),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for tag, amount in html_tags:
            with self.subTest():
                self.assertContains(self.response, tag, amount)

    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_index_link(self):
        expected = 'href="{}"'.format(resolve_url('core:index'))
        self.assertContains(self.response, expected)
        #
        # def test_speakers(self):
        #     """Must show keynote speakers"""
        #     contents = ['Grace Hopper',
        #                 'http://hbn.link/hopper-pic',
        #                 'href="{}"'.format(resolve_url('speaker_detail', slug='grace-hopper')),
        #                 'Alan Turing',
        #                 'href="{}"'.format(resolve_url('speaker_detail', slug='alan-turing')),
        #                 'http://hbn.link/turing-pic']
        #     for expected in contents:
        #         with self.subTest():
        #             self.assertContains(self.response, expected)
        #
        # def test_speakers_link(self):
        #     expected = 'href="{}#speakers"'.format(resolve_url('home'))
        #     self.assertContains(self.response, expected)
        #
        # def test_talks_link(self):
        #     expected = 'href="{}"'.format(resolve_url('talk_list'))
        #     self.assertContains(self.response, expected)
