# ComputeGlycemicLoad200ResponseIngredientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**original** | **str** |  | 
**glycemic_index** | **float** |  | 
**glycemic_load** | **float** |  | 

## Example

```python
from spoonacular.models.compute_glycemic_load200_response_ingredients_inner import ComputeGlycemicLoad200ResponseIngredientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeGlycemicLoad200ResponseIngredientsInner from a JSON string
compute_glycemic_load200_response_ingredients_inner_instance = ComputeGlycemicLoad200ResponseIngredientsInner.from_json(json)
# print the JSON string representation of the object
print ComputeGlycemicLoad200ResponseIngredientsInner.to_json()

# convert the object into a dict
compute_glycemic_load200_response_ingredients_inner_dict = compute_glycemic_load200_response_ingredients_inner_instance.to_dict()
# create an instance of ComputeGlycemicLoad200ResponseIngredientsInner from a dict
compute_glycemic_load200_response_ingredients_inner_form_dict = compute_glycemic_load200_response_ingredients_inner.from_dict(compute_glycemic_load200_response_ingredients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


