# this spec is really nasty right now.  It will fail when built with remote_rpm
# on the 9s, because they conditionally don't build mod_auth_system.  However,
# remote_rpm, running on the local machine (so long as it's not a solaris 9)
# machine, will query the spec, and try to scp back an RPM for the 9s.

# The workaround?  Use remote_rpm to build it on the other arches, then go 
# to each 2.9 build machine and use rpmbuild on them locally, it will succeed.
# Then scp the resulting RPMs back.

%define apver 1.3.29
%define apache_prefix /usr/local/apache-%{apver}

Summary: Netscape Roaming Access server Apache extension
Name: apache-module-mod_roaming
Version: 1.0.1
Release: 11
Group: Applications/Internet
License: BSD-type
Source: RU-apache-modules.tar.gz
BuildRoot: /var/tmp/%{name}-root
Provides: mod_roaming
Obsoletes: mod_roaming


# I don't see why pam? (Nor rcs...)
# BuildRequires: rcs pam apache = %{apver} apache-devel = %{apver}
BuildRequires: rcs apache apache-devel = %{apver}
Requires: apache

%description
With mod_roaming you can use your Apache webserver as a Netscape
Roaming Access server. This allows you to store your Netscape
Communicator 4.5 preferences, bookmarks, address books, cookies etc.
on the server so that you can use (and update) the same settings from
any Netscape Communicator 4.5 that can access the server.

%package -n apache-module-mod_auth_radius
Requires: apache
BuildRequires: rcs apache apache-devel = %{apver}
Version: 1.5.0
Group: Applications/Internet
Summary: Radius server authorization extension to Apache
Provides: mod_auth_radius
Obsoletes: mod_auth_radius

%description -n apache-module-mod_auth_radius
mod_radius allows users to request authentication via a Radius server.
Users can request that access to a directory require authentication
via radius by putting these commands in .htaccess.

%ifnos solaris2.9
%package -n apache-module-mod_auth_system
Requires: apache
BuildRequires: rcs apache apache-devel = %{apver}
Version: 1.2
Group: Applications/Internet
Summary: /etc/passwd authentication for Apache
Provides: mod_auth_system
Obsoletes: mod_auth_system

%description -n apache-module-mod_auth_system
mod_auth_system allows users to request authentication via
/etc/passwd.  Users can request that access to a directory require
authentication via by putting these commands in .htaccess.
%endif

%package -n apache-module-mod_log_dir
Requires: apache
BuildRequires: rcs apache apache-devel = %{apver}
Version: 1.13
Group: Applications/Internet
Summary: Enhanced logging extension to Apache
Provides: mod_log_dir
Obsoletes: mod_log_dir

%description -n apache-module-mod_log_dir
This module implements per-directory logging to pre-existing,
server-writable, logfiles using the config log module formatting syntax.
Sub-directory logging configurations override any logging their parent
directory's may have configured. Per-server logging already setup through
the use of the TransferLog directive is not overridden or effected by this
module. The config_log_module is required for linking this module and must
be included first in the Configuration file.

%prep
%setup -q -n apache_modules

%build
gunzip -c mod_roaming-1.0.1.tar.gz | tar xf -

RCS_FILES=`find . -name \*,v | sed 's/,v$//' | sed 's/^\.\///'`
rm -f $RCS_FILES
co $RCS_FILES

%ifnos solaris2.9
cd mod_auth_system
make clean
rm -f authprog # not destroyed by make clean
rm -f hold/*
perl -i -p -e 's/cc/gcc/' Makefile
make APXS="/usr/local/apache-%{apver}/bin/apxs" GLIBDIR=
cd ..
%endif

cd mod_auth_radius
make clean
make APXS="/usr/local/apache-%{apver}/bin/apxs" GLIBDIR=
cd ..

cd mod_log_dir # mod_log_dir_2 doesn't compile
make clean
make APXS="/usr/local/apache-%{apver}/bin/apxs" GLIBDIR=
cd ..

cd mod_roaming-1.0.1
rm -f mod_roaming.*o
/usr/local/apache-%{apver}/bin/apxs -c mod_roaming.c
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache-modules/

APACHE_MODULES=`find . -name \*.so | sed 's/^\.\///'`

for i in $APACHE_MODULES ; do
    install -c -m 0755 $i $RPM_BUILD_ROOT/usr/local/apache-modules/
%ifnos solaris2.9
    install -c -m 0755 mod_auth_system/authprog $RPM_BUILD_ROOT/usr/local/apache-modules
%endif
done

%post
cat <<EOF 
Extra Apache modules are now placed in /usr/local/apache-modules/
You need to install this module into your Apache configuration with apxs. 
EOF

%ifnos solaris2.9
%post -n apache-module-mod_auth_system
cat <<EOF 
Extra Apache modules are now placed in /usr/local/apache-modules/. 
You need to install this module into your Apache configuration with apxs. 
EOF
%endif

%post -n apache-module-mod_auth_radius
cat <<EOF 
Extra Apache modules are now placed in /usr/local/apache-modules/.
You need to install this module into your Apache configuration with apxs. 
EOF

%post -n apache-module-mod_log_dir
cat <<EOF 
Extra Apache modules are now placed in /usr/local/apache-modules/.
You need to install this module into your Apache configuration with apxs. 
EOF


%files
%defattr(-,root,other)
%doc README.RUTGERS mod_roaming-1.0.1/README
/usr/local/apache-modules/mod_roaming.so

#%ifnos solaris2.9
%files -n apache-module-mod_auth_system
%defattr(-,root,other)
%doc README.RUTGERS mod_auth_system/README
/usr/local/apache-modules/mod_auth_system.so
/usr/local/apache-modules/authprog
#%endif

%files -n apache-module-mod_auth_radius
%defattr(-,root,other)
%doc README.RUTGERS mod_auth_radius/README
/usr/local/apache-modules/mod_auth_radius.so

%files -n apache-module-mod_log_dir
%defattr(-,root,other)
%doc README.RUTGERS mod_log_dir/README
/usr/local/apache-modules/mod_log_dir.so
