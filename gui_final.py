import ipywidgets as widgets
from IPython.display import display
import joblib

# Load the trained model (assuming it's saved as 'car_price_model.pkl')
model = joblib.load('car_price_model.pkl')  # Update the path if necessary

# Define input widgets
present_price_input = widgets.FloatText(description="Present Price (in lakhs)")
mileage_input = widgets.IntText(description="Kms Driven")
engine_volume_input = widgets.FloatText(description="Engine Volume")
year_input = widgets.IntText(description="Year")
bmw_input = widgets.Dropdown(options=['True','False'], description="Brand: BMW")
merc_input = widgets.Dropdown(options=['True','False'], description="Brand: Mercedes-Benz")
mits_input = widgets.Dropdown(options=['True','False'], description="Brand: Mitsubishi")
renault_input = widgets.Dropdown(options=['True','False'], description="Brand: Renault")
toyota_input = widgets.Dropdown(options=['True','False'], description="Brand: Toyota")
volks_input = widgets.Dropdown(options=['True','False'], description="Brand: Volkswagen")

body_hatch_input = widgets.Dropdown(options=['True','False'], description="Body: Hatch")
body_other_input = widgets.Dropdown(options=['True','False'], description="Body: Other")
body_sedan_input = widgets.Dropdown(options=['True','False'], description="Body: Sedan")
body_vagon_input = widgets.Dropdown(options=['True','False'], description="Body: Wagon")
body_van_input = widgets.Dropdown(options=['True','False'], description="Body: Van")

gas_input = widgets.Dropdown(options=['True','False'], description="Engine-type: Gas")
other_input = widgets.Dropdown(options=['True','False'], description="Engine-type: Other")
petrol_input = widgets.Dropdown(options=['True','False'], description="Engine-type: Petrol")

registration_input =widgets.Dropdown(options=['Yes'], description="Registration")

# Display for output
output = widgets.Output()

# Prediction function
def predict_price(b):
    with output:
        output.clear_output()
        try:
            # Gather inputs

            present_price = present_price_input.value
            mileage=mileage_input.value
            engine_volume=engine_volume_input.value
            year = year_input.value
            bmw=bmw_input.value
            merc=merc_input.value
            mits=mits_input.value
            ren=renault_input.value
            toyota=toyota_input.value
            volks=volks_input.value

            hatch=body_hatch_input.value
            other=body_other_input.value
            sedan=body_sedan_input.value
            vagon=body_vagon_input.value
            van=body_van_input.value

            gas=gas_input.value
            other2=other_input.value
            petrol=petrol_input.value
            regs=registration_input.value
        

            # Map categorical variables to model-compatible encoding
            bmw_map = {'False': 0, 'True': 1}
            merc_map = {'False': 0, 'True': 1}
            mits_map = {'False': 0, 'True': 1}
            ren_map = {'False': 0, 'True': 1}
            toyota_map = {'False': 0, 'True': 1}
            volks_map = {'False': 0, 'True': 1}

            map1 = {'False': 0, 'True': 1}
            map2 = {'False': 0, 'True': 1}
            map3 = {'False': 0, 'True': 1}
            map4 = {'False': 0, 'True': 1}
            map5 = {'False': 0, 'True': 1}
            map6 = {'False': 0, 'True': 1}
            map7 = {'False': 0, 'True': 1}
            map8 = {'False': 0, 'True': 1}

            map9 = {'Yes': 1}
        
            
            
            bmw_encoded = bmw_map[bmw]
            merc_encoded = merc_map[merc]
            mits_encoded = mits_map[mits]
            ren_encoded = ren_map[ren]
            toyota_encoded = toyota_map[toyota]
            volks_encoded = volks_map[volks]
            

            map1_encoded = map1[hatch]
            map2_encoded = map2[other]
            map3_encoded = map3[sedan]
            map4_encoded = map4[vagon]
            map5_encoded = map5[van]
            map6_encoded = map6[gas]
            map7_encoded = map7[other2]
            map8_encoded = map8[petrol]
            map9_encoded = map9[regs]

            
            # Prepare data for prediction
            input_data = [[present_price,mileage,engine_volume,year,bmw_encoded,merc_encoded,mits_encoded,ren_encoded,toyota_encoded,volks_encoded,map1_encoded,map2_encoded,map3_encoded,map4_encoded,map5_encoded,map6_encoded,map7_encoded,map8_encoded,map9_encoded]]
            
            # Predict and display result
            predicted_price = model.predict(input_data)[0]
            print(f"Estimated Price: ₹{predicted_price:.2f}")
        except Exception as e:
            print(f"Error: {e}")

# Predict button
predict_button = widgets.Button(description="Predict")
predict_button.on_click(predict_price)

# Display inputs and button in the notebook
display(present_price_input,mileage_input,engine_volume_input,year_input,bmw_input,merc_input,mits_input,renault_input,toyota_input,volks_input,body_hatch_input,body_other_input,body_sedan_input,body_vagon_input,body_van_input,gas_input,other_input,petrol_input,registration_input predict_button, output)
