Summary: Kerberos 5 base software
Name: kerberos-base
Version: 5.000203
Release: 1
Group: System Environment/Base
License: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Updated by S. Isaacson on 15 August 2001 to remove
passwd, chsh, chfn.

========

Updated by B. Binde on 3 February 2000 to remove 
kerbshell, pwshell and guestshell. kerbshell will be available
via the probsh package.  pwshell and guestshell are 
being removed.  

Also, the version of password from 

/sos/tint/old.junk/kerberos-980529/ 

was put in this package so that the hand copy of this program 
no longer needs to be done as part of the install. 

========

This package supplies the kerberos stuff needed to support the current
authentication software. 

this was gotten from a tarball located in: 

/rutgers/src/public/kerberos-distribution/client

a copy of the tarball used to make this package is in: 

/sos/src/kerberos5/981112

NOTE: the tarball contains the full kerberos dist.  I broke this into 2
parts, base and tools.  

Make sure that the kerberos service ports for kerberos are installed.
One way (YMMV) would be to do:

cat services >> /etc/services 

and then edit /etc/services to remove the old kerberos entries.  Be sure
to read the comments in the services file and remove old kerberos entries.

%prep
%setup -q -n files

%build
rm -f usr/bin/passwd
rm -f usr/bin/chsh
rm -f usr/bin/chfn
rm -f usr/lib/netsvc/yp/rpc.yppasswd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

%clean
rm -rf %{buildroot}

%files
%attr(-, root, daemon) /etc/*
%attr(-, bin, bin) /usr/local/man/*/*
%attr(-, bin, bin) /usr/local/krb5/man/*/*
%attr(-, root, daemon) /usr/local/krb5/sbin/*
%attr(-, root, daemon) /usr/local/krb5/bin/*
%attr(-, root, sysprog) /usr/local/bin/*
%attr(-, root, sysprog) /usr/local/sbin/*
