from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return []

class ActionThankYou(Action):
    def name(self) -> Text:
        return "utter_thank_you"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_thank_you")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []

class Actionexplain_crop_rotation(Action):
    def name(self) -> Text:
        return "utter_explain_crop_rotation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_explain_crop_rotation")
        return []


class Actioncrop_rotation_importance(Action):
    def name(self) -> Text:
        return "utter_crop_rotation_importance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_crop_rotation_importance")
        return []


class Actionfarming_practices_soil_erosion(Action):
    def name(self) -> Text:
        return "utter_farming_practices_soil_erosion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_farming_practices_soil_erosion")
        return []


class Actionylcv_primary_vector(Action):
    def name(self) -> Text:
        return "utter_ylcv_primary_vector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ylcv_primary_vector")
        return []


class Actionylcv_symptoms(Action):
    def name(self) -> Text:
        return "utter_ylcv_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ylcv_symptoms")
        return []


class Actionylcv_impact(Action):
    def name(self) -> Text:
        return "utter_ylcv_impact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ylcv_impact")
        return []


class Actionylcv_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_ylcv_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ylcv_preventive_measures")
        return []


class Actionylcv_treatment(Action):
    def name(self) -> Text:
        return "utter_ylcv_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ylcv_treatment")
        return []


class Actionleaf_blight_affected_plants(Action):
    def name(self) -> Text:
        return "utter_leaf_blight_affected_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_blight_affected_plants")
        return []


class Actionleaf_blight_symptoms(Action):
    def name(self) -> Text:
        return "utter_leaf_blight_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_blight_symptoms")
        return []


class Actionleaf_blight_fungal_pathogens(Action):
    def name(self) -> Text:
        return "utter_leaf_blight_fungal_pathogens"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_blight_fungal_pathogens")
        return []


class Actionleaf_blight_environmental_conditions(Action):
    def name(self) -> Text:
        return "utter_leaf_blight_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_blight_environmental_conditions")
        return []


class Actionleaf_blight_management(Action):
    def name(self) -> Text:
        return "utter_leaf_blight_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_blight_management")
        return []


class Actionleaf_mold_fungal_species(Action):
    def name(self) -> Text:
        return "utter_leaf_mold_fungal_species"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_mold_fungal_species")
        return []


class Actionleaf_mold_susceptible_plants(Action):
    def name(self) -> Text:
        return "utter_leaf_mold_susceptible_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_mold_susceptible_plants")
        return []


class Actionleaf_mold_symptoms(Action):
    def name(self) -> Text:
        return "utter_leaf_mold_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_mold_symptoms")
        return []


class Actionleaf_mold_environmental_conditions(Action):
    def name(self) -> Text:
        return "utter_leaf_mold_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_mold_environmental_conditions")
        return []


class Actionleaf_mold_management(Action):
    def name(self) -> Text:
        return "utter_leaf_mold_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_mold_management")
        return []


