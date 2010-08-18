Summary:      Tool for automatically generating simple manual pages
Name:         help2man
# This is the latest version that runs with perl < 5.8
Version:      1.36.4
Release:      1
License:      GPL
Group:        Applications/Productivity
URL:          http://ftp.gnu.org/gnu/help2man/
Source:       http://ftp.gnu.org/gnu/help2man/help2man-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
help2man is a tool for automatically generating simple manual pages
from program output.

It is intended to provide an easy way for software authors to 
include a manual page in their distribution without having to 
maintain that document.

Given a program which produces resonably standard --help and 
--version outputs, help2man will attempt to re-arrange that output
into something which resembles a manual page.

%prep
%setup -q

%build
%configure --disable-nls

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=%{_infodir} %{_infodir}/%{name}.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=%{_infodir} \
		%{_infodir}/%{name}.info
fi

%files
%defattr(-,root,root,-)
%doc COPYING NEWS THANKS README debian/changelog
%{_mandir}/man1/*
%{_infodir}/%{name}*
%{_bindir}/*

%changelog
* Tue Aug 17 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.36.4-1
- Initial Solaris package
