from django import forms

PERIOD_1 = (
    ('84', '12_недель'),
    ('70', '10_недель'),
    ('56', '8_недель')

)


PERIOD_2 = (
    ('28', '4_недели'),
    ('21', '3_недели'),
    ('14', '2_недели'),
    ('7', '1_неделю'),
)


class ForecastForm(forms.Form):
    base_period = forms.ChoiceField(
        label='Базовый период, дней', choices=PERIOD_1, initial='10_недель')
    forecast_period = forms.ChoiceField(
        label='Период прогноза, дней', choices=PERIOD_2, initial='4_недели')
