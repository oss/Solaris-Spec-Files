Summary: Apache logfile program w/strftime(3) support
Name: httplog
Version: 2.1
Release: 1
License: FREE SOFTWARE LICENSE
Group: Applications/Internet
Source: httplog-2.1.tar.gz
BuildRoot: /var/tmp/%{name}-root
URL: http://nutbar.chemlab.org/
Requires: zlib
BuildRequires: zlib-devel

%description
This program is intended to be a logfile rollover program for the Apache web
server.

%prep 
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib"
export LD_LIBRARY_PATH
./configure --prefix=$RPM_BUILD_ROOT/usr/local
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
Edit your httpd.conf and add
CustomLog "|/usr/local/bin/httplog /path/to/logfiles/ex%Y%m%d.log"
in the section where lines like this already exist.
EOF

%files
%defattr(755,root,root) 
/usr/local/bin/httplog
%defattr(644,root,root) 
/usr/local/man/man8/httplog.8

%changelog
* Tue Feb 5 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Initial package