class Actionseptoria_leaf_spot_causal_agent(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_causal_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_causal_agent")
        return []


class Actionseptoria_leaf_spot_affected_crops(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_affected_crops"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_affected_crops")
        return []


class Actionseptoria_leaf_spot_symptoms(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_symptoms")
        return []


class Actionseptoria_leaf_spot_climate(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_climate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_climate")
        return []


class Actionseptoria_leaf_spot_effect_on_plants_yield(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_effect_on_plants_yield"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_effect_on_plants_yield")
        return []


class Actionseptoria_leaf_spot_management_cultural_practices(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_management_cultural_practices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_management_cultural_practices")
        return []


class Actionseptoria_leaf_spot_management_chemical_control(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_management_chemical_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_management_chemical_control")
        return []


class Actionseptoria_leaf_spot_prevention(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_prevention")
        return []


class Actionseptoria_leaf_spot_resistant_varieties(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_resistant_varieties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_resistant_varieties")
        return []


class Actionseptoria_leaf_spot_early_detection(Action):
    def name(self) -> Text:
        return "utter_septoria_leaf_spot_early_detection"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_septoria_leaf_spot_early_detection")
        return []


class Actionverticillium_wilt_fungal_pathogens(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_fungal_pathogens"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_fungal_pathogens")
        return []


class Actionverticillium_wilt_affected_plants(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_affected_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_affected_plants")
        return []


class Actionverticillium_wilt_symptoms(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_symptoms")
        return []


class Actionverticillium_wilt_spread(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_spread"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_spread")
        return []


class Actionverticillium_wilt_management_cultural_practices(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_management_cultural_practices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_management_cultural_practices")
        return []


class Actionverticillium_wilt_management_chemical_control(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_management_chemical_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_management_chemical_control")
        return []


class Actionverticillium_wilt_prevention(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_prevention")
        return []


class Actionverticillium_wilt_symptoms_in_tomatoes(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_symptoms_in_tomatoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_symptoms_in_tomatoes")
        return []


class Actionverticillium_wilt_genetic_resistance(Action):
    def name(self) -> Text:
        return "utter_verticillium_wilt_genetic_resistance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_verticillium_wilt_genetic_resistance")
        return []


class Actiongummosis_definition(Action):
    def name(self) -> Text:
        return "utter_gummosis_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_definition")
        return []


class Actiongummosis_affected_trees(Action):
    def name(self) -> Text:
        return "utter_gummosis_affected_trees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_affected_trees")
        return []


class Actiongummosis_common_causes(Action):
    def name(self) -> Text:
        return "utter_gummosis_common_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_common_causes")
        return []


class Actiongummosis_symptoms(Action):
    def name(self) -> Text:
        return "utter_gummosis_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_symptoms")
        return []


class Actiongummosis_management_prevention(Action):
    def name(self) -> Text:
        return "utter_gummosis_management_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_management_prevention")
        return []


class Actiongummosis_symptoms_in_citrus_trees(Action):
    def name(self) -> Text:
        return "utter_gummosis_symptoms_in_citrus_trees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_symptoms_in_citrus_trees")
        return []


class Actiongummosis_effect_on_fruit_production(Action):
    def name(self) -> Text:
        return "utter_gummosis_effect_on_fruit_production"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_effect_on_fruit_production")
        return []


class Actiongummosis_chemical_treatment(Action):
    def name(self) -> Text:
        return "utter_gummosis_chemical_treatment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_gummosis_chemical_treatment")
        return []


class Actionred_rust_fungal_pathogen(Action):
    def name(self) -> Text:
        return "utter_red_rust_fungal_pathogen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_fungal_pathogen")
        return []


class Actionred_rust_affected_crops(Action):
    def name(self) -> Text:
        return "utter_red_rust_affected_crops"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_affected_crops")
        return []


class Actionred_rust_identification(Action):
    def name(self) -> Text:
        return "utter_red_rust_identification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_identification")
        return []


class Actionred_rust_symptoms_in_wheat(Action):
    def name(self) -> Text:
        return "utter_red_rust_symptoms_in_wheat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_symptoms_in_wheat")
        return []


class Actionred_rust_environmental_conditions(Action):
    def name(self) -> Text:
        return "utter_red_rust_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_environmental_conditions")
        return []


class Actionred_rust_impact_on_yield(Action):
    def name(self) -> Text:
        return "utter_red_rust_impact_on_yield"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_impact_on_yield")
        return []


class Actionred_rust_management(Action):
    def name(self) -> Text:
        return "utter_red_rust_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_management")
        return []


class Actionred_rust_fungicides(Action):
    def name(self) -> Text:
        return "utter_red_rust_fungicides"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_fungicides")
        return []


class Actionred_rust_monitoring(Action):
    def name(self) -> Text:
        return "utter_red_rust_monitoring"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_monitoring")
        return []


class Actionred_rust_genetic_resistance(Action):
    def name(self) -> Text:
        return "utter_red_rust_genetic_resistance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_red_rust_genetic_resistance")
        return []


class Actionbrown_spot_primary_pathogen(Action):
    def name(self) -> Text:
        return "utter_brown_spot_primary_pathogen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_primary_pathogen")
        return []


class Actionbrown_spot_affected_crop(Action):
    def name(self) -> Text:
        return "utter_brown_spot_affected_crop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_affected_crop")
        return []


class Actionbrown_spot_identification(Action):
    def name(self) -> Text:
        return "utter_brown_spot_identification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_identification")
        return []


class Actionbrown_spot_symptoms_soybean(Action):
    def name(self) -> Text:
        return "utter_brown_spot_symptoms_soybean"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_symptoms_soybean")
        return []


class Actionbrown_spot_environmental_conditions(Action):
    def name(self) -> Text:
        return "utter_brown_spot_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_environmental_conditions")
        return []


class Actionbrown_spot_effect_on_yield(Action):
    def name(self) -> Text:
        return "utter_brown_spot_effect_on_yield"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_effect_on_yield")
        return []


class Actionbrown_spot_management_practices(Action):
    def name(self) -> Text:
        return "utter_brown_spot_management_practices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_management_practices")
        return []


class Actionbrown_spot_fungicides(Action):
    def name(self) -> Text:
        return "utter_brown_spot_fungicides"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_fungicides")
        return []


