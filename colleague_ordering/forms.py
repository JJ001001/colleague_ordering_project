from django import forms
from .models import Colleague, Equipment

class ColleagueForm(forms.ModelForm):

    class Meta:
        model = Colleague
        fields = "__all__" #can customise fields here ('firstname','sirname')
        # customer field from db to how you want it on the form on the frontend
        labels = {
            "firstname":"First Name", #firstname (db) : First Name (front end)
            'sirname': 'Sirname',
            'colleagueID': 'Colleague ID',
            'jobfamily': 'Job Family'
        }
    
    def __init__(self, *args, **kwargs):
        super(ColleagueForm,self).__init__(*args, **kwargs) #  (*args, **kwargs)  allows that function to accept an arbitrary number of arguments and/or keyword arguments.
        self.fields['jobfamily'].empty_label = "Select" #changes default drop down ----- to Select
        self.fields['status'].required = False #makes a field NOT manadatory

#TODO, NOT SURE HOW NOW TO LINK THIS TO A FORM IN VIEWS ETC, CREATED THE DB IN POSTGRES, AND CREATED THE CLASS BELOW, THATS IT FOR EQUIPMENT FORM

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = "__all__"
        labels = {
            "itemID":"Equipment Item ID", 
            'itemname': 'Product Name',
            'status': 'Stock Status',
        }
