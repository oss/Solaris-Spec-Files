Summary: Batch RPM tool
Name: build-repository
Version: 9.13.2001
Release: 1
Copyright: Rutgers
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl

%description
Build-repository lets you build massive amounts of RPMs at once.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 build-r.pl %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%post
if [ ! -x /usr/local/bin/perl ]; then
    echo "You need to link perl to /usr/local/bin/perl."
fi

%files
%defattr(-, root, bin)
%doc *profile instructions.html
/usr/local/bin/build-r.pl
