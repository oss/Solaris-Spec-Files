Summary: X-based commercial email reader
Name: Zmail
Version: 4.0
Release: 3
Group: System Environment/Base
Copyright: Rutgers
Source: Zmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Zmail is an X-based commercial email reader.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

%post 
ln -s /usr/local/Zmail/doc /usr/local/doc/Zmail-%{version}
ln -s /usr/local/Zmail/bin.zmail.4.0 /usr/local/Zmail/bin.zmail
ln -s /usr/local/Zmail/bin.zmlite.4.0 /usr/local/Zmail/bin.zmlite
ln -s /usr/local/Zmail/lib.zmail.4.0 /usr/local/Zmail/lib.zmail
ln -s /usr/local/Zmail/lib.zmlite.4.0 /usr/local/Zmail/lib.zmlite

%preun
rm -f /usr/local/doc/Zmail-%{version}
rm -f /usr/local/Zmail/bin.zmail
rm -f /usr/local/Zmail/bin.zmailite
rm -f /usr/local/Zmail/lib.zmail
rm -f /usr/local/Zmail/lib.zmailite

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%dir /usr/local/Zmail
/usr/local/bin/zmail
/usr/local/bin/zmail.small
/usr/local/bin/zmlite
/usr/local/Zmail/Doc
%attr(2755, root, mail) /usr/local/Zmail/bin.zmail.4.0/zmail
%attr(2755, root, mail) /usr/local/Zmail/bin.zmail.4.0/zmail.small
%attr(-, root, mail) /usr/local/Zmail/bin.zmlite.4.0/zmlite
%attr(2755, root, mail) /usr/local/Zmail/bin.zmlite.4.0/zmlite.solar25
%attr(-, root, mail) /usr/local/Zmail/bin.zmlite.4.0/ztermkey
/usr/local/Zmail/lib.RU
/usr/local/Zmail/lib.zmail.4.0
/usr/local/Zmail/lib.zmlite.4.0
/usr/local/X11R5/lib/X11/app-defaults/Zmail
/usr/local/lib/app-defaults/Zmail/Zmail
