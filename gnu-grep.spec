Name:		grep
Version:	2.5.3
License:	GPL
Group:		System Environment/Base
Summary:	GNU grep
Release:	2
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		grep-%{version}.tar.gz
Patch:		grep-2.5.3-suncc.patch
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	make, pcre-devel >= 7.7

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

./configure --prefix=/usr/local/gnu		\
	    --mandir=/usr/local/gnu/man		\
            --infodir=/usr/local/gnu/info	\
	    --disable-nls
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/local/gnu/info/dir

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/grep.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/grep.info
fi

%files
%defattr(-,root,bin)
%doc README COPYING AUTHORS NEWS THANKS ChangeLog
%{_prefix}/gnu/bin/*grep
%{_prefix}/gnu/man/man1/*grep.1
%{_prefix}/gnu/info/grep.info

%changelog
* Wed Jul 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-2
- Fixed some paths and use Sun cc now

* Mon Jul 07 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-1
- Added changelog and updated to version 2.5.3
