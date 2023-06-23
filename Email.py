"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'scan_url' block
    scan_url(container=container)

    return

def scan_url(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("scan_url() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.id"])

    parameters = []

    # build parameters list for 'scan_url' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "url": container_artifact_item[0],
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("detonate url", parameters=parameters, name="scan_url", assets=["scan link"], callback=decision_1)

    return


def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["scan_url:action_result.status", "==", "success"]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        get_report_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    send_message_fail(action=action, success=success, container=container, results=results, handle=handle)

    return


def get_report_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_report_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    scan_url_result_data = phantom.collect2(container=container, datapath=["scan_url:action_result.data.*.scan_id","scan_url:action_result.parameter.context.artifact_id"], action_results=results)

    parameters = []

    # build parameters list for 'get_report_1' call
    for scan_url_result_item in scan_url_result_data:
        if scan_url_result_item[0] is not None:
            parameters.append({
                "report_type": "file",
                "scan_id": scan_url_result_item[0],
                "context": {'artifact_id': scan_url_result_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get report", parameters=parameters, name="get_report_1", assets=["scan link"], callback=send_message_info)

    return


def send_message_fail(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_message_fail() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    headers_formatted_string = phantom.format(
        container=container,
        template="""{\n\"accept\": \"application/json\"\n}""",
        parameters=[])
    location_formatted_string = phantom.format(
        container=container,
        template="""/send-msteam/email-alert/fail-scan/{0}/anlt/{1}""",
        parameters=[
            "artifact:*.cef.sourceUserName",
            "artifact:*.cef.requestURL"
        ])

    parameters = []

    if location_formatted_string is not None:
        parameters.append({
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

    phantom.act("get data", parameters=parameters, name="send_message_fail", assets=["http"])

    return


def send_message_info(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_message_info() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    headers_formatted_string = phantom.format(
        container=container,
        template="""{\n\"Content-Type\": \"application/json\";\n\"accept\": \"application/json\"\n}""",
        parameters=[])
    body_formatted_string = phantom.format(
        container=container,
        template="""{\n  \"sender\": \"anlt\",\n  \"receiver\": \"khoana\",\n  \"url\": \"https://siuvipprono1siucapvutruthienhahemattroi.com.vn.net/asf/asf/asf/asfsaf/?123.asf\"\n}""",
        parameters=[])
    location_formatted_string = phantom.format(
        container=container,
        template="""/send-msteam/email-alert/fail-scan""",
        parameters=[])

    parameters = []

    if body_formatted_string is not None and location_formatted_string is not None:
        parameters.append({
            "headers": headers_formatted_string,
            "body": body_formatted_string,
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

    phantom.act("post data", parameters=parameters, name="send_message_info", assets=["http"])

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