Name: 		sed
Version: 	4.2.1
Release:	1
Group: 		System Environment/Base
License:	GPL
URL:		http://www.gnu.org/software/sed
Source: 	ftp://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:        The GNU stream editor

%description
sed is a stream editor. A stream editor is used to perform basic text 
transformations on an input stream (a file or input from a pipeline). 
While in some ways similar to an editor which permits scripted edits 
(such as ed), sed works by making only one pass over the input(s), 
and is consequently more efficient. But it is sed's ability to filter 
text in a pipeline which particularly distinguishes it from other types 
of editors. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure 			\
	--prefix=%{_prefix} 	\
	--infodir=%{_infodir}	\
	--mandir=%{_mandir}	\
	--disable-nls		

gmake -j3
gmake check

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_infodir}/dir 
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/sed.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/sed.info
fi

%files
%defattr(-, root, root)
%doc README BUGS NEWS
%doc COPYING AUTHORS THANKS
%doc doc/groupify.sed
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*

%changelog
* Fri Jul 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.2.1-1
- Updated to version 4.2.1
- Switched to sun compilers

* Tue Nov 13 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 4.1.4-3
- Disabled NLS

* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 4.1.4-2
- Updated to 4.1.4
