Summary: GNU trueprint
Name: trueprint
Version: 5.3
Release: 2
Group: Applications/Printing
License: GPL
URL: ftp://ftp.gnu.org/gnu/trueprint/
Source: ftp://ftp.gnu.org/gnu/trueprint/trueprint-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Trueprint is a general purpose program printing program.  It tries to
produce everything that anybody could need in a program printout
without the need for large numbers of switches or pipelines.
Trueprint can currently handle C, C++, Java, Perl, Verilog, shell
(including ksh), Pascal, pseudo C, report files (trueprint report
file, see NOTES), listing files, text files. [ from trueprint.1 ]

%prep
%setup -q

%build
%configure
gmake

%check
gmake check

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/local/share/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/share/info \
		 /usr/local/share/info/trueprint.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/share/info \
		 /usr/local/share/info/trueprint.info
fi

%files
%defattr(-,bin,bin)
%doc README COPYING NEWS
/usr/local/bin/trueprint
%{_mandir}/man1/*
/usr/local/share/info/trueprint.info

%changelog
* Fri Aug 06 2010 Steven Lu <sjlu@nbcs.rutgers.edu>
- bump, spec file update
