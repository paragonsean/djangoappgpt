import os
import time
import requests
import dotenv

dotenv.load_dotenv(verbose=True)

def fetch_all_transcripts():
    """
    Fetches all transcripts from the server.

    Returns:
        list: A list of transcripts.
    """
    try:
        response = requests.get(f"https://{os.getenv('SERVER')}/all_transcripts")
        return response.json().get('transcripts', [])
    except requests.RequestException as e:
        print(f"Error fetching call list: {str(e)}")
        return []

def start_call(phone_number, system_message, initial_message):
    """
    Starts a call with the specified phone number, system message, and initial message.

    Args:
        phone_number (str): The phone number to call.
        system_message (str): The system message to play during the call.
        initial_message (str): The initial message to send during the call.

    Returns:
        str: The call SID if the call was successfully started, None otherwise.
    """
    try:
        response = requests.post(f"https://{os.getenv('SERVER')}/start_call", json={
            "to_number": phone_number,
            "system_message": system_message,
            "initial_message": initial_message
        }, timeout=10)
        call_data = response.json()
        return call_data.get('call_sid')
    except requests.RequestException as e:
        print(f"Error: {str(e)}")
        return None

def end_call(call_sid):
    """
    Ends a call by sending a POST request to the server.

    Parameters:
    - call_sid (str): The unique identifier of the call.

    Returns:
    - bool: True if the call was successfully ended, False otherwise.
    """
    try:
        response = requests.post(f"https://{os.getenv('SERVER')}/end_call", json={"call_sid": call_sid})
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error ending call: {str(e)}")
        return False

def fetch_recording_info(call_sid):
    """
    Fetches the recording information for a given call SID.

    Args:
        call_sid (str): The SID of the call.

    Returns:
        dict or None: A dictionary containing the recording URL and duration if the recording exists, 
                      otherwise None.

    Raises:
        requests.RequestException: If there is an error fetching the recording information.
    """
        # Code to fetch recording information
    try:
        response = requests.get(f"https://{os.getenv('SERVER')}/call_recording/{call_sid}")
        if media_url := response.json().get('recording_url'):
            media_response = requests.get(media_url)
            if media_response.status_code == 200:
                media_data = media_response.json()
                return {
                    'url': f"{media_data.get('media_url')}.mp3",
                    'duration': media_data.get('duration', 0)
                }
    except requests.RequestException as e:
        print(f"Error fetching recording info: {str(e)}")
    return None

def update_call_info(call_sid):
    """
    Update call information based on the given call SID.
    Parameters:
    - call_sid (str): The call SID to retrieve information for.
    Returns:
    - tuple: A tuple containing a boolean value indicating the success of the update and the updated call information.
             If the update is successful, the boolean value is True and the call information is returned.
             If the update fails, the boolean value is False and the reason for the failure is returned.
    Raises:
    - requests.RequestException: If there is an error while making the API requests.
    """
        # Code implementation
    try:
        status = requests.get(f"https://{os.getenv('SERVER')}/call_status/{call_sid}").json().get('status')
        if status not in ['in-progress', 'ringing']:
            return False, status
        
        transcript_data = requests.get(f"https://{os.getenv('SERVER')}/transcript/{call_sid}").json()
        if transcript_data.get('call_ended', False):
            return False, transcript_data.get('final_status', 'Unknown')
        
        return True, transcript_data.get('transcript', [])
    except requests.RequestException as e:
        print(f"Error updating call info: {str(e)}")
        return False, None
    
    

    


    
    