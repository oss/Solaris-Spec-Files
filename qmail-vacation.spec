Summary: Perl vacation script compatible with qmail
Name: qmail-vacation
Version: 1.0
Release: 3
Group: Applications/Internet
License: RU
Source: vacation
BuildRoot: /var/tmp/%{name}-root

Requires: perl qmail
Conflicts: vacation-perl+qmail vacation


%description
Rutgers-made Perl script to do what vacation does, but with qmail.

%prep
#%setup -q

%build


%install
mkdir -p %{buildroot}/usr/local/bin/
cp $RPM_SOURCE_DIR/vacation %{buildroot}/usr/local/bin/vacation


%clean
rm -rf %{buildroot}

%post
cat<<EOF
You may wish to> ln -s /usr/local/bin/vacation /usr/bin/vacation
EOF
#blank


%files
%defattr(0755,root,other) 
/usr/local/bin/vacation






