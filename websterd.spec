Name: websterd
Version: 1.9
Copyright: Purdue University/PD
Group: System/Daemons
Summary: Webster dictionary server
Release: 0
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
(from the man page)
websterd listens on a well-known socket for connections, and then accepts
commands to look up words.

%prep
%setup -q

%build
cd server
make clean
make nwebsterd
cd ../misc
rm makeindex
make makeindex

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/lib/oxford/webster/help
mkdir -p %{buildroot}/usr/local/man/man1
mkdir -p %{buildroot}/usr/local/man/man8

cp misc/makeindex %{buildroot}/usr/local/bin/makeindex
cp misc/makeindex.1 %{buildroot}/usr/local/man/man1
cp server/nwebsterd %{buildroot}/usr/local/bin/websterd
cp server/webster.conf %{buildroot}/usr/local/etc/webster.conf
cp help/*hlp help/protocol.doc %{buildroot}/usr/local/lib/oxford/webster/help
cp help/websterd.8 %{buildroot}/usr/local/man/man8

%post
cat <<EOF
You can consider adding to /etc/services

webster         765/tcp         dict

however, if you're at Rutgers, be warned that

#kerberos-adm   765/tcp                 # CAMSTUDENTS K5 admin/changepw


You'll need a dictionary to serve anything. We recommend:
/usr/local/lib/oxford/{cod8,thesaurus,quotations,world}{,.index,.hlp}


Those are copyrighted, so they're not included in this package.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc server/conf.doc
/usr/local/bin/*
%config(noreplace) /usr/local/etc/webster.conf
/usr/local/lib/oxford/webster/help/*
/usr/local/man/man1/makeindex.1
/usr/local/man/man8/websterd.8
