#!/usr/bin/env python

print 'Content-type: text/html'
print
print"""
<html>
<body>
  <form method="post" action="login.py">
    Username: <input type="text" name="user" /><br />
    Password: <input type="password" name="password" /><br />
    <input type="hidden" name="hehe" value="You cannot see me =D" />
    <input type="submit" name="action" value="LOGIN" />
  </form>
  <form method="post" action="createacc.py">
    Username: <input type="text" name="user" /><br />
    Password: <input type="password" name="password" /><br />
    Retype Password: <input type="password" name="password" /><br />
    <input type="hidden" name="hehe" value="You cannot see me =D" />
    <input type="submit" name="action" value="CREATE" />
  </form>
</body>
</html>"""