Summary: Configurable menu-driven front end to Unix
Name: lush
Version: 1.3
Release: 3
Group: System Environment/Base
Copyright: Rutgers
Source: lush.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Added extra files so that lush can run on 2.7 frontend machines
without hanging xsession.  These files are:
        /etc/dt/config/C/sys.session.sample
                (this is to get lush running on cde)
        /usr/local/bin/lush - NOW A WRAPPER FOR ....
        /usr/local/bin/menus - a link to /usr/local/bin/lush
        /usr/local/bin/lush.real

/usr/local/bin/lush also invokes /usr/local/bin/asklush to see if
anyone wants to keep the menus before executing lush.

Lush is a configurable user-friendly menu-driven front end 
to Unix. It is intended to help novice users gain access to 
services on a Unix system without having to learn the 
basics of Unix itself. 

This package has been engineered such that sysadmins may 
opt to create/maintain local lush menu configuration files. 
The package comes with 2 sample files .... to guide you
with making your setup.  You MUST have /usr/local/lush/lushrc
and /usr/local/lush/lushmenu for lush to work.

INSTALLED SAMPLE FILES:
        /usr/local/lush/lushrc.sample
        /usr/local/lush/lushmenu.sample

%prep
%setup -q -n lush

%build
make clean
make
mv lush lush.real

%install
rm -rf $RPM_BUILD_ROOT
for i in bin man/man1 lush ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
mkdir -p $RPM_BUILD_ROOT/etc/dt/config/C

install -m 0755 EXTRA.FILES/lush $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 EXTRA.FILES/asklush $RPM_BUILD_ROOT/usr/local/bin
install -m 0644 EXTRA.FILES/sys.session.sample $RPM_BUILD_ROOT/etc/dt/config/C
install -m 0755 lush.real $RPM_BUILD_ROOT/usr/local/bin
install -m 0644 RU.FILES/lush.1 $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0644 RU.FILES/lushrc.sample $RPM_BUILD_ROOT/usr/local/lush
install -m 0644 RU.FILES/menu.sample \
    $RPM_BUILD_ROOT/usr/local/lush/lushmenu.sample

cd $RPM_BUILD_ROOT/usr/local/bin
ln -s lush menus

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

This package has been engineered such that sysadmins may 
opt to create/maintain local lush menu configuration files. 
The package comes with 2 sample files .... to guide you
with making your setup.  You MUST have /usr/local/lush/lushrc
and /usr/local/lush/lushmenu for lush to work.

INSTALLED SAMPLE FILES:
        /usr/local/lush/lushrc.sample
        /usr/local/lush/lushmenu.sample

EOF

%files
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/lush/*
/usr/local/man/man1/lush.1
/etc/dt/config/C/sys.session.sample