class Actionbrown_spot_monitoring(Action):
    def name(self) -> Text:
        return "utter_brown_spot_monitoring"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_monitoring")
        return []


class Actionbrown_spot_genetic_resistance(Action):
    def name(self) -> Text:
        return "utter_brown_spot_genetic_resistance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_brown_spot_genetic_resistance")
        return []


class Actionmaize_streak_primary_vector(Action):
    def name(self) -> Text:
        return "utter_maize_streak_primary_vector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_primary_vector")
        return []


class Actionmaize_streak_affected_crop(Action):
    def name(self) -> Text:
        return "utter_maize_streak_affected_crop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_affected_crop")
        return []


class Actionmaize_streak_symptoms(Action):
    def name(self) -> Text:
        return "utter_maize_streak_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_symptoms")
        return []


class Actionmaize_streak_family_genus(Action):
    def name(self) -> Text:
        return "utter_maize_streak_family_genus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_family_genus")
        return []


class Actionmaize_streak_transmission(Action):
    def name(self) -> Text:
        return "utter_maize_streak_transmission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_transmission")
        return []


class Actionmaize_streak_consequences(Action):
    def name(self) -> Text:
        return "utter_maize_streak_consequences"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_consequences")
        return []


class Actionmaize_streak_management(Action):
    def name(self) -> Text:
        return "utter_maize_streak_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_management")
        return []


class Actionmaize_streak_chemical_control(Action):
    def name(self) -> Text:
        return "utter_maize_streak_chemical_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_maize_streak_chemical_control")
        return []


class Actionleaf_smut_primary_pathogen(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_primary_pathogen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_primary_pathogen")
        return []


class Actionleaf_smut_affected_crops(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_affected_crops"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_affected_crops")
        return []


class Actionleaf_smut_identification(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_identification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_identification")
        return []


class Actionleaf_smut_symptoms(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_symptoms")
        return []


class Actionleaf_smut_spread(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_spread"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_spread")
        return []


class Actionleaf_smut_environmental_conditions(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_environmental_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_environmental_conditions")
        return []


class Actionleaf_smut_management(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_management")
        return []


class Actionleaf_smut_chemical_control(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_chemical_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_chemical_control")
        return []


class Actionleaf_smut_prevention(Action):
    def name(self) -> Text:
        return "utter_leaf_smut_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_smut_prevention")
        return []


class Actionspider_mites_type(Action):
    def name(self) -> Text:
        return "utter_spider_mites_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_type")
        return []


class Actionspider_mites_infested_plants(Action):
    def name(self) -> Text:
        return "utter_spider_mites_infested_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_infested_plants")
        return []


class Actionspider_mites_feeding(Action):
    def name(self) -> Text:
        return "utter_spider_mites_feeding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_feeding")
        return []


class Actionspider_mites_thrive_conditions(Action):
    def name(self) -> Text:
        return "utter_spider_mites_thrive_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_thrive_conditions")
        return []


class Actionspider_mites_signs_infestation(Action):
    def name(self) -> Text:
        return "utter_spider_mites_signs_infestation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_signs_infestation")
        return []


class Actionspider_mites_control(Action):
    def name(self) -> Text:
        return "utter_spider_mites_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_control")
        return []


class Actionspider_mites_natural_predators(Action):
    def name(self) -> Text:
        return "utter_spider_mites_natural_predators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_natural_predators")
        return []


class Actionspider_mites_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_spider_mites_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_spider_mites_preventive_measures")
        return []


