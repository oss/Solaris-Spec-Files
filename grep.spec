Name: grep
Version: 2.5.3
Copyright: GPL
Group: System Environment/Base
Summary: GNU grep
Release: 1
Source: grep-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: pcre-devel >= 7.7

%description
Grep is an extremely powerful tool that lets you search through files
to match regular expressions.  GNU grep has a lot of options that Sun
grep lacks, so you may want to install this package.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install prefix=%{buildroot}/usr/local/gnu

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/share/info \
		 /usr/local/gnu/share/info/grep.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/share/info \
		 /usr/local/gnu/share/info/grep.info
fi

%files
%defattr(-,root,bin)
%doc README COPYING AUTHORS NEWS THANKS ChangeLog
%doc /usr/local/gnu/share/man
%doc /usr/local/gnu/share/info
/usr/local/gnu/bin/*

%changelog
* Mon Jul 07 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-1
- Added changelog and updated to version 2.5.3
