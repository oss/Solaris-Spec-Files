Summary: Enhanced talk client
Name: ytalk
Version: 3.1.1
Release: 2
Group: Applications/Internet
Copyright: GPL
Source: ytalk-3.1.1.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
for i in `find $RPM_BUILD_ROOT/etc -type f` ; do
    mv $i $i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You need to edit and move
    /etc/ytalkrc.rpm
EOF

%files
%defattr(-,bin,bin)
%doc README README.old BUGS INSTALL
/etc/ytalkrc.rpm
/usr/local/bin/ytalk
/usr/local/man/man1/ytalk.1
