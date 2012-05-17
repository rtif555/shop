from django.forms import *
from shop.furnitures.models import *
from django.forms.widgets import SelectMultiple, Select
from django.db.models.query import QuerySet

class FindForm(Form):  
    type=TypedChoiceField(label = u"Тип")
    model=TypedChoiceField(label = u"Модель")             
    color=TypedChoiceField(label = u"Цвет")
    manufacturer=ModelChoiceField(label = u"Производитель", queryset = Producer.objects.none(), empty_label = '---------')	 
    
    def __init__(self,*args, **kwargs):        
        super(FindForm, self).__init__(*args, **kwargs)
        	
    def __init__(self, objects,*args, **kwargs):        
        super(FindForm, self).__init__(*args, **kwargs)		
        substitution=PieceOfFurniture.objects.all()
        for item in self.fields.keys():  #формируем select(-------,[выборка из базы])
            if item!='manufacturer':
                if item!='type':
                    substitution=objects
                else:
                    substitution.query.group_by = [item]
                self.fields[item].choices=substitution.values_list(item,item)
                self.fields[item].choices.insert(0,('---------','---------'))		      
        self.fields['manufacturer'].queryset=Producer.objects.filter(id__in=objects.values_list("manufacturer"))        
		
    def as_table(self):
        "Returns this form rendered as HTML <t>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<th>%(label)s</th><td>%(errors)s%(field)s%(help_text)s</td>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)

class ArmchairFormFind(Form):
    material=TypedChoiceField(label=u"Материал")
    has_gazopatron=BooleanField(label=u"Газоптрон")

class CupboardFormFind(Form):    
    quantity_of_doors=TypedChoiceField(label=u"Количество дверей")
    has_lock=BooleanField(label=u"Наличие замка")

class ChairFormFind(Form):
    quantity_of_legs=TypedChoiceField(label = u"Количество ножек ")
    height_spin=TypedChoiceField(label=u"Высота спинки")

class ShelfFind(PieceOfFurniture):
    max_weight=TypedChoiceField(label=u"Максимальная масса содержимого")#
				
class ArmchairFormAdd(ModelForm):
    class Meta:
        model = Armchair
        exclude = ('statys',)
	
    def as_tale(self):
        "Returns this form rendered as HTML <t>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<tr><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)

class ChairFormAdd(ModelForm):
    class Meta:
        model = Chair
        exclude = ('statys',)
		
    def as_tale(self):
        "Returns this form rendered as HTML <t>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<tr><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)

class CupboardFormAdd(ModelForm):
    class Meta:
        model = Cupboard
        exclude = ('statys',)
    
    def as_tale(self):
        "Returns this form rendered as HTML <t>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<tr><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)
		
class ShelfFormAdd(ModelForm):
    class Meta:
        model = Shelf
        exclude = ('statys',)

    def as_tale(self):
        "Returns this form rendered as HTML <t>s -- excluding the <table></table>."
        return self._html_output(
            normal_row = u'<tr><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row = u'<tr><td colspan="2">%s</td></tr>',
            row_ender = u'</td></tr>',
            help_text_html = u'<br /><span class="helptext">%s</span>',
            errors_on_separate_row = False)
			
class ProduserFormAdd(ModelForm):
    class Meta:
        model = Producer
    