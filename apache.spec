%include perl-header.spec

Name: apache
Version: 1.3.20
Release: 2
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: /var/tmp/%{name}-root
Source: apache_%{version}.tar.gz
Requires: perl

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  You will need to edit Apache's configuration files after
the installation.

%package devel
Summary: Apache include files, etc.
Group: Applications/Internet
Requires: apache

%description devel
This package consists of the Apache include files.

%package doc
Summary: Apache documentation
Group: Documentation

%description doc
This package consists of the Apache documentation.

%prep
%setup -q -n apache_%{version}

%build
./configure --with-layout=Apache --prefix=/usr/local/apache \
    --enable-module=so --enable-shared=max --with-perl=%{perl_binary}
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
# perl -i -p -e "s(/usr/local/apache)($RPM_BUILD_ROOT/usr/local/apache)" Makefile
make install root=$RPM_BUILD_ROOT
for i in $RPM_BUILD_ROOT/usr/local/apache/conf/* ; do
    mv $i $i.rpm
done
perl -i -p -e "s($RPM_BUILD_ROOT)()" $RPM_BUILD_ROOT/usr/local/apache/bin/apxs

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "You need to manually configure Apache; go to /usr/local/apache/conf."

%files
%defattr(-,root,other)
/usr/local/apache/bin
/usr/local/apache/libexec
/usr/local/apache/man
/usr/local/apache/conf
/usr/local/apache/icons
/usr/local/apache/cgi-bin

%files doc
%defattr(-,root,other)
/usr/local/apache/htdocs

%files devel
%defattr(-,root,other)
/usr/local/apache/include
