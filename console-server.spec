Summary: Console server software and setup
Name: console-server
Version: 1.2
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: console-server-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Console-server contains console server software.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT
for i in etc/init.d/gnpsetup usr/local/etc/console.screenrc ; do
    mv $RPM_BUILD_ROOT/$i $RPM_BUILD_ROOT/$i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You probably want to edit and copy /etc/init.d/gnpsetup.rpm and
/usr/local/etc/console.screenrc.rpm.
EOF

%files
%defattr(-,root,other)
/usr/local/sbin/*
/usr/local/etc/console.screenrc.rpm
/usr/local/console
/usr/local/doc/console.help
