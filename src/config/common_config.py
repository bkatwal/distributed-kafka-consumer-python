import os
import uuid

CLIENT_ID = str(uuid.uuid4())
SECURITY_PROTOCOL = os.environ.get('security_protocol', 'PLAINTEXT')
AUTH_MECHANISM = os.environ.get('auth_mechanism')
