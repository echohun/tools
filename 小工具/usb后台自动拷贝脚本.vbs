set fso=createobject("scripting.filesystemobject")
set ws=createobject("wscript.shell")
on error resume next
do
wscript.sleep 1000
if fso.driveexists("D:") then
fso.copyfile "D:*","C:\Users\Leticia\Desktop\copy"
fso.copyfolder "D:*","C:\Users\Leticia\Desktop\copy"
wscript.sleep 20000
end if
loop