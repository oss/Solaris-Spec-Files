%include machine-header.spec

%define apache_ver    2.0.35
%define apache_prefix /usr/local/apache2
%define gcc3_ver      3.0.4

Name: apache2
Version: %{apache_ver}
Release: 1
Summary: The Apache webserver
Copyright: BSD-like
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Source0: httpd-%{version}.tar.gz
Provides: webserver
Requires: perl openssl
BuildRequires: perl openssl flex make

%description
Apache is a powerful web server.  Install this package if you want to
use Apache.  

This package includes mod_ssl support.

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
%setup -n httpd-2.0.35

PATH="/usr/local/gcc-%{gcc3_ver}/bin:/usr/local/gnu/bin:$PATH"

export PATH

which gcc
which cpp

CC="/usr/local/gcc-%{gcc3_ver}/bin/gcc" ASCPP="/usr/local/gcc-%{gcc3_ver}/bin/cpp"

%ifarch sparc64
CC="/usr/local/gcc-%{gcc3_ver}/bin/gcc" ASCPP="/usr/local/gcc-%{gcc3_ver}/bin/cpp" ./configure --prefix=/usr/local/apache2 sparc64-sun-%{sol_os}
sed "s/-xarch=v8plus/-xarch=v9/" srclib/apr/atomic/solaris_sparc/Makefile > srclib/apr/atomic/solaris_sparc/Makefile.cjs 
sed "s/ASCPPFLAGS =.*-D_ASM/ASCPPFLAGS = -m64 -D_ASM/" srclib/apr/atomic/solaris_sparc/Makefile.cjs > srclib/apr/atomic/solaris_sparc/Makefile
%else
CC="/usr/local/gcc-%{gcc3_ver}/bin/gcc" ASCPP="/usr/local/gcc-%{gcc3_ver}/bin/cpp" ./configure --prefix=/usr/local/apache2 
%endif


#%ifarch sparc64
#sed "s/-xarch=v8plus/-xarch=v9/" srclib/apr/atomic/solaris_sparc/Makefile > srclib/apr/atomic/solaris_sparc/Makefile.cjs 
#sed "s/ASCPPFLAGS =.*-D_ASM/ASCPPFLAGS = -m64 -D_ASM/" srclib/apr/atomic/solaris_sparc/Makefile.cjs > srclib/apr/atomic/solaris_sparc/Makefile
#%endif

%build
make

#make certificate TYPE=dummy


%install
#TOPDIR=`pwd`

#rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/apache2

#cd $TOPDIR/%{apache_dir}
make install prefix=%{buildroot}/usr/local/apache2

#Make config not say build user / server
#sed "s/ServerAdmin.*rutgers.edu/ServerAdmin root@localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2

#sed "s/ServerName.*rutgers.edu/ServerName localhost/" %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2 > %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf

#rm %{buildroot}/usr/local/apache-%{apache_ver}/conf/httpd.conf2 


%clean
rm -rf %{buildroot}

%post
cat <<EOF
You must configure Apache before use (%{apache_prefix}/conf)
If upgrading from previous package revision (but same Apache version)
your configuration was left alone.

To utilize OpenSSL, you must replace the sample certificates that are
in %{apache_prefix}/conf/ssl*.

For instructions on how to make your very own certificate, see:
http://www.modssl.org/docs/2.8/ssl_faq.html#ToC28
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


%files doc
%defattr(-, root, other)
%{apache_prefix}/htdocs
%{apache_prefix}/man
%{apache_prefix}/manual

%files devel
%defattr(-, root, other)
%{apache_prefix}/include


%changelog
* Mon Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Updated Apache to 1.3.22, modssl 2.8.6

* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to Apache 1.3.22
- Added mod_ssl support
