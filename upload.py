#!/usr/bin/python

import os
import cgi
import cgitb
import subprocess
import sys



print "Content-Type: text/html"
print

cgitb.enable()

form = cgi.FieldStorage()


print '<html><body>'

saveDir = './data'
readDir = '/data'

if ('pic' not in form):
    print "No file uploaded. "
elif (not form['pic'].filename):
    print "No file selected. "
else:
    fileitem = form['pic']
    filelocate = "./data/" + (fileitem.filename)
    #save file in local dir
    (fn, ext) = os.path.splitext(os.path.basename(fileitem.filename))
    savePath = os.path.join(saveDir, fn + ext)
    open(savePath, 'wb').write(fileitem.file.read())


    cmd = ['identify', (filelocate)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()

    """
    print '''<table>
    <tr><td>cmd</td><td>%s</td></tr>
    <tr><td>stdout</td><td>%s</td></tr>
    <tr><td>stderr</td><td>%s</td></tr>
    </table>''' % (cmd, out.replace('\n', '<br />'), err.replace('\n', '<br />'))
    """

    file_ext = str(fileitem.filename.split("."))

    out= out.split(" ")
    if(len(out) == 1):
        print ("error: wrong file format")
    else:
        filetype = out[1]
        print(filetype)
        if (filetype.find("JPEG") == -1) and (filetype.find("PNG") == -1) and (filetype.find("GIF") == -1):
            print ("error: wrong file format")
        elif (filetype.find("JPEG") != -1) and file_ext.find("jpg") == -1:
            print ("error: wrong file format not consist")
        elif (filetype.find("PNG") != -1) and file_ext.find("png") == -1:
            print ("error: wrong file format not consist")
        elif (filetype.find("GIF") != -1) and file_ext.find("gif") == -1:
            print ("error: wrong file format not consist")
        else:
            print "Filename: " + fileitem.filename
            print 'File uploaded. <br /><img src="%s" />'%(os.path.join('/data', fn + ext))
            print'''
            <form method="post" action="editor.py">
                <input type="submit" name="action" value="Go to Editor" />
            </form>'''

    #print (filetype[1])



    print '</body></html>'