Summary: Radius authentication server
Name: radius
Version: 3.5.6
Release: 4
License: Commercial
Group: Applications/Internet
Source0: radius-3.5.6.tar.gz
Source1: radius-config.tar.gz
Patch0: RU-radius.patch
Patch1: radius-2.patch
BuildRoot: /var/tmp/%{name}-root

%description
Radius is an authentication server; this RPM has Rutgers-specific
hacks added.

%prep
%setup -q -n radius.3.5.6.basic
# shell scripts, text config files from tint package
%setup -q -D -T -n radius.3.5.6.basic -a 1
%patch -p1
%ifnos solaris2.6
%patch -p1 -P 1
%endif

%build
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/private/etc
mkdir -p $RPM_BUILD_ROOT/usr/local/private/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/local/private/man/man8
mkdir -p $RPM_BUILD_ROOT/etc
for i in radiusd radcheck radpwtst radpass dnscheck ; do
    install -m 0755 src/$i $RPM_BUILD_ROOT/usr/local/private/etc
done
for i in `ls man/*5 | sed 's/man\///'` ; do
    install -m 0644 man/$i $RPM_BUILD_ROOT/usr/local/private/man/man5/$i
done
for i in `ls man/*8 | sed 's/man\///'` ; do
    install -m 0644 man/$i $RPM_BUILD_ROOT/usr/local/private/man/man8/$i
done
(cd usr && find . | cpio -pd $RPM_BUILD_ROOT/usr)
(cd etc && find . | cpio -pd $RPM_BUILD_ROOT/etc)
for i in `find $RPM_BUILD_ROOT/etc/ -type f` ; do
    mv $i $i.rpm
done

cd $RPM_BUILD_ROOT
ln -s raddb.ici usr/local/private/etc/ici
ln -s raddb.general usr/local/private/etc/general
ln -s raddb.rci usr/local/private/etc/rci
ln -s raddb.njin usr/local/private/etc/njin

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
The following files need to be edited and copied:

   /etc/init.d/radius.rpm
   /etc/libru.conf.rpm
   /etc/libru.ici.rpm
   /etc/libru.rci.rpm
   /etc/rc2.d/S99radius.rpm
   /etc/ru_radius.conf.rpm

EOF

%files
%defattr(-,root,bin)
/etc/init.d/*
/etc/*.rpm
/etc/rc2.d/*
/usr/local/sbin/*
/usr/local/private/etc/*
/usr/local/private/man/man5/*
/usr/local/private/man/man8/*



