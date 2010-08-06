%include perl-header.spec

Summary:      GNU shell tools
Name:         shtool
Version:      2.0.8
Release:      1
Group:        System Environment/Base
License:      GPL
Source:       http://ftp.gnu.org/gnu/shtool/shtool-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:     perl

%description
Shtool is a collection of shell scripts useful for distributions of
software.  If you are developing software that you plan to distribute,
using shtool may increase your portability, along with libtool and
autoconf.

%prep
%setup -q

%build
export PATH="%{perl_prefix}/bin:$PATH"
%configure

gmake

%check
gmake test

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

%post
cat <<EOF

Depending on your Perl installation, you may wish to change the first
line of shtoolize to read

  #!/usr/local/bin/perl

instead of

  #!/bin/perl

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README THANKS
%{_bindir}/shtool
%{_bindir}/shtoolize
%{_mandir}/man1/shtool*
%{_datadir}/aclocal/shtool.m4
%{_datadir}/shtool

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.0.8
- Update to 2.0.8
