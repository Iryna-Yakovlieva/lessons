def is_palindrome(text: str) -> bool:
	text = text.lower()
	text_all = ''.join(str(x) for x in text if text.isalnum())
	return text_all == text_all[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

