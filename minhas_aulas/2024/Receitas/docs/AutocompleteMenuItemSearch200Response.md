# AutocompleteMenuItemSearch200Response



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AutocompleteProductSearch200ResponseResultsInner]**](AutocompleteProductSearch200ResponseResultsInner.md) |  | 

## Example

```python
from spoonacular.models.autocomplete_menu_item_search200_response import AutocompleteMenuItemSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteMenuItemSearch200Response from a JSON string
autocomplete_menu_item_search200_response_instance = AutocompleteMenuItemSearch200Response.from_json(json)
# print the JSON string representation of the object
print AutocompleteMenuItemSearch200Response.to_json()

# convert the object into a dict
autocomplete_menu_item_search200_response_dict = autocomplete_menu_item_search200_response_instance.to_dict()
# create an instance of AutocompleteMenuItemSearch200Response from a dict
autocomplete_menu_item_search200_response_form_dict = autocomplete_menu_item_search200_response.from_dict(autocomplete_menu_item_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


