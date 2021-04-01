## 一些漏洞的批量探测脚本

本目录下脚本均使用python3运行

urls.txt中保存需要探测的url，url格式没有太大限制，ip:port、http://xx.com/xxx/xxx 等格式都可以自动识别

改变输出颜色的函数写在源码中了但是没有使用，可根据自己需求修改

## 目前已经有的脚本

Apache Druid 命令执行漏洞 cve-2021-25646 druid_rce_poc.py

致远oa文件上传漏洞 CNTA-2021-0002 seeyon_upload_poc.py

VMware vRealize ssrf漏洞 CVE-2021-21975 vmware-vRealize-ssrf-poc.py
 
## ps
后续会慢慢增加
