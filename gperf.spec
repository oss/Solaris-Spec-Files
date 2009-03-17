Summary:        Perfect hash function generator
Name: 		gperf
Version:	3.0.4
Release: 	1	
License: 	GPL
Group: 		Development/Tools
Source:         ftp://ftp.gnu.org/gnu/gperf/gperf-%{version}.tar.gz
URL:		http://www.gnu.org/software/gperf/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
GNU gperf is a perfect hash function generator. For a given list of strings, 
it produces a hash function and hash table, in form of C or C++ code, for 
looking up a value depending on the input string. The hash function is perfect, 
which means that the hash table has no collisions, and the hash table lookup 
needs a single string comparison only.

GNU gperf is highly customizable. There are options for generating C or C++ 
code, for emitting switch statements or nested ifs instead of a hash table, 
and for tuning the algorithm employed by gperf. 

%prep
%setup -q

%build
./configure			\
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir} 	\
	--infodir=%{_infodir}
gmake
gmake check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_datadir}/doc/gperf.html

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} \
	    %{_infodir}/gperf.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --delete --info-dir=%{_infodir} \
	    %{_infodir}/gperf.info
fi

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS
%doc NEWS ChangeLog
%doc doc/gperf.html
%{_bindir}/gperf
%{_infodir}/gperf.info
%{_mandir}/man1/gperf.1

%changelog
* Tue Mar 17 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.0.4-1
- Updated to version 3.0.4
- Now use Sun cc
- Added changelog
