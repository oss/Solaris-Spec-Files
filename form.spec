Summary: Form-to-email cgi-bin application
Name: ru-form-server

Version: 1.0
Release: 5
Group: Applications/Internet
License: RU
Source: form.tar.bz2
BuildRoot: /var/tmp/%{name}-root

Requires: webserver

%description
Form-to-email cgi-bin application


%package -n ru-form-client
Summary: Manual pages for form and make_html_data.
Group: Documentation
Provides: ru-form-roy

%description -n ru-form-client
Manual pages for form and make_html_data for the frontends.
Make_html_data,ets up directories for form if program is run setgid.


%prep
rm -rf %{buildroot}/*

%setup -q -n form

%build

make


%install
mkdir -p %{buildroot}/usr/local/man/man1/
mkdir -p %{buildroot}/usr/local/cgi-bin/
mkdir -p %{buildroot}/usr/local/bin/
cp form %{buildroot}/usr/local/cgi-bin/
cp make_html_data %{buildroot}/usr/local/bin/
cp form.1 make_html_data.1 %{buildroot}/usr/local/man/man1/



%clean
rm -rf %{buildroot}

%post
cat <<EOF
form should be setgid 'www' (or Apache's user) or setuid 'root'.
If you configure it is setgid 'www', you need the helper package 
form-frontend. You may wish to set form to setuid 'root', 
in which case  form-frontend is not needed.
EOF

%post -n ru-form-client
cat<<EOF
make_html_data needs to be run setuid 'root' setgid 'www' (or what
your apache runs as). This program is only needed if you do not run
'form' setuid 'root'.
EOF

%files
%defattr(0644,root,other) 
%doc INSTALL
%defattr(0755,root,other) 
/usr/local/cgi-bin/form

%files -n ru-form-client
%defattr(0644,root,other) 
/usr/local/man/man1/*
%defattr(0755,root,other) 
/usr/local/bin/make_html_data




