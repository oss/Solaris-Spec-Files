%define sourcetz  splus-6.0.tar.Z 
%define prefix    /usr/local/splus6

Summary: MathSoft statistics software
Name: splus
Version: 6.0
Release: 1
Group: Licensed
License: Licensed
Source: %{sourcetz}
BuildRoot: %{_tmppath}/%{name}-root

%description
SPLUS is commercial statistics software.  You need a valid license in
order to use this software.

%install
umask 022
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{prefix}
uncompress < %{_sourcedir}/%{sourcetz} | (cd %{buildroot}/%{prefix} && tar oxf -)

%clean
rm -rf %{buildroot}

%post
cat <<EOF
At this point the rpm package should be installed.  You will now need to
do a few steps concerning licensing and startup.

1) Run the HOSTINFO command from the %{prefix} directory.  This will
   give you a magic key that you send to SPLUS and then they send you
   back a license key.  Send the output from HOSTINFO to:

        ssr@statsci.com or fax to (206) 283-8691

2) Run the INSTALL command from the %{prefix} directory.  This will
   prompt you for the key information that you received from SPLUS.
   This will also start the license manager and test to be sure it is
   running properly.
EOF

%files
%defattr(-, root, bin)
%{prefix}
