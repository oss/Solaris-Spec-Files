%define gnu_prefix %{_prefix}/gnu

Name:		grep
Version:	2.5.4
License:	GPL
Group:		System Environment/Base
Summary:	GNU grep
Release:	1
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		ftp://ftp.gnu.org/gnu/grep/%{name}-%{version}.tar.gz
Patch:		grep-2.5.3-suncc.patch
URL:		http://www.gnu.org/software/grep/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	pcre-devel >= 7.7

%description
Grep is an extremely powerful tool that lets you search through files
to match regular expressions.  GNU grep has a lot of options that Sun
grep lacks, so you may want to install this package.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=%{gnu_prefix}		\
	    --mandir=%{gnu_prefix}/man		\
            --infodir=%{gnu_prefix}/info	\
	    --disable-nls
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{gnu_prefix}/info/dir

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{gnu_prefix}/info \
		 %{gnu_prefix}/info/grep.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --delete --info-dir=%{gnu_prefix}/info \
		 %{gnu_prefix}/info/grep.info
fi

%files
%defattr(-,root,bin)
%doc README COPYING AUTHORS NEWS THANKS ChangeLog
%{gnu_prefix}/bin/*grep
%{gnu_prefix}/man/man1/*grep.1
%{gnu_prefix}/info/grep.info

%changelog
* Mon Mar 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.4-1
- Updated to version 2.5.4

* Wed Jul 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-2
- Fixed some paths and use Sun cc now

* Mon Jul 07 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-1
- Added changelog and updated to version 2.5.3
