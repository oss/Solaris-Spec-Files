Summary: mail.local replacement
Name: mail.local
Version: 2001_9_6
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: mail.local-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Rutgers-specific mail.local replacement.

%prep
%setup -q -n mail.local

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/man/man8
install mail.local %{buildroot}/usr/local/lib
install mail.local.8 %{buildroot}/usr/local/man/man8

%clean
rm -rf %{buildroot}

%files
%attr(4511,root,other) /usr/local/lib/mail.local
%attr(0644,root,other) /usr/local/man/man8/mail.local.8