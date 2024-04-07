from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            last_user_message = tracker.get_last_event_for("user")
            if last_user_message:
                dispatcher.utter_message("I'm sorry, I didn't understand. Can you please rephrase your message?")
                return [UserUtteranceReverted()]


