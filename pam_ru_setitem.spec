Summary: pam_ru_setitem PAM module
Name: pam_ru_setitem
Version: 1.0
Release: 4
Copyright: Rutgers University
Group: System/Authentication
Source: %{name}-%{version}.tar.gz
URL: http://oss.rutgers.edu/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Aaron Richton <richton@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Obsoletes: pam_setitem

%description
pam_ru_setitem.so.1 is used to call the pam_set_item(3PAM) function from within 
the PAM stack as defined in pam.conf(4).
(from the man page)

%prep
%setup -q

%build
%ifarch sparc64
gmake sparcv9 CFLAGS="-g -xs -xarch=generic64 -xcode=pic32"
gmake clean
%endif

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
cp pam_ru_setitem.5 $RPM_BUILD_ROOT/usr/local/man/man5
cp pam_ru_setitem.so.1 $RPM_BUILD_ROOT/usr/local/lib
%ifarch sparc64
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cp sparcv9/pam_ru_setitem.so.1 $RPM_BUILD_ROOT/usr/local/lib/sparcv9
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
This version was built with both 32bit and 64bit modules, as such you want to
make sure you have an appropriate pam.conf (should contain \$ISA items in the
module paths).

As part of this recompile the location of the modules was moved to fit in
better with the rest of the Rutgers pam items.
THIS WILL BREAK YOUR EXISTING pam.conf FILES. YOU WILL NEED TO MODIFY THE FILE
TO POINT TO THE NEW LOCATION /usr/local/lib/\$ISA/pam_ru_setitem.so.1
EOF

%files
%attr(644, root, bin) /usr/local/man/man5/pam_ru_setitem.5
%attr(755, root, root) /usr/local/lib/pam_ru_setitem.so.1
%ifarch sparc64
%attr(755, root, root) /usr/local/lib/sparcv9/pam_ru_setitem.so.1
%endif
