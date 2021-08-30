from flask_restx import Resource
from utils.smsUtil import SMS
from utils.appSmsUtil import APPSMS

import africastalking

ns_sms = SMS.ns_sms
ns_app_sms = APPSMS.ns_app_sms

sms_model = SMS.sms_model
app_sms_model = APPSMS.app_sms_model


@ns_sms.route('')
class SMS(Resource):
    @ns_sms.expect(sms_model)
    def post(self):
        """Use this endpoint to send a new sms"""
        data = ns_sms.payload

        africastalking.initialize(data['username'], data['api_key'])

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        code = '+254'

        recipient1 = data['recipient1']
        recipient1 = code + recipient1[1:]

        recipient2 = data['recipient2']
        recipient2 = code + recipient2[1:]

        recipient3 = data['recipient3']
        recipient3 = code + recipient3[1:]
        sender = 'ANETQUICK'

        # Use the service synchronously
        response = sms.send('Name:' + data['name'] + '. Email:' + data['email'] + '. ' + 'Phone:' + data['phone']
                            + '. Company:' + data['company'] + '. Message:' + data['message'], [recipient1, recipient2,
                                                                                                recipient3], sender)

        return response


@ns_app_sms.route('')
class APPSMS(Resource):
    @ns_app_sms.expect(app_sms_model)
    def post(self):
        """Use this endpoint to send a new sms through web"""
        data = ns_sms.payload

        africastalking.initialize(data['username'], data['api_key'])

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        code = '+254'

        recipient = data['recipient']
        recipient = code + recipient[1:]
        otp = data['otp']

        sender = 'ANETQUICK'

        # Use the service synchronously
        response = sms.send(otp, [recipient], sender)

        return response
