Name: grep
Version: 2.4.2
Copyright: GPL
Group: System Environment/Base
Summary: GNU grep
Release: 3
Source: grep-2.4.2.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Grep is an extremely powerful tool that lets you search through files
to match regular expressions.  GNU grep has a lot of options that Sun
grep lacks, so you may want to install this package.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

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
%doc COPYING
/usr/local/gnu/lib/locale/*/LC_MESSAGES/grep.mo
/usr/local/gnu/info/grep.info
/usr/local/gnu/man/man1/*
/usr/local/gnu/bin/*
