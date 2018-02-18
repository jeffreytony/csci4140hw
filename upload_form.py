#!/usr/bin/env python

print 'Content-type: text/html'
print
print"""
<html>
<body>
<form enctype="multipart/form-data" action="upload.py" method="POST">
    Choose an image (.jpg .gif .png): <br />
    <input type="file" name="pic" accept="image/gif, image/jpeg, image/png" /><br />
    <input type="submit" value="Upload" />
    <select>
    <option selected="selected" value="public">Public</option>
    <option value="private">Private</option>
    </select>
</form>
</body>
</html>"""