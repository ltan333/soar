"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'post_data_1' block
    post_data_1(container=container)

    return

def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    body_formatted_string = phantom.format(
        container=container,
        template="""{\n  \"sender\": \"string\",\n  \"receiver\": \"string\",\n  \"url\": \"\n        https://siuvipprono1siucapvutruthienhahemattroi.com.vn.net/asf/asf/asf/asfsaf/?123.asf\"\n}""",
        parameters=[])
    headers_formatted_string = phantom.format(
        container=container,
        template="""{\n\"accept\": \"application/json\"\n}""",
        parameters=[])
    location_formatted_string = phantom.format(
        container=container,
        template="""/send-msteam/email-alert/fail-scan""",
        parameters=[])

    parameters = []

    if body_formatted_string is not None and location_formatted_string is not None:
        parameters.append({
            "body": body_formatted_string,
            "headers": headers_formatted_string,
            "location": location_formatted_string,
            "verify_certificate": False,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["http"])

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return