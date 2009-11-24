%define perl_version=5.6.1

Summary: SpamAssassin RU Language module
Name: perl-module-Mail-SpamAssassin-RULang
Version: 1.5
Release: 1
Group: System Environment/Base
License: apache
Source: RULang-%{version}.tar
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-Mail-SpamAssassin, perl-module-utf8simple
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
%doc README

%post
cat <<EOF
------------------------------------
Be sure to read /usr/local/doc/perl-module-Mail-SpamAssassin-RULang-%{version}/README and edit local.cf accordingly
------------------------------------
EOF

%changelog
* Tue Nov 24 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.5-1
- Bumped to version 1.5

* Tue Nov 10 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.4-1
- Bumped to version 1.4

* Mon Nov 09 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.3-1
- Bumped to version 1.3
- added perl-module-utf8simple to Requires

* Mon Nov 02 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.2-1
- Bumped to version 1.2
- added README to doc section

* Fri Oct 16 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.1-1
- Bumped to version 1.1

* Wed Aug 19 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-1
- Initial Build
