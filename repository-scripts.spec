Summary: rpm.rutgers.edu maintenance tools
Name: repository-scripts
Version: 9.13.2001
Release: 1
Copyright: Rutgers
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl gnupg apt-server-tools textutils rpm2html

%description
Repository-scripts includes signature-checking and rpm-installing
scripts designed to automate the maintenance of rpm.rutgers.edu.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 check_sigs.pl %{buildroot}/usr/local/bin
install -m 0755 update-apt.pl %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%post
if [ ! -x /usr/local/bin/perl ]; then
    echo "You need to link perl to /usr/local/bin/perl."
fi

%files
%defattr(-, root, bin)
%doc *html
/usr/local/bin/*
