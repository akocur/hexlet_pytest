from hexlet_pytest.example import reverse


def test_reverse():
	assert reverse('12345') == '54321'
	assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
	assert reverse('') == ''

