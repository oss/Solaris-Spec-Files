Summary: mail.local replacement
Name: mail.local
Version: 1.6
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: mail.local-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Rutgers-specific mail.local replacement.

%prep
%setup -q

%build
ln -s Makefile.SOL2 Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
install mail.local $RPM_BUILD_ROOT/usr/local/lib
install mail.local.8 $RPM_BUILD_ROOT/usr/local/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(4511,root,other) /usr/local/lib/mail.local
%attr(0644,root,other) /usr/local/man/man8/mail.local.8