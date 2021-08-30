from flask_restx import Namespace, fields


class APPSMS:
    ns_app_sms = Namespace('app_sms', description='Send message to a single user')
    app_sms_model = ns_app_sms.model('APPSMS', {
        'username': fields.String(required=True, description='Your africastalking username'),
        'api_key': fields.String(required=True, description='Your api key'),
        'otp': fields.String(required=True, description='otp'),
        'recipient': fields.String(required=True, description='recipient 1')
    })
