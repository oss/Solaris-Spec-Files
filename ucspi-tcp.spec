Summary: Dan Bernstein's ucspi-tcp programs
Name: ucspi-tcp
Version: 0.88
Release: 2
Group: Applications/Internet
Copyright: BSD
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
   tcpserver and tcpclient are easy-to-use command-line tools for
   building TCP client-server applications.
(from the web page)

%prep
%setup -q
perl -i -p -e "s(/usr/local)($RPM_BUILD_ROOT/usr/local)" conf-home

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make setup check
# an ugly kludge:
for i in $RPM_BUILD_ROOT/usr/local/bin/* ; do
    if file $i | grep "shell" ; then
        perl -i -p -e "s($RPM_BUILD_ROOT)()g" $i
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
