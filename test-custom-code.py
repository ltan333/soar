"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'call_api_message' block
    call_api_message(container=container)

    return

def call_api_message(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("call_api_message() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationUserName","artifact:*.cef.deviceCustomString1"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import requests
    api=f"http://192.168.232.7:3334/send-msteam/alert/{container_artifact_cef_item_1}/{container_artifact_cef_item_0}"
    header = {
        'Content-Type': 'application/json; charset=UTF-8'
        }
    data={}
    rs = requests.get(api,headers=header,data=data)
    rsj=rs.json()
    print(rs.status_code)
    print(rs.content)
    print(rs.raw)
    print(rs.text)

    ################################################################################
    ## Custom Code End
    ################################################################################

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