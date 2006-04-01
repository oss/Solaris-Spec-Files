%define __find_requires %{nil}
%define __find_provides %{nil}

Name: iexplorer
Summary: Internet Explorer for Unix
Version: 5.0
Release: 2
Copyright: Commercial
Group: Applications/Internet
Source: ie5-oe-inst.tar.gz
Packager: Rutgers University
BuildRoot: /var/tmp/%{name}-root

%description
Microsoft Internet Explorer for Unix.

As an added bonus, this contains Outlook Express.

%prep
%setup -q -n microsoft

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/

cd .. # Go one above, we want to whole directory
cp -R microsoft $RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Internet Explorer (iexplorer) and Outlook Express (oexpress) has been
installing in:
    /usr/local/microsoft
Look in bin/ for the stuff to run.

Enjoy!!! :)

EOF

%files
%defattr(-,root,bin)
%dir /usr/local/microsoft
/usr/local/microsoft/*
/usr/local/microsoft/.oeversion

