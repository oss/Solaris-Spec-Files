Name: indent
Version: 2.2.8
Release: 1
Copyright: GPL
Group: Development/Tools
Summary: indent is a C beautifier
Source: indent-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Indent is a program that reformats C code in several classic and modern
styles for your viewing pleasure.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	    /usr/local/info/indent.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/indent.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/indent
/usr/local/info/indent.info
/usr/local/man/man1/indent.1
