Summary: Rutgers version of sendmail mailer
Name: sendmail
Version: 8.8.8
Release: LCSR_1
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}-%{version}-lcsr.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Do not install this unless you know what you are doing!  If you need
an MTA, use qmail or postfix instead.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

echo "%defattr(-, root, bin)" >RPM_FILE_LIST
find . -type f -print | grep -v RPM_FILE_LIST | sed 's/^\.//' >>RPM_FILE_LIST

%clean
rm -rf %{buildroot}

%files -f RPM_FILE_LIST
