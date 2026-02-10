import http.client
import json


GITHUB_API = 'api.github.com'
USER_AGENT = 'github_activity'


def fetch(username: str) -> list[dict]:
    '''Fetch data from the GitHub REST API'''
    conn = http.client.HTTPSConnection(
        GITHUB_API,
        timeout=5
    )
    try:
        conn.request(
            'GET',
            f'/users/{username}/events',
            headers={
                'User-Agent': USER_AGENT
            }
        )
        response = conn.getresponse()
        status = response.status
        reason = response.reason

        if status == 404:
            raise Exception(
                f'User not found: {status} {reason}'
            )

        if status >= 500:
            raise Exception(
                f'Server error: {status} {reason}'
            )

        if status != 200:
            raise Exception(
                f'Something went wrong: {status} {reason}'
            )

        try:
            data = json.loads(
                response.read().decode('utf-8')
            )
        except Exception as e:
            raise Exception(
                f'Failed to parse JSON: {e}'
            )

        return data

    except Exception as e:
        raise Exception(e)
    
    finally:
        conn.close()
