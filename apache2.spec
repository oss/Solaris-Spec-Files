%define apache_ver    2.0.50
%define apache_prefix /usr/local/apache2-%{apache_ver}

Name: apache2
Version: %{apache_ver}
Release: 1
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Source0: httpd-%{version}.tar.gz
Provides: webserver
Requires: perl openssl gdbm expat db4
BuildRequires: perl openssl flex make db4-devel >= 4.2

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  

This package includes mod_ssl support.


%package devel
Summary: Apache include files, etc.
Group: Applications/Internet
Requires: apache2

%description devel
This package consists of the Apache include files.


%package doc
Summary: Apache documentation
Group: Documentation
Requires: apache2

%description doc
This package consists of the Apache documentation.



%prep
%setup -n httpd-%{apache_ver}
SSL_BASE="/usr/local/ssl"
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib"

export LDFLAGS
export SSL_BASE

which gcc
which cpp

LD_LIBRARY_PATH="/usr/local/lib" LD_RUN_PATH="/usr/local/lib" \
./configure --enable-ssl=static --prefix=/usr/local/apache2-%{version}

%build

LD_LIBRARY_PATH="/usr/local/lib" LD_RUN_PATH="/usr/local/lib" make

#make certificate TYPE=dummy

%install
mkdir -p %{buildroot}/usr/local/apache2-%{version}

make install DESTDIR=%{buildroot} 
cd %{buildroot}/usr/local 
ln -s apache2-%{version} apache2


#Make config not say build user / server
#sed "s/ServerAdmin.*rutgers.edu/ServerAdmin root@localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2


# I don't know why I ever did this, don't know if it actually does anything. --cjs

cd %{buildroot}%{apache_prefix}/conf/

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" highperformance-std.conf > highperformance-std.conf2
sed "s/Group #-1/Group nobody/" highperformance-std.conf2 > highperformance-std.conf
rm highperformance-std.conf2

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" highperformance.conf > highperformance.conf2
sed "s/Group #-1/Group nobody/" highperformance.conf2 > highperformance.conf
rm highperformance.conf2

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" httpd-std.conf >httpd-std.conf2
sed "s/Group #-1/Group nobody/" httpd-std.conf2 > httpd-std.con
rm httpd-std.conf2

#sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" httpd-std.conf.in >httpd-std.conf.in2
#sed "s/Group #-1/Group nobody/" httpd-std.conf.in2 > httpd-std.conf.in
#rm httpd-std.conf.in

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" httpd.conf >httpd.conf2
sed "s/Group #-1/Group nobody/" httpd.conf2 > httpd.conf
rm httpd.conf2

#sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" httpd.conf.in >httpd.conf.in2
#sed "s/Group #-1/Group nobody/" httpd.conf.in2 > httpd.conf.in
#rm httpd.conf.in

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" ssl-std.conf > ssl-std.conf2
mv ssl-std.conf2 ssl-std.conf

sed "s/export\/home\/richton\/tmp\/apache2-root\/usr/usr/" ssl.conf >ssl.conf2
mv ssl.conf2 ssl.conf

#sed "s/ServerName.*rutgers.edu/ServerName localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2 > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf

#rm %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2


%clean
rm -rf %{buildroot}

%post
cat <<EOF
You must configure Apache before use (%{apache_prefix}/conf)
If upgrading from previous package revision (but same Apache version)
your configuration was left alone.

Apache 1.3.* modules are not compatible with this release.

THERE ARE NO EXAMPLE SSL CERTIFICATES DISTRIBUTED WITH THIS RELEASE
IN ORDER TO USE SSL YOU MUST CREATE SSL CERTIFICATES, read here:
   http://httpd.apache.org/docs-2.0/ssl/ssl_faq.html#realcert
EOF

%files
%defattr(-, root, other)
#%{apache_prefix}
%{apache_prefix}/bin
%{apache_prefix}/build
%{apache_prefix}/cgi-bin
%config(noreplace)%{apache_prefix}/conf
%{apache_prefix}/error
%{apache_prefix}/icons
%{apache_prefix}/lib
%{apache_prefix}/logs
%{apache_prefix}/modules
%config(noreplace) /usr/local/apache2

%files doc
%defattr(-, root, other)
%{apache_prefix}/htdocs
%{apache_prefix}/man
%{apache_prefix}/manual

%files devel
%defattr(-, root, other)
%{apache_prefix}/include


%changelog
* Wed Aug 25 2004 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
- Updated Apache to 2.0.50

* Tue Feb 4 2003 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Apache2 build

* Mon Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Updated Apache to 1.3.22, modssl 2.8.6

* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to Apache 1.3.22
- Added mod_ssl support
