== How to re-enable Firstboot after first boot ==
To re-enable Firstboot, you need to do the following:

 1. rm /etc/sysconfig/firstboot
 2. systemctl enable firstboot-graphical.service

NOTE: /etc/reconfigSys is now (RHEL7) ignored.

== Advisory to porting Firstboot plugins ==

The legacy Firstboot tool is no longer in development and all current Firstboot users are advised to port their legacy Firstboot plugins to Anaconda addons, which don't have most of the limitations imposed by the Firstboot architecture.  Also unlike Firstboot plugins, Anaconda addons can be run both of during installation (by Anaconda), and after installation (by Initial Setup).

A comprehensive Anaconda Addon Development Guide is available:
http://rhinstaller.github.io/anaconda-addon-development-guide/

As well as an example "Hello world" addon:
https://github.com/rhinstaller/hello-world-anaconda-addon

Also the Kdump project recently successfully made the transition from a Firstboot plugin to an Anaconda addon and could be used as good reference example for a more advanced addon project:
https://github.com/daveyoung/kdump-anaconda-addon