class Actionleaf_miners_type(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_type")
        return []


class Actionleaf_miners_infested_plants(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_infested_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_infested_plants")
        return []


class Actionleaf_miners_damage(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_damage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_damage")
        return []


class Actionleaf_miners_signs_infestation(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_signs_infestation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_signs_infestation")
        return []


class Actionleaf_miners_management(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_management")
        return []


class Actionleaf_miners_chemical_insecticides(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_chemical_insecticides"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_chemical_insecticides")
        return []


class Actionleaf_miners_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_leaf_miners_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_miners_preventive_measures")
        return []


class Actiongrasshoppers_type(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_type")
        return []


class Actiongrasshoppers_feeding(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_feeding"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_feeding")
        return []


class Actiongrasshoppers_damage(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_damage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_damage")
        return []


class Actiongrasshoppers_active_conditions(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_active_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_active_conditions")
        return []


class Actiongrasshoppers_signs_infestation(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_signs_infestation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_signs_infestation")
        return []


class Actiongrasshoppers_management(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_management")
        return []


class Actiongrasshoppers_natural_predators(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_natural_predators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_natural_predators")
        return []


class Actiongrasshoppers_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_grasshoppers_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_grasshoppers_preventive_measures")
        return []


class Actionleaf_beetles_type(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_type")
        return []


class Actionleaf_beetles_infested_plants(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_infested_plants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_infested_plants")
        return []


class Actionleaf_beetles_damage(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_damage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_damage")
        return []


class Actionleaf_beetles_signs_infestation(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_signs_infestation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_signs_infestation")
        return []


class Actionleaf_beetles_management(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_management")
        return []


class Actionleaf_beetles_natural_predators(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_natural_predators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_natural_predators")
        return []


class Actionleaf_beetles_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_leaf_beetles_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_leaf_beetles_preventive_measures")
        return []


class Actionhispa_beetle_common_name(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_common_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_common_name")
        return []


class Actionhispa_beetle_family(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_family"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_family")
        return []


class Actionhispa_beetle_plants_attacked(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_plants_attacked"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_plants_attacked")
        return []


class Actionhispa_beetle_damage(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_damage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_damage")
        return []


class Actionhispa_beetle_identification(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_identification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_identification")
        return []


class Actionhispa_beetle_management(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_management")
        return []


class Actionhispa_beetle_natural_predators(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_natural_predators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_natural_predators")
        return []


class Actionhispa_beetle_preventive_measures(Action):
    def name(self) -> Text:
        return "utter_hispa_beetle_preventive_measures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_hispa_beetle_preventive_measures")
        return []


class Actionirrigation_methods(Action):
    def name(self) -> Text:
        return "utter_irrigation_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_irrigation_methods")
        return []


class Actionirrigation_definition(Action):
    def name(self) -> Text:
        return "utter_irrigation_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_irrigation_definition")
        return []


class Actionsurface_irrigation_working(Action):
    def name(self) -> Text:
        return "utter_surface_irrigation_working"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_surface_irrigation_working")
        return []


class Actiondrip_irrigation_definition(Action):
    def name(self) -> Text:
        return "utter_drip_irrigation_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_drip_irrigation_definition")
        return []


class Actionsprinkler_irrigation_working(Action):
    def name(self) -> Text:
        return "utter_sprinkler_irrigation_working"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_sprinkler_irrigation_working")
        return []


class Actioncenter_pivot_irrigation_definition(Action):
    def name(self) -> Text:
        return "utter_center_pivot_irrigation_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_center_pivot_irrigation_definition")
        return []


class Actionirrigation_method_choice_factors(Action):
    def name(self) -> Text:
        return "utter_irrigation_method_choice_factors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_irrigation_method_choice_factors")
        return []


class Actiondrip_irrigation_advantages(Action):
    def name(self) -> Text:
        return "utter_drip_irrigation_advantages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_drip_irrigation_advantages")
        return []


class Actionsprinkler_irrigation_disadvantages(Action):
    def name(self) -> Text:
        return "utter_sprinkler_irrigation_disadvantages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_sprinkler_irrigation_disadvantages")
        return []


class Actionsoil_health_importance(Action):
    def name(self) -> Text:
        return "utter_soil_health_importance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_soil_health_importance")
        return []


class Actionsoil_degradation_causes(Action):
    def name(self) -> Text:
        return "utter_soil_degradation_causes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_soil_degradation_causes")
        return []


class Actionerosion_impact_soil_health(Action):
    def name(self) -> Text:
        return "utter_erosion_impact_soil_health"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_erosion_impact_soil_health")
        return []


class Actionsoil_compaction_definition(Action):
    def name(self) -> Text:
        return "utter_soil_compaction_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_soil_compaction_definition")
        return []


class Actionnutrient_depletion_impact_soil_health(Action):
    def name(self) -> Text:
        return "utter_nutrient_depletion_impact_soil_health"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_nutrient_depletion_impact_soil_health")
        return []


class Actionpoor_soil_health_signs(Action):
    def name(self) -> Text:
        return "utter_poor_soil_health_signs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_poor_soil_health_signs")
        return []


class Actionimprove_soil_health_methods(Action):
    def name(self) -> Text:
        return "utter_improve_soil_health_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_improve_soil_health_methods")
        return []


class Actionsoil_organic_matter_importance(Action):
    def name(self) -> Text:
        return "utter_soil_organic_matter_importance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_soil_organic_matter_importance")
        return []


class Actionsoil_microorganisms_role(Action):
    def name(self) -> Text:
        return "utter_soil_microorganisms_role"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_soil_microorganisms_role")
        return []


class Actionorganic_farming_definition(Action):
    def name(self) -> Text:
        return "utter_organic_farming_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_organic_farming_definition")
        return []


class Actionimportance_of_organic_farming(Action):
    def name(self) -> Text:
        return "utter_importance_of_organic_farming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_importance_of_organic_farming")
        return []


class Actionorganic_farming_soil_health(Action):
    def name(self) -> Text:
        return "utter_organic_farming_soil_health"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_organic_farming_soil_health")
        return []


class Actionsustainable_practices_organic_farming(Action):
    def name(self) -> Text:
        return "utter_sustainable_practices_organic_farming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_sustainable_practices_organic_farming")
        return []


class Actionbenefits_organic_farming_environment(Action):
    def name(self) -> Text:
        return "utter_benefits_organic_farming_environment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_benefits_organic_farming_environment")
        return []


class Actionchallenges_organic_farming(Action):
    def name(self) -> Text:
        return "utter_challenges_organic_farming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_challenges_organic_farming")
        return []


class Actionregulation_organic_farming(Action):
    def name(self) -> Text:
        return "utter_regulation_organic_farming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_regulation_organic_farming")
        return []


class Actiondifference_organic_conventional_farming(Action):
    def name(self) -> Text:
        return "utter_difference_organic_conventional_farming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_difference_organic_conventional_farming")
        return []


class Actionmajor_source_food_africa(Action):
    def name(self) -> Text:
        return "utter_major_source_food_africa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_major_source_food_africa")
        return []


