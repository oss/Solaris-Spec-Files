Name: gperf
Version: 2.7
Source: gperf-2.7.tar.gz
Release: 2
Summary: gperf is a perfect hash function generator
Copyright: GPL
Group: Development/Tools
BuildRoot: /var/tmp/%{name}-root

%description
Gperf generates perfect hash functions for sets of keywords---it
generates code that allows the recognition of keywords from a set of
words in roughly constant time.  It is used in gcc and indent, among
other programs.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	    /usr/local/info/gperf.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/gperf.info
fi

%files
%defattr(-,root,root)
%doc $RPM_BUILD_ROOT/usr/local/man/html/gperf.html 
%doc $RPM_BUILD_ROOT/usr/local/man/dvi/gperf.dvi
/usr/local/bin/gperf
/usr/local/info/gperf.info
/usr/local/man/man1/gperf.1

