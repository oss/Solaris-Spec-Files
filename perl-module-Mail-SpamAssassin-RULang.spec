%define perl_version=5.6.1

Summary: SpamAssassin RU Language module
Name: perl-module-Mail-SpamAssassin-RULang
Version: 1.1
Release: 1
Group: System Environment/Base
License: apache
Source: RULang-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-Mail-SpamAssassin
BuildRequires: perl = %{perl_version}

%description
SpamAssassin language filtering plugin

%prep
%setup -q -n RULang-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/mail/spamassassin
cp RULang.pm $RPM_BUILD_ROOT/usr/local/etc/mail/spamassassin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/etc/mail/spamassassin/RULang.pm
%doc

%changelog
* Fri Oct 16 2009 Jarek Sedlacke <jarek@nbcs.rutgers.edu> - 1.1-1
- Bumped to version 1.1

* Wed Aug 19 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-1
- Initial Build