class Actionmajor_cassava_disease(Action):
    def name(self) -> Text:
        return "utter_major_cassava_disease"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_major_cassava_disease")
        return []


class Actioncbb_definition(Action):
    def name(self) -> Text:
        return "utter_cbb_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_definition")
        return []


class Actioncbb_symptoms(Action):
    def name(self) -> Text:
        return "utter_cbb_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_symptoms")
        return []


class Actioncbb_effects_on_cassava(Action):
    def name(self) -> Text:
        return "utter_cbb_effects_on_cassava"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_effects_on_cassava")
        return []


class Actioncbb_spread_factors(Action):
    def name(self) -> Text:
        return "utter_cbb_spread_factors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_spread_factors")
        return []


class Actioncbb_management(Action):
    def name(self) -> Text:
        return "utter_cbb_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_management")
        return []


class Actioncbb_resistant_varieties(Action):
    def name(self) -> Text:
        return "utter_cbb_resistant_varieties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_resistant_varieties")
        return []


class Actioncbb_economic_impacts(Action):
    def name(self) -> Text:
        return "utter_cbb_economic_impacts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_economic_impacts")
        return []


class Actioncbb_importance_of_control(Action):
    def name(self) -> Text:
        return "utter_cbb_importance_of_control"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cbb_importance_of_control")
        return []


class Actionsustainable_approaches_to_management(Action):
    def name(self) -> Text:
        return "utter_sustainable_approaches_to_management"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_sustainable_approaches_to_management")
        return []


class Actiondiseases_spread_by_whiteflies(Action):
    def name(self) -> Text:
        return "utter_diseases_spread_by_whiteflies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_diseases_spread_by_whiteflies")
        return []


class Actionorganic_fertilizers_definition(Action):
    def name(self) -> Text:
        return "utter_organic_fertilizers_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_organic_fertilizers_definition")
        return []


class Actionfertilizers_definition(Action):
    def name(self) -> Text:
        return "utter_fertilizers_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fertilizers_definition")
        return []


class Actionfertilizers_purpose(Action):
    def name(self) -> Text:
        return "utter_fertilizers_purpose"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fertilizers_purpose")
        return []


class Actionchemical_fertilizers_type(Action):
    def name(self) -> Text:
        return "utter_chemical_fertilizers_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_chemical_fertilizers_type")
        return []


class Actionpest_management_definition(Action):
    def name(self) -> Text:
        return "utter_pest_management_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_pest_management_definition")
        return []


class Actionpest_management_methods(Action):
    def name(self) -> Text:
        return "utter_pest_management_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_pest_management_methods")
        return []


class Actionbiological_control_definition(Action):
    def name(self) -> Text:
        return "utter_biological_control_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_biological_control_definition")
        return []


class Actioncultural_control_definition(Action):
    def name(self) -> Text:
        return "utter_cultural_control_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cultural_control_definition")
        return []


class Actionchemical_control_definition(Action):
    def name(self) -> Text:
        return "utter_chemical_control_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_chemical_control_definition")
        return []


class Actionphysical_control_definition(Action):
    def name(self) -> Text:
        return "utter_physical_control_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_physical_control_definition")
        return []


class Actionipm_definition(Action):
    def name(self) -> Text:
        return "utter_ipm_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter