Summary: An SGML DTD for technical documentation.
Name: docbook
%define version 3.1
%define release 3
Version: %{version}
Release: %{release}
Copyright: Copyright 1992, 1993, 1994, 1995, 1996 HaL Computer Systems, Inc., O'Reilly & Associates, Inc., ArborText, Inc., and Fujitsu Software Corporation.
Prereq: sgml-common
Source: docbook-%{version}.tgz 
Source1: docbook-3.0.tgz
Group: Applications/Text
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root
Prefix: /usr/local


%description
DocBook is an SGML DTD (document type definition). DTDs define how the
markup tags in SGML documents should be interpreted. DocBook is well
suited for the creation of books and papers about computer hardware
and software.

%prep
%setup -q -c -b1

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/sgml/docbook-3.0
mkdir -p $RPM_BUILD_ROOT/%{prefix}/lib/sgml/docbook-3.1
install -c -m644 dtd/docbook-3.1/*.mod dtd/docbook-3.1/*.dtd \
    dtd/docbook-3.1/*.cat dtd/docbook-3.1/*.dcl \
    $RPM_BUILD_ROOT/%{prefix}/lib/sgml/
install -c -m644 dtd/docbook-3.0/*.mod dtd/docbook-3.0/*.dtd \
    dtd/docbook-3.0/*.cat dtd/docbook-3.0/*.dcl \
    $RPM_BUILD_ROOT/%{prefix}/lib/sgml/docbook-3.0

%clean
rm -rf $RPM_BUILD_ROOT

%post
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{prefix}/bin/install-catalog --install docbook --version $V >/dev/null
V=3.0-%{version}-%{release}
%{prefix}/bin/install-catalog --install docbook-3.0/docbook --version $V >/dev/null

%postun
# since old-postun is run *after* new-post, we must always cycle.
V=%{version}-%{release}
%{prefix}/bin/install-catalog --remove docbook --version $V >/dev/null
V=3.0-%{version}-%{release}
%{prefix}/bin/install-catalog --remove docbook-3.0/docbook --version $V >/dev/null

%files
%defattr(-,root,root)
%doc dtd/docbook-3.1/*.txt dtd/docbook-3.1/ChangeLog
%{prefix}/lib/sgml/*

%changelog
* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- fix %pre/%post

* Wed Jan  5 2000 Bill Nottingham <notting@redhat.com>
- add in docbook-3.0 stuff
- sanitize specfile

* Mon Nov 8 1999 Tim Powers <timp@redhat.com>
- updated to 3.1

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- changed buildroot to /var/tmp/docbook-root
- updated source download location
- built for 6.1

* Fri Apr 23 1999 Michael K. Johnson <johnsonm@redhat.com>
- quiet scripts
