from behave import given, when, then
from time import time
import json
from sdk import api
import data

print('Feature: signup\n')
print('Scenario: Successfully create an account\n')


@given("I am a new user")
def step_impl(context):
    context.email = "test.{}@mail.com".format(int(time()))
    body = {
        "first_name": "test",
        "middle_name": "",
        "last_name": "user",
        "email": context.email,
        "state": "ca"
    }

    context.request_body = body
    print('Given I am a new user: pass\n')


@when("I fill signup form")
def step_impl(context):
    response = api.save_sender(context.request_body)
    context.response = response
    context.content = json.loads(response.text)
    print('When I fill signup form: pass\n')


@then("User account should be created")
def step_impl(context):
    content = context.content
    assert context.response.status_code == 200, 'status code does not match'
    assert content['status'] == 'UNVERIFIED', 'KYC status is not UNVERIFIED'
    assert content['email'] == context.email, 'Email does not matches'
    data.sender_id = content['id']
    print('Then User account should be created: pass\n')
