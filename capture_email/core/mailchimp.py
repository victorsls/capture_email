from mailchimp3 import MailChimp
from dateutil import parser
from django.conf import settings


class APIMailChimp(object):
    client = MailChimp(mc_api=settings.MAILCHIMP_KEY, mc_user=settings.MAILCHIMP_USER)

    def add_email(self, list_id, email):
        return self.client.lists.members.create(list_id, {
            'email_address': email,
            'status': 'subscribed',
        })

    def add_tag(self, list_id, segment_id):
        members = self.client.lists.members.all(list_id=list_id, get_all=True).get('members')
        members_to_add = []
        for member in members:
            timestamp_opt = parser.parse(member.get('timestamp_opt'))
            if timestamp_opt.second % 2 == 0:
                members_to_add.append(member.get('email_address'))
        return self.client.lists.segments.update_members(
            list_id=list_id,
            segment_id=segment_id,
            data={
                'members_to_add': members_to_add
            }
        )
