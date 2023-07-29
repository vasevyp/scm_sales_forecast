from django import forms
from django.forms import ModelForm
from .models import Supplier, CategoryGoods, Goods, Buier 

class AddSupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields=['code', 'name','address', 'contact']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'rows':3}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),            
        }
class AddBuierForm(ModelForm):
    class Meta:
        model = Buier
        fields=['code', 'name','address', 'contact']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'rows':3}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),            
        }        
        

class AddCategoryGoodsForm(ModelForm):
    class Meta:
        model = CategoryGoods
        fields=['code', 'name']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'})
                    
        }
          
        
class AddGoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields=['name', 'code','category', 'supplier', 'unit','unit_cost', 'price','description', 'delivery_time', 'supply_pack', 'pack_weight', 'pack_length', 'pack_width', 'pack_height']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id': 'product'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'},),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control',  'rows':3}),
            'delivery_time':forms.NumberInput(attrs={'class':'form-control'}), 
            'supply_pack':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_weight':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_length':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_width':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_height':forms.NumberInput(attrs={'class':'form-control'}), 
           
              
        }           
        
