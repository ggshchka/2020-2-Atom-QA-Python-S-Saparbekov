import pytest


@pytest.mark.API
class TestApi:

    def test_login(self, client):
        resp = client.login()
        assert resp.status_code == 200

    def test_create_and_delete_segment(self, client):
        name = 'new_segment'
        client.login()
        cre_resp = client.create_segment(name)
        assert cre_resp['name'] == name
        id = client.get_segment_id(cre_resp)
        del_resp = client.delete_segment(id)
        assert del_resp.status_code == 204
        emp_resp = client._request(
            method='GET',
            location='api/v2/coverage/segment.json',
            params={'id': id},
            json=True
        )
        assert emp_resp['items'][0]['status'] == 'not found'
