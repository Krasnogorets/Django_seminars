from django import forms


class ChooseGame(forms.Form):
    game = forms.ChoiceField(choices=[('C', 'Coin'), ('R', 'Rnd'), ('D', 'Dice')])
    attempts = forms.IntegerField(min_value=1,max_value=64)
